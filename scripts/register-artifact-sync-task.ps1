param(
    [ValidateRange(15, 1440)]
    [int]$IntervalMinutes = 30,

    [switch]$PushMetadata
)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$syncScript = Join-Path $PSScriptRoot "sync-action-artifacts.ps1"
$taskName = "PaperDailyReading Artifact Sync"
$arguments = @(
    "-NoProfile",
    "-ExecutionPolicy", "Bypass",
    "-File", ('"' + $syncScript + '"'),
    "-CommitMetadata"
)
if ($PushMetadata) {
    $arguments += "-PushMetadata"
}

$action = New-ScheduledTaskAction `
    -Execute "powershell.exe" `
    -Argument ($arguments -join " ") `
    -WorkingDirectory $repoRoot
$trigger = New-ScheduledTaskTrigger `
    -Once `
    -At (Get-Date).AddMinutes(1) `
    -RepetitionInterval (New-TimeSpan -Minutes $IntervalMinutes)
$settings = New-ScheduledTaskSettingsSet `
    -MultipleInstances IgnoreNew `
    -StartWhenAvailable `
    -AllowStartIfOnBatteries

Register-ScheduledTask `
    -TaskName $taskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Description "Serially downloads PaperDailyReading GitHub Actions artifacts and syncs metadata." `
    -Force

Write-Host "Registered '$taskName' to run every $IntervalMinutes minutes."
