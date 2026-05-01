# BTC 갭 연구 Streamlit 대시보드 (프로젝트 루트 = 이 스크립트의 상위)
$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root
if (-not (Get-Command streamlit -ErrorAction SilentlyContinue)) {
    Write-Host "Install: pip install -r requirements-streamlit.txt" -ForegroundColor Yellow
    exit 1
}
$uf = Join-Path $root "data\derived\btc_factors_unified.csv"
if (-not (Test-Path $uf)) {
    Write-Host "Building unified factors: scripts\build_btc_unified_factor_csv.py" -ForegroundColor Cyan
    & python (Join-Path $root "scripts\build_btc_unified_factor_csv.py")
}
Write-Host "Streamlit: http://127.0.0.1:7520 (port 7000-7999, .streamlit/config.toml). Override: -- --server.port 7530" -ForegroundColor Green
# 프로젝트 루트의 .streamlit/config.toml 이 기본 포트(7520)를 씀
& streamlit run (Join-Path $root "dashboard\btc_research_app.py") @args
