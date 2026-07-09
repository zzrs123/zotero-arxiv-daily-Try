param(
    [string]$Repository = "zzrs123/zotero-arxiv-daily-Try",

    [ValidateRange(1, 168)]
    [int]$LookbackHours = 72,

    [ValidateRange(1, 240)]
    [int]$DownloadTimeoutMinutes = 60,

    [switch]$Backfill,

    [switch]$SkipDaily,

    [switch]$SkipManual,

    [switch]$SkipTracking,

    [switch]$CommitMetadata,

    [switch]$PushMetadata,

    [switch]$ForceDownload
)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$stateDir = Join-Path $repoRoot ".local-state"
$statePath = Join-Path $stateDir "artifact-sync.json"
$tempRoot = Join-Path $env:TEMP "paper-daily-artifact-sync"

function Assert-Command {
    param([string]$Name)

    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command '$Name' was not found."
    }
}

function Initialize-GitHubAuthEnvironment {
    if ([string]::IsNullOrWhiteSpace($env:GH_TOKEN)) {
        $userToken = [Environment]::GetEnvironmentVariable("GH_TOKEN", "User")
        if (-not [string]::IsNullOrWhiteSpace($userToken)) {
            $env:GH_TOKEN = $userToken
        }
    }

    if ([string]::IsNullOrWhiteSpace($env:GITHUB_TOKEN) -and -not [string]::IsNullOrWhiteSpace($env:GH_TOKEN)) {
        $env:GITHUB_TOKEN = $env:GH_TOKEN
    }
}

function Load-State {
    if (-not (Test-Path -LiteralPath $statePath)) {
        return @{ downloaded_artifact_ids = @() }
    }

    $loaded = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
    return @{
        downloaded_artifact_ids = @($loaded.downloaded_artifact_ids)
    }
}

function Save-State {
    param([hashtable]$State)

    New-Item -ItemType Directory -Force -Path $stateDir | Out-Null
    $State | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $statePath -Encoding utf8
}

function Invoke-GhJson {
    param(
        [string[]]$Arguments,
        [int]$MaxAttempts = 4
    )

    $lastOutput = ""
    for ($attempt = 1; $attempt -le $MaxAttempts; $attempt++) {
        $output = & gh @Arguments 2>&1
        $lastOutput = ($output | Out-String).Trim()
        if ($LASTEXITCODE -eq 0) {
            return $output | ConvertFrom-Json
        }

        if ($attempt -lt $MaxAttempts) {
            $waitSeconds = [Math]::Min(60, 5 * $attempt)
            Write-Host "GitHub CLI failed on attempt $attempt/$MaxAttempts: gh $($Arguments -join ' ')"
            if ($lastOutput) { Write-Host $lastOutput }
            Write-Host "Retrying in $waitSeconds seconds..."
            Start-Sleep -Seconds $waitSeconds
        }
    }

    throw "GitHub CLI failed after $MaxAttempts attempts: gh $($Arguments -join ' ')`n$lastOutput"
}

function Format-FileSize {
    param([long]$Bytes)

    if ($Bytes -ge 1GB) { return "{0:N1} GB" -f ($Bytes / 1GB) }
    if ($Bytes -ge 1MB) { return "{0:N1} MB" -f ($Bytes / 1MB) }
    if ($Bytes -ge 1KB) { return "{0:N1} KB" -f ($Bytes / 1KB) }
    return "$Bytes B"
}

