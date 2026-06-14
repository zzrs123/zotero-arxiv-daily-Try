param(
    [string]$Keywords = "",

    [ValidateSet('default', 'all', 'any')]
    [string]$MatchMode = 'default',

    [string]$Journals = "",

    [Parameter(Mandatory = $true)]
    [ValidatePattern('^\d{4}-\d{2}-\d{2}$')]
    [string]$FromDate,

    [ValidatePattern('^\d{4}-\d{2}-\d{2}$')]
    [string]$ToDate = (Get-Date -Format 'yyyy-MM-dd'),

    [ValidateRange(1, 100)]
    [int]$MaxResults = 30,

    [switch]$SkipSummary,

    [switch]$SkipPdfDownload
)

$arguments = @(
    'run', 'python', '-m', 'zotero_arxiv_daily.openalex_search',
    '--keywords', $Keywords,
    '--match-mode', $MatchMode,
    '--journals', $Journals,
    '--from-date', $FromDate,
    '--to-date', $ToDate,
    '--max-results', $MaxResults,
    '--output-dir', 'papers/manual'
)

if (-not $SkipSummary) {
    $arguments += '--summarize'
}

if ($SkipPdfDownload) {
    $arguments += '--skip-pdf-download'
}

& py -3.12 -m uv @arguments
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
