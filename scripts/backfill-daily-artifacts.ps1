param(
    [string]$Repository = "zzrs123/zotero-arxiv-daily-Try",

    [ValidateRange(1, 30)]
    [int]$LookbackDays = 30,

    [ValidateRange(1, 200)]
    [int]$MaxRuns = 100,

    [long[]]$RunIds = @(),

    [ValidateRange(1, 240)]
    [int]$DownloadTimeoutMinutes = 60,

    [ValidatePattern('^\d{4}-\d{2}-\d{2}$')]
    [string]$FromDate = "",

    [ValidatePattern('^\d{4}-\d{2}-\d{2}$')]
    [string]$ToDate = "",

    [switch]$RepairEmpty,

    [switch]$ForceUpdate,

    [switch]$CommitMetadata,

    [switch]$PushMetadata
)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$destination = Join-Path $repoRoot "papers/daily"
$tempRoot = Join-Path $env:TEMP "paper-daily-backfill"

function Assert-Command {
    param([string]$Name)

    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command '$Name' was not found."
    }
}

function Invoke-GhJson {
    param([string[]]$Arguments)

    $output = & gh @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "GitHub CLI failed: gh $($Arguments -join ' ')"
    }
    return $output | ConvertFrom-Json
}

function Format-FileSize {
    param([long]$Bytes)

    if ($Bytes -ge 1GB) { return "{0:N1} GB" -f ($Bytes / 1GB) }
    if ($Bytes -ge 1MB) { return "{0:N1} MB" -f ($Bytes / 1MB) }
    if ($Bytes -ge 1KB) { return "{0:N1} KB" -f ($Bytes / 1KB) }
    return "$Bytes B"
}

function Get-CsvRowCount {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        return 0
    }
    return @((Import-Csv -LiteralPath $Path -Encoding UTF8)).Count
}

function Test-DateInRange {
    param([string]$DateText)

    if ($FromDate -and $DateText -lt $FromDate) {
        return $false
    }
    if ($ToDate -and $DateText -gt $ToDate) {
        return $false
    }
    return $true
}

function Get-DailyFolders {
    param([string]$Root)

    if (-not (Test-Path -LiteralPath $Root)) {
        return @()
    }
    return @(
        Get-ChildItem -LiteralPath $Root -Directory -Recurse |
            Where-Object {
                $hasMetadata = (
                    (Test-Path -LiteralPath (Join-Path $_.FullName "papers.csv")) -or
                    (Test-Path -LiteralPath (Join-Path $_.FullName "summaries.md"))
                )
                $_.Name -match '^\d{4}-\d{2}-\d{2}$' -and $hasMetadata -and (Test-DateInRange $_.Name)
            } |
            Sort-Object Name, FullName -Unique
    )
}

