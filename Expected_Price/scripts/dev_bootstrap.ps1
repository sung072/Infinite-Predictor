# 의존성 설치 + 빠른 CI(테스트)까지 한 번에. 사용 예:
#   pwsh -File scripts/dev_bootstrap.ps1
#   pwsh -File scripts/dev_bootstrap.ps1 -CreateVenv   # 프로젝트 루트에 .venv 생성·사용
param(
    [switch] $CreateVenv
)
$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $Root

$py = "python"
if ($CreateVenv) {
    $venvPath = Join-Path $Root ".venv"
    if (-not (Test-Path $venvPath)) {
        & $py -m venv $venvPath
    }
    $pyExe = Join-Path $venvPath "Scripts\python.exe"
    if (-not (Test-Path $pyExe)) { throw "venv not created: $venvPath" }
    $py = $pyExe
}

& $py -c "import sys; assert sys.version_info >= (3, 11), 'Python 3.11+ required'; print('python', sys.version.split()[0])"
& $py -m pip install -U pip wheel
& $py -m pip install -r requirements-research.txt
$devReq = Join-Path $Root "requirements-dev.txt"
if (Test-Path $devReq) {
  & $py -m pip install -r $devReq
}
& $py scripts\run_ci.py --skip-pip --no-jsonl -q
$code = $LASTEXITCODE
if ($code -eq 0) {
  Write-Host "OK. Next: full CI  ->  python scripts\run_ci.py  or  make ci  (Korean: docs\QUICKSTART.md)"
}
exit $code
