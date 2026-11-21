# Architecture

`genshin-modmenu` is split into three layers:

1. **ModMenu.App** — thin CLI bootstrap (`main.py`). Parses args, loads
   config, attaches to the game process, and either runs headless or hands
   off to the overlay host.
2. **ModMenu.Core** — the actual menu logic:
   - `loader.py` — process attach + build detection
   - `memory/pattern_scanner.py` — AOB signature scanning
   - `features/` — one module per feature (esp, aimbot, player_state)
   - `overlay_host.py` — spawns the C# overlay process
3. **ModMenu.Infrastructure** — data-plane helpers: per-build offsets
   (`offsets_loader.py`) and the signature cache (`signature_db.py`).

The C# `ModMenu.Overlay.Host` project renders the ImGui menu over a DX11
swapchain and reads the `INSERT` keybind to toggle.

## Adding a feature

1. Create `src/ModMenu.Core/features/<name>.py` with an `enable/toggle/update` trio.
2. Register it in `features/registry.py`.
3. Add a config flag under `features:` in `config/default.yaml`.