function Download-RunArtifact {
    param(
        [long]$RunId,
        [long]$ArtifactId,
        [string]$ArtifactName
    )

    $staging = Join-Path $tempRoot "$RunId-$ArtifactId"
    Remove-Item -LiteralPath $staging -Recurse -Force -ErrorAction SilentlyContinue
    New-Item -ItemType Directory -Force -Path $staging | Out-Null

    $psi = [System.Diagnostics.ProcessStartInfo]::new()
    $psi.FileName = (Get-Command gh).Source
    $psi.Arguments = "run download $RunId --repo $Repository --name $ArtifactName --dir `"$staging`""
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
        Write-Host "  Run ${RunId}: download timed out after $DownloadTimeoutMinutes min, skipping."
        return $null
    }
    if ($proc.ExitCode -ne 0) {
        Remove-Item -LiteralPath $staging -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "  Run ${RunId}: download failed (exit $($proc.ExitCode)), skipping."
        if ($stdout) { Write-Host $stdout.Trim() }
        if ($stderr) { Write-Host $stderr.Trim() }
        return $null
    }
    return $staging
}

function Publish-DailyMetadata {
    Push-Location $repoRoot
    try {
        $metadata = @(
            Get-ChildItem "papers/daily" -Recurse -File -ErrorAction SilentlyContinue |
                Where-Object { $_.Name -in @("papers.csv", "summaries.md") }
        )
        if ($metadata.Count -eq 0) {
            Write-Host "No daily metadata files found to commit."
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
            Write-Host "No daily metadata changes to commit."
            return
        }

        & git commit -m "chore: backfill daily paper metadata [skip ci]"
        if ($LASTEXITCODE -ne 0) {
            throw "Failed to commit daily metadata."
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

$previousErrorActionPreference = $ErrorActionPreference
$ErrorActionPreference = "SilentlyContinue"
& gh auth status *> $null
$authExitCode = $LASTEXITCODE
$ErrorActionPreference = $previousErrorActionPreference
if ($authExitCode -ne 0) {
    throw "GitHub CLI is not logged in. Run 'gh auth login' once before using this script."
}

New-Item -ItemType Directory -Force -Path $destination | Out-Null
New-Item -ItemType Directory -Force -Path $tempRoot | Out-Null

$runs = @()
if ($RunIds.Count -gt 0) {
    foreach ($id in $RunIds) {
        $run = Invoke-GhJson @(
            "run", "view", "$id",
            "--repo", $Repository,
            "--json", "databaseId,createdAt,event,displayTitle,conclusion"
        )
        if ($run.conclusion -ne "success") {
            Write-Host "Run ${id} is not successful (conclusion=$($run.conclusion)), skipping."
            continue
        }
        $runs += $run
    }
    $runs = @($runs | Sort-Object createdAt)
}
else {
    $cutoff = (Get-Date).ToUniversalTime().AddDays(-$LookbackDays)
    $runs = @(
        Invoke-GhJson @(
            "run", "list",
            "--repo", $Repository,
            "--workflow", "main.yml",
            "--status", "success",
            "--limit", "$MaxRuns",
            "--json", "databaseId,createdAt,event,displayTitle"
        ) |
            Where-Object { ([datetime]$_.createdAt).ToUniversalTime() -ge $cutoff } |
            Sort-Object createdAt
    )
}

if ($runs.Count -eq 0) {
    Write-Host "No successful daily runs found in the last $LookbackDays day(s)."
    exit 0
}

if ($RunIds.Count -gt 0) {
    Write-Host "Found $($runs.Count) requested successful daily run(s)."
}
else {
    Write-Host "Found $($runs.Count) successful daily run(s) in the last $LookbackDays day(s)."
}
$copied = 0
$skipped = 0

foreach ($run in $runs) {
    $artifactResponse = Invoke-GhJson @(
        "api", "repos/$Repository/actions/runs/$($run.databaseId)/artifacts"
    )
    $artifact = @($artifactResponse.artifacts | Where-Object {
        $_.name -eq "daily-paper-archive" -and -not $_.expired
    } | Select-Object -First 1)

    if ($artifact.Count -eq 0) {
        Write-Host "  Run $($run.databaseId): no active daily-paper-archive artifact, skipping."
        continue
    }

    $sizeStr = Format-FileSize $artifact[0].size_in_bytes
    Write-Host "  Run $($run.databaseId) [$($run.createdAt)]: downloading daily-paper-archive ($sizeStr)..."
    $staging = Download-RunArtifact -RunId $run.databaseId -ArtifactId $artifact[0].id -ArtifactName "daily-paper-archive"
    if (-not $staging) {
        continue
    }

    $folders = Get-DailyFolders -Root $staging
    if ($folders.Count -eq 0) {
        Write-Host "  Run $($run.databaseId): artifact has no matching daily folders."
        Remove-Item -LiteralPath $staging -Recurse -Force -ErrorAction SilentlyContinue
        continue
    }

    foreach ($folder in $folders) {
        $target = Join-Path $destination $folder.Name
        $targetCsv = Join-Path $target "papers.csv"
        $sourceCsv = Join-Path $folder.FullName "papers.csv"
        $shouldCopy = $ForceUpdate -or -not (Test-Path -LiteralPath $target)
        if (-not $shouldCopy -and $RepairEmpty) {
            $shouldCopy = (Get-CsvRowCount $targetCsv) -eq 0 -and (Get-CsvRowCount $sourceCsv) -gt 0
        }

        if ($shouldCopy) {
            Copy-Item -LiteralPath $folder.FullName -Destination $destination -Recurse -Force
            $copied += 1
            Write-Host "    restored $($folder.Name)"
        }
        else {
            $skipped += 1
            Write-Host "    $($folder.Name) already exists, skipping"
        }
    }

    Remove-Item -LiteralPath $staging -Recurse -Force -ErrorAction SilentlyContinue
}

Write-Host "Daily backfill finished. Restored $copied folder(s), skipped $skipped existing folder(s)."

if ($CommitMetadata -or $PushMetadata) {
    Publish-DailyMetadata
}
