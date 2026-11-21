# Security Policy

## Supported versions

Only the latest tagged release of `genshin-modmenu` receives fixes.

## Reporting a vulnerability

This is a hobbyist modding tool. If you find a vulnerability in the
**loader / injector** path (e.g. arbitrary DLL sideload from a writable
directory, unsafe `ctypes` call, or a pattern scanner that can be coerced into
writing outside the target module) open a private security advisory on GitHub
rather than a public issue.

Please include:

- Windows version and game build
- The exact CLI invocation
- A minimal repro (script or steps)

## Out of scope

- Detection by the game's anti-cheat (that's the point of the tool).
- Account bans from using the modmenu. Use at your own risk.
- Issues that only reproduce with third-party DLLs you injected yourself.