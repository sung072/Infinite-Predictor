# 시작하기 (로컬)

**요구:** Python **3.11+** (`.python-version` 참고; CI는 3.11)

## 1) 한 방에 (권장)

- **Windows (PowerShell):** `pwsh -File scripts\dev_bootstrap.ps1`  
  가상환경을 쓰려면: `pwsh -File scripts\dev_bootstrap.ps1 -CreateVenv`
- **Linux / macOS:** `chmod +x scripts/dev_bootstrap.sh && ./scripts/dev_bootstrap.sh`  
  가상환경: `./scripts/dev_bootstrap.sh --venv`

→ `pip install` 후 **빠른 CI**(unittest + JSONL 제외)까지 돌리고, 성공이면 환경은 준비된 것과 같다.

## 2) “한 번에” (의존성 + 전체 CI + pre-commit*)

\* pre-commit 은 **Git 저장소 루트**에 `.git`이 있을 때만 실행.

- **Windows:** `pwsh -File scripts\run_all.ps1`
- **Linux / macOS:** `chmod +x scripts/run_all.sh && ./scripts/run_all.sh` 또는 `make all`

(`run_ci`를 중복 `pip` 없이 이어가려면 `requirements-*` 먼저 설치한 뒤 `run_ci --skip-pip` — 위 스크립트가 이 순서)

## 3) GitHub CI 와 완전히 동일하게

프로젝트 루트(`requirements-research.txt` 보이는 폴더)에서:

```bash
python scripts/run_ci.py
```

또는 `make ci` / `.\scripts\run_ci_local.ps1` (인자는 그대로 `run_ci.py`에 전달).

**반복용(빠름):** `make ci-fast` = `--skip-pip --no-jsonl`  
(로컬 래퍼: `run_ci_local`에 `--skip-pip --no-jsonl -q` 등)

## 4) 샘 Registry gap 한 번 돌리기

```bash
python code/run_registry_research.py
```

(기본 Registry: `schemas/predictor_registry.example.json`, 합성 OHLCV)

## 5) 선택

- **pre-commit (권장, 로컬):** `pip install -r requirements-dev.txt` 후 `pre-commit install` — 커밋 시 `.pre-commit-config.yaml`의 빠른 `run_ci` 훅. (`dev_bootstrap`이 `requirements-dev.txt`가 있으면 같이 설치)
- **Nautilus 등 실행 스택:** `requirements-execution.txt` — 연구 `requirements-research.txt`와 분리

설계·경계는 `chat/README.md` 를 본다.
