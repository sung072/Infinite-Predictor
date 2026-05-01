# CI 와 동일 → scripts/run_ci.py 호출. 옵션 그대로 전달 예:
#   pwsh -File scripts/run_ci_local.ps1
#   pwsh -File scripts/run_ci_local.ps1 --skip-pip --no-jsonl -q
$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $Root
& python (Join-Path $Root "scripts\run_ci.py") @args
exit $LASTEXITCODE
