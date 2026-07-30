import os
import shutil
import subprocess
import sys
import platform
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
BUILD = ROOT / "build"


def run(cmd, cwd=None):
    print("\n>>>", " ".join(cmd))
    subprocess.check_call(cmd, cwd=cwd or ROOT)


def clean():
    for path in [DIST, BUILD]:
        if path.exists():
            shutil.rmtree(path)
    (ROOT / "build").mkdir(exist_ok=True)


def ensure_python_packages():
    run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    run([sys.executable, "-m", "pip", "install", "-r", str(ROOT / "requirements.txt")])
    run([sys.executable, "-m", "pip", "install", "pyinstaller"])


def build_windows_exe():
    out = DIST / "windows"
    out.mkdir(parents=True, exist_ok=True)
    run([
        sys.executable, "-m", "PyInstaller",
        "--noconfirm",
        "--onefile",
        "--windowed",
        "--name", "PrankJumpAndRun",
        "--distpath", str(out),
        "--workpath", str(BUILD / "pyinstaller_windows"),
        "--add-data", f"{ROOT};.",
        "Spiel.py"
    ])


def build_macos_app():
    out = DIST / "macos"
    out.mkdir(parents=True, exist_ok=True)
    run([
        sys.executable, "-m", "PyInstaller",
        "--noconfirm",
        "--windowed",
        "--name", "PrankJumpAndRun",
        "--distpath", str(out),
        "--workpath", str(BUILD / "pyinstaller_macos"),
        "--add-data", f"{ROOT};.",
        "Spiel.py"
    ])


def build_macos_dmg():
    """Erstellt eine DMG-Datei aus der macOS .app."""
    app_path = DIST / "macos" / "PrankJumpAndRun.app"
    if not app_path.exists():
        print("macOS .App nicht gefunden. Bitte zuerst build_macos_app() ausführen.")
        return

    dmg_path = DIST / "PrankJumpAndRun.dmg"
    temp_dmg = BUILD / "temp.dmg"
    volume_name = "PrankJumpAndRun"

    # Versuche zuerst dmgbuild (pip install dmgbuild)
    try:
        import dmgbuild
        settings = {
            "volume_name": volume_name,
            "format": "UDBZ",
            "size": "200M",
            "files": [str(app_path)],
            "symlinks": {"Applications": "/Applications"},
            "icon_locations": {app_path.name: (140, 120), "Applications": (400, 120)},
        }
        dmgbuild.build_dmg(str(dmg_path), volume_name, settings)
        print(f"DMG erstellt mit dmgbuild: {dmg_path}")
        return
    except ImportError:
        print("dmgbuild nicht installiert, versuche hdiutil...")

    # Fallback: hdiutil (nur auf macOS verfügbar)
    if platform.system() != "Darwin":
        print("hdiutil nur auf macOS verfügbar. DMG kann nicht erstellt werden.")
        return

    try:
        # Erstelle ein temporäres Verzeichnis für den DMG-Inhalt
        dmg_content = BUILD / "dmg_content"
        if dmg_content.exists():
            shutil.rmtree(dmg_content)
        dmg_content.mkdir(parents=True, exist_ok=True)

        # Kopiere die .app und erstelle einen Alias für /Applications
        shutil.copytree(app_path, dmg_content / app_path.name)
        # Erstelle einen Symlink zu /Applications
        (dmg_content / "Applications").symlink_to("/Applications")

        # Erstelle die DMG
        if temp_dmg.exists():
            temp_dmg.unlink()
        run([
            "hdiutil", "create",
            "-volname", volume_name,
            "-srcfolder", str(dmg_content),
            "-ov",
            "-format", "UDZO",
            str(temp_dmg)
        ])
        # Komprimiere die DMG
        if dmg_path.exists():
            dmg_path.unlink()
        run([
            "hdiutil", "convert",
            str(temp_dmg),
            "-format", "UDZO",
            "-o", str(dmg_path)
        ])
        # Aufräumen
        if temp_dmg.exists():
            temp_dmg.unlink()
        shutil.rmtree(dmg_content)
        print(f"DMG erstellt mit hdiutil: {dmg_path}")
    except Exception as e:
        print(f"Fehler beim Erstellen der DMG: {e}")


def build_linux_appimage():
    out = DIST / "linux"
    out.mkdir(parents=True, exist_ok=True)
    run([
        sys.executable, "-m", "PyInstaller",
        "--noconfirm",
        "--onefile",
        "--windowed",
        "--name", "PrankJumpAndRun",
        "--distpath", str(out),
        "--workpath", str(BUILD / "pyinstaller_linux"),
        "--add-data", f"{ROOT}:.",
        "Spiel.py"
    ])


def build_linux_deb():
    """Erstellt ein .deb Paket aus dem Linux Binary."""
    binary = DIST / "linux" / "PrankJumpAndRun"
    if not binary.exists():
        print("Linux Binary nicht gefunden. Bitte zuerst build_linux_appimage() ausführen.")
        return

    deb_root = BUILD / "deb_package"
    if deb_root.exists():
        shutil.rmtree(deb_root)

    package_name = "prank-jump-and-run"
    version = "1.0.0"
    arch = "amd64"

    # Erstelle die DEB-Verzeichnisstruktur
    debian_dir = deb_root / "DEBIAN"
    debian_dir.mkdir(parents=True, exist_ok=True)

    # control-Datei
    control_content = f"""Package: {package_name}
Version: {version}
Section: games
Priority: optional
Architecture: {arch}
Maintainer: Leo Göttlinger <leogoettlinger@example.com>
Description: Its a Prank! Jump and Run
 A fun jump and run game with prank elements.
 Built with Python and Arcade library.
"""
    (debian_dir / "control").write_text(control_content, encoding="utf-8")

    # Installationspfad: /usr/games/
    install_dir = deb_root / "usr" / "games"
    install_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(binary, install_dir / "prank-jump-and-run")

    # Desktop-Eintrag
    desktop_dir = deb_root / "usr" / "share" / "applications"
    desktop_dir.mkdir(parents=True, exist_ok=True)
    desktop_content = """[Desktop Entry]
Type=Application
Name=Prank Jump and Run
Comment=A fun jump and run game with prank elements
Exec=/usr/games/prank-jump-and-run
Icon=prank-jump-and-run
Terminal=false
Categories=Game;
"""
    (desktop_dir / "prank-jump-and-run.desktop").write_text(desktop_content, encoding="utf-8")

    # Icon (falls vorhanden)
    icon_src = ROOT / "creeper.png"
    if icon_src.exists():
        icon_dir = deb_root / "usr" / "share" / "icons" / "hicolor" / "256x256" / "apps"
        icon_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(icon_src, icon_dir / "prank-jump-and-run.png")

    # Baue das .deb Paket
    deb_path = DIST / f"{package_name}_{version}_{arch}.deb"
    run(["dpkg-deb", "--build", str(deb_root), str(deb_path)])
    print(f"DEB Paket erstellt: {deb_path}")

    # Aufräumen
    shutil.rmtree(deb_root)


def build_all():
    clean()
    ensure_python_packages()
    build_windows_exe()
    build_macos_app()
    build_macos_dmg()
    build_linux_appimage()
    build_linux_deb()
    print("\nBuild abgeschlossen. Artefakte in", DIST)


if __name__ == "__main__":
    build_all()
