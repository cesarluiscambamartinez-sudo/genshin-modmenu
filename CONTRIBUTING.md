# Contributing to genshin-modmenu

Thanks for wanting to help out. This repo is a hobbyist modmenu / overlay toolkit
for Genshin Impact, written in Python (with a small C# bridge for the
DX11 overlay host). Keep contributions focused, tested on a clean Windows 10/11
install, and documented.

## Ground rules

- **Educational / research use only.** Do not open PRs that add anti-cheat
  bypass chains, HWID spoofers pointed at live services, or anything that
  targets other players.
- One feature per PR. Feature modules live under
  `src/ModMenu.Core/features/`.
- Match the existing style: type hints, `dataclasses` for state, no bare
  `except:` blocks.
- Add a test under `tests/` for anything touching memory offsets, the
  pattern scanner, or the config loader.

## Local setup

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
python -m pytest tests/
```

## Commit messages

Use `feat:`, `fix:`, `chore:`, `docs:` prefixes. Reference the feature module
name (e.g. `feat(esp): add bone-box toggle`).

## Reporting issues

Attach the output of `python -m modmenu --diagnostics` and the game build
number. Do **not** attach memory dumps of the game process.