function Get-RecentRuns {
    param(
        [string]$WorkflowFile,
        [string[]]$Statuses = @("success"),
        [int]$MaxRuns = 1
    )

    $candidateRuns = if ($Backfill) { 20 } else { [Math]::Max($MaxRuns, 5) }
    $limit = $candidateRuns
    $runs = @()
    foreach ($status in $Statuses) {
        $statusRuns = Invoke-GhJson @(
            "run", "list",
            "--repo", $Repository,
            "--workflow", $WorkflowFile,
            "--status", $status,
            "--limit", "$limit",
            "--json", "databaseId,createdAt,displayTitle,status,conclusion"
        )
        $runs += @($statusRuns)
    }
    $cutoff = (Get-Date).ToUniversalTime().AddHours(-$LookbackHours)
    $filtered = @(
        $runs |
            Group-Object databaseId |
            ForEach-Object { $_.Group | Select-Object -First 1 } |
            Where-Object { ([datetime]$_.createdAt).ToUniversalTime() -ge $cutoff }
    )
    if (-not $Backfill) {
        $filtered = @($filtered | Sort-Object createdAt -Descending | Select-Object -First $candidateRuns)
        return @($filtered | Sort-Object createdAt -Descending)
    }
    return @($filtered | Sort-Object createdAt)
}

