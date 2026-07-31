#!/usr/bin/env python3
"""
Builds a .deb package for Prank Jump and Run.
Called from .github/workflows/build.yml on the Linux runner.
"""
import os
import shutil
import subprocess
import sys

def main():
    binary = "./dist/PrankJumpAndRun"
    if not os.path.exists(binary):
        print(f"Binary not found at {binary}")
        sys.exit(1)

    deb_root = "./build/deb_package"
    
    # Clean and create structure
    if os.path.exists(deb_root):
        shutil.rmtree(deb_root)
    os.makedirs(os.path.join(deb_root, "DEBIAN"))
    os.makedirs(os.path.join(deb_root, "usr", "games"))
    os.makedirs(os.path.join(deb_root, "usr", "share", "applications"))
    os.makedirs(os.path.join(deb_root, "usr", "share", "icons", "hicolor", "256x256", "apps"))

    # Copy binary
    shutil.copy2(binary, os.path.join(deb_root, "usr", "games", "prank-jump-and-run"))

    # Copy icon
    if os.path.exists("creeper.png"):
        shutil.copy2("creeper.png", os.path.join(deb_root, "usr", "share", "icons", "hicolor", "256x256", "apps", "prank-jump-and-run.png"))
    else:
        print("Warning: creeper.png not found, skipping icon")

    # Create .desktop file
    desktop_content = """[Desktop Entry]
Type=Application
Name=Prank Jump and Run
Comment=Its a Prank! Jump and Run - A fun jump and run game
Exec=/usr/games/prank-jump-and-run
Icon=prank-jump-and-run
Terminal=false
Categories=Game;
"""
    desktop_path = os.path.join(deb_root, "usr", "share", "applications", "prank-jump-and-run.desktop")
    with open(desktop_path, "w") as f:
        f.write(desktop_content)

    # Create control file
    control_content = """Package: prank-jump-and-run
Version: 1.0.0
Section: games
Priority: optional
Architecture: amd64
Maintainer: Leo Goettlinger <leogoettlinger@users.noreply.github.com>
Description: Its a Prank! Jump and Run
 A fun jump and run game with prank elements.
 Built with Python and the Arcade library.
Homepage: https://github.com/LeoGoettlinger/Prank-Jump-and-Run
"""
    control_path = os.path.join(deb_root, "DEBIAN", "control")
    with open(control_path, "w") as f:
        f.write(control_content)

    # Build .deb package
    deb_file = "./dist/PrankJumpAndRun-Linux.deb"
    result = subprocess.run(
        ["dpkg-deb", "--build", deb_root, deb_file],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"dpkg-deb failed: {result.stderr}")
        sys.exit(1)

    print(f"Done: .deb package created at {deb_file}")

    # Cleanup: remove ONLY temp dir, KEEP binary for AppImage!
    shutil.rmtree(deb_root)

if __name__ == "__main__":
    main()