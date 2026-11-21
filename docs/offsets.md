# Offsets & signatures

Offsets are versioned per game build under `data/offsets/<build>.json`.
`fallback.json` is used when a build is unknown — most offsets will be
zero, meaning that feature silently no-ops until a PR adds the build.

Signatures live in `data/sigs.sqlite` (git-ignored) and are populated by
`python -m modmenu.sigupdate` after each patch. The pattern scanner reads
from this DB at attach time.

**Do not** commit dumps of `GenshinImpact.exe` to this repo.