function Sync-WorkflowArtifacts {
    param(
        [string]$WorkflowFile,
        [string]$ArtifactName,
        [string]$Destination,
        [string[]]$RunStatuses = @("success"),
        [hashtable]$State
    )

    $runs = @((Get-RecentRuns -WorkflowFile $WorkflowFile -Statuses $RunStatuses))
    if ($runs.Count -eq 0) {
        Write-Host "No recent matching runs found for $WorkflowFile."
        return
    }

    $modeLabel = if ($Backfill) { "backfill" } else { "latest-only" }
    Write-Host "[$modeLabel] Found $($runs.Count) run(s) for $WorkflowFile."

    foreach ($run in $runs) {
        $artifactResponse = Invoke-GhJson @(
            "api", "repos/$Repository/actions/runs/$($run.databaseId)/artifacts"
        )
        $artifacts = @($artifactResponse.artifacts | Where-Object {
            $_.name -eq $ArtifactName -and -not $_.expired
        })

        if ($artifacts.Count -eq 0) {
            Write-Host "  Run $($run.databaseId): no '$ArtifactName' artifact found, skipping."
            continue
        }

        foreach ($artifact in $artifacts) {
            $artifactId = [string]$artifact.id
            if (-not $ForceDownload -and $State.downloaded_artifact_ids -contains $artifactId) {
                Write-Host "  Run $($run.databaseId): artifact $artifactId already synced, skipping."
                continue
            }

            $sizeStr = Format-FileSize $artifact.size_in_bytes
            Write-Host "  Run $($run.databaseId): downloading $ArtifactName ($sizeStr)..."

            $staging = Join-Path $tempRoot "$($run.databaseId)-$artifactId"
            Remove-Item -LiteralPath $staging -Recurse -Force -ErrorAction SilentlyContinue
            New-Item -ItemType Directory -Force -Path $staging | Out-Null

            $psi = [System.Diagnostics.ProcessStartInfo]::new()
            $psi.FileName = (Get-Command gh).Source
            $psi.Arguments = "run download $($run.databaseId) --repo $Repository --name $ArtifactName --dir `"$staging`""
            $psi.UseShellExecute = $false
            $psi.CreateNoWindow = $true
            $psi.RedirectStandardError = $true
            $psi.RedirectStandardOutput = $true

            $proc = [System.Diagnostics.Process]::Start($psi)
            $ok = $proc.WaitForExit([int]($DownloadTimeoutMinutes * 60 * 1000))
            $stdout = $proc.StandardOutput.ReadToEnd()
            $stderr = $proc.StandardError.ReadToEnd()

            if (-not $ok) {
                Stop-Process -Id $proc.Id -Force -ErrorAction SilentlyContinue
                Remove-Item -LiteralPath $staging -Recurse -Force -ErrorAction SilentlyContinue
                Write-Host "  Run $($run.databaseId): download timed out after $DownloadTimeoutMinutes min, skipping."
                continue
            }

            if ($proc.ExitCode -ne 0) {
                Remove-Item -LiteralPath $staging -Recurse -Force -ErrorAction SilentlyContinue
                Write-Host "  Run $($run.databaseId): download failed (exit $($proc.ExitCode)), skipping."
                if ($stdout) { Write-Host $stdout.Trim() }
                if ($stderr) { Write-Host $stderr.Trim() }
                continue
            }

            New-Item -ItemType Directory -Force -Path $Destination | Out-Null
            Get-ChildItem -LiteralPath $staging -Force | ForEach-Object {
                Copy-Item -LiteralPath $_.FullName -Destination $Destination -Recurse -Force
            }

            if ($State.downloaded_artifact_ids -notcontains $artifactId) {
                $State.downloaded_artifact_ids = @($State.downloaded_artifact_ids) + $artifactId
            }
            Save-State $State
            Remove-Item -LiteralPath $staging -Recurse -Force
            Write-Host "  Run $($run.databaseId): saved $ArtifactName to $Destination"
        }
    }
}

function Publish-Metadata {
    Push-Location $repoRoot
    try {
        $metadata = @(
            Get-ChildItem "papers/daily", "papers/manual", "papers/tracking" -Recurse -File -ErrorAction SilentlyContinue |
                Where-Object { $_.Name -in @("papers.csv", "summaries.md", "uncertain.md", "history.json", "daily_history.json", "manual_history.json") }
        )
        if ($metadata.Count -eq 0) {
            Write-Host "No metadata files found to commit."
            return
        }

        foreach ($file in $metadata) {
            & git add -- $file.FullName
            if ($LASTEXITCODE -ne 0) {
                throw "Failed to stage $($file.FullName)."
            }
        }

        & git diff --cached --quiet
        if ($LASTEXITCODE -eq 0) {
            Write-Host "No metadata changes to commit."
            return
        }

        & git commit -m "chore: sync paper metadata [skip ci]"
        if ($LASTEXITCODE -ne 0) {
            throw "Failed to commit paper metadata."
        }

        if ($PushMetadata) {
            Write-Host "Synchronizing remote main before pushing metadata..."
            & git pull --rebase origin main
            if ($LASTEXITCODE -ne 0) {
                throw "Metadata was committed locally, but remote changes could not be integrated. Resolve the rebase before pushing."
            }

            & git push origin main
            if ($LASTEXITCODE -ne 0) {
                throw "Metadata was committed locally, but push failed."
            }
        }
    }
    finally {
        Pop-Location
    }
}

Assert-Command "gh"
Assert-Command "git"
Initialize-GitHubAuthEnvironment

$previousErrorActionPreference = $ErrorActionPreference
$ErrorActionPreference = "SilentlyContinue"
& gh auth status *> $null
$authExitCode = $LASTEXITCODE
$ErrorActionPreference = $previousErrorActionPreference
if ($authExitCode -ne 0) {
    throw "GitHub CLI is not logged in. Set GH_TOKEN in the Windows user environment or run 'gh auth login' once before using this script."
}

New-Item -ItemType Directory -Force -Path $tempRoot | Out-Null
$state = Load-State

if (-not $SkipDaily) {
    Sync-WorkflowArtifacts `
        -WorkflowFile "main.yml" `
        -ArtifactName "daily-paper-archive" `
        -Destination (Join-Path $repoRoot "papers/daily") `
        -RunStatuses @("success", "failure") `
        -State $state
}

if (-not $SkipManual) {
    Sync-WorkflowArtifacts `
        -WorkflowFile "search-papers.yml" `
        -ArtifactName "paper-search-results" `
        -Destination (Join-Path $repoRoot "papers/manual") `
        -State $state
}


if (-not $SkipTracking) {
    Sync-WorkflowArtifacts `
        -WorkflowFile "track-researchers.yml" `
        -ArtifactName "researcher-tracking-results" `
        -Destination (Join-Path $repoRoot "papers/tracking") `
        -State $state
}
if ($CommitMetadata -or $PushMetadata) {
    Publish-Metadata
}

Write-Host "Artifact synchronization finished."
