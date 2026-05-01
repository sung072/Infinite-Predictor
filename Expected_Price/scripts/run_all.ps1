# 한 번에: pip(연구+dev) -> CI 전체(test + JSONL) -> (Git 있으면) pre-commit
#   pwsh -File scripts\run_all.ps1
$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $Root
$py = "python"
& $py -m pip install -U pip wheel
& $py -m pip install -r requirements-research.txt
if (Test-Path "requirements-dev.txt") {
  & $py -m pip install -r requirements-dev.txt
}
& $py scripts\run_ci.py --skip-pip
$code = $LASTEXITCODE
if ($code -ne 0) { exit $code }
& $py scripts\verify_expected_price_stack.py --skip-unittest
$code = $LASTEXITCODE
if ($code -ne 0) { exit $code }
if (Test-Path ".git" -PathType Container) {
  pre-commit run --all-files
  $code = $LASTEXITCODE
} else {
  Write-Host "== pre-commit skipped: no .git (normal if you are not using Git)"
}
exit $code
