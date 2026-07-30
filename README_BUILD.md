# Release-Builds

## Voraussetzungen

- Python 3.10+
- Internetzugang für PyInstaller und die Abhängigkeiten
- Für DMG (macOS): `pip install dmgbuild` oder macOS mit `hdiutil`
- Für DEB (Linux): `dpkg-deb` (im Paket `dpkg` enthalten)

## Build starten

```bash
python build_release.py
```

## Ausgabe

Die gebauten Dateien landen im Ordner dist/:

- **Windows**: `dist/windows/PrankJumpAndRun.exe` (Einzelfile-EXE)
- **macOS**: `dist/macos/PrankJumpAndRun.app` (App-Bundle)
- **macOS DMG**: `dist/PrankJumpAndRun.dmg` (Disk-Image für einfache Installation)
- **Linux**: `dist/linux/PrankJumpAndRun` (Einzelfile-Binary)
- **Linux DEB**: `dist/prank-jump-and-run_1.0.0_amd64.deb` (Debian-Paket)

## Einzelne Builds ausführen

Du kannst auch nur bestimmte Builds aus dem Skript importieren und einzeln aufrufen:

```python
from build_release import build_windows_exe, build_macos_app, build_macos_dmg, build_linux_appimage, build_linux_deb

build_windows_exe()   # Nur Windows EXE
build_macos_app()     # Nur macOS .app
build_macos_dmg()     # Nur DMG (benötigt vorher .app)
build_linux_appimage() # Nur Linux Binary
build_linux_deb()     # Nur DEB (benötigt vorher Linux Binary)
```

## Speichern

Spielstände werden im Nutzer-App-Ordner gespeichert, nicht im Projektordner:

- Windows: `%APPDATA%/PrankJumpAndRun`
- macOS: `~/Library/Application Support/PrankJumpAndRun`
- Linux: `~/.local/share/prank-jump-and-run`
