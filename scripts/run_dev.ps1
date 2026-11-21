# Dev boot: venv + attach to running game with overlay.
$ErrorActionPreference = "Stop"
if (-not (Test-Path .venv)) { py -3.12 -m venv .venv }
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt -q
python -m src.ModMenu.App.main --config config/default.yaml