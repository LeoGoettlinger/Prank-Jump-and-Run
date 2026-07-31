#!/usr/bin/env python3
"""
Builds an AppImage for Linux.
Called from .github/workflows/build.yml on the Linux runner.
"""

import os
import shutil
import subprocess
import sys


def main():
    binary = os.path.abspath("dist/PrankJumpAndRun")
    if not os.path.exists(binary):
        print(f"Error: {binary} not found. Build binary first.")
        sys.exit(1)

    # Download appimagetool if not present
    appimagetool = os.path.abspath("build/appimagetool")
    if not os.path.exists(appimagetool):
        os.makedirs("build", exist_ok=True)
        url = "https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage"
        result = subprocess.run(
            ["wget", "-q", url, "-O", appimagetool],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            print(f"Failed to download appimagetool: {result.stderr}")
            sys.exit(1)
        os.chmod(appimagetool, 0o755)

    # Create AppDir structure
    appdir = os.path.abspath("build/PrankJumpAndRun.AppDir")
    if os.path.exists(appdir):
        shutil.rmtree(appdir)

    os.makedirs(os.path.join(appdir, "usr", "bin"))
    os.makedirs(os.path.join(appdir, "usr", "share", "applications"))
    os.makedirs(os.path.join(appdir, "usr", "share", "icons", "hicolor", "256x256", "apps"))

    # Copy binary
    shutil.copy2(binary, os.path.join(appdir, "usr", "bin", "prank-jump-and-run"))

    # Copy icon
    if os.path.exists("creeper.png"):
        shutil.copy2("creeper.png", os.path.join(appdir, "usr", "share", "icons", "hicolor", "256x256", "apps", "prank-jump-and-run.png"))

    # Create .desktop file
    desktop_content = """[Desktop Entry]
Type=Application
Name=Prank Jump and Run
Comment=Its a Prank! Jump and Run - A fun jump and run game
Exec=prank-jump-and-run
Icon=prank-jump-and-run
Terminal=false
Categories=Game;
"""
    desktop_path = os.path.join(appdir, "usr", "share", "applications", "prank-jump-and-run.desktop")
    with open(desktop_path, "w") as f:
        f.write(desktop_content)

    # Create AppRun script
    apprun_content = """#!/bin/bash
HERE="$(dirname "$(readlink -f "${0}")")"
export PATH="${HERE}/usr/bin:${PATH}"
export LD_LIBRARY_PATH="${HERE}/usr/lib:${LD_LIBRARY_PATH}"
exec "${HERE}/usr/bin/prank-jump-and-run" "$@"
"""
    apprun_path = os.path.join(appdir, "AppRun")
    with open(apprun_path, "w") as f:
        f.write(apprun_content)
    os.chmod(apprun_path, 0o755)

    # Symlink .desktop and icon to top-level AppDir
    os.symlink("usr/share/applications/prank-jump-and-run.desktop", os.path.join(appdir, "prank-jump-and-run.desktop"))
    os.symlink("usr/share/icons/hicolor/256x256/apps/prank-jump-and-run.png", os.path.join(appdir, "prank-jump-and-run.png"))

    # Build AppImage
    appimage_path = os.path.abspath("dist/PrankJumpAndRun-x86_64.AppImage")
    result = subprocess.run(
        [appimagetool, appdir, appimage_path],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"appimagetool failed: {result.stderr}")
        sys.exit(1)

    # Cleanup
    shutil.rmtree(appdir)

    print(f"Done: AppImage created at {appimage_path}")


if __name__ == "__main__":
    main()
