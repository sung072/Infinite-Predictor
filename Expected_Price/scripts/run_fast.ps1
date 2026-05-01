# Fast local check: unittest only (no pip, no JSONL smoke). Same as: make ci-fast
#   pwsh -File scripts\run_fast.ps1
#   pwsh -File scripts\run_fast.ps1 -- -q
$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $Root
& python (Join-Path $Root "scripts\run_ci.py") --skip-pip --no-jsonl @args
exit $LASTEXITCODE
