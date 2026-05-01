# P0 TODO 자동 완료: 검증 실행 + docs/todo_state.json + TODO.md 체크박스(자동 항목만)
#   pwsh -File scripts\complete_todo.ps1
#   pwsh -File scripts\complete_todo.ps1 -- --full
#   pwsh -File scripts\complete_todo.ps1 -- --dry-run
$ErrorActionPreference = "Stop"
$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $Root
& python (Join-Path $Root "scripts\complete_todo.py") @args
exit $LASTEXITCODE
