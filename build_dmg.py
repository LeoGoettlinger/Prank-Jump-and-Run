#!/usr/bin/env python3
"""
Builds a .dmg disk image for macOS.
Called from .github/workflows/build.yml on the macOS runner.
"""

import os
import shutil
import subprocess
import sys


def main():
    app_path = os.path.abspath("dist/PrankJumpAndRun.app")
    if not os.path.exists(app_path):
        print(f"Error: {app_path} not found. Build .app first.")
        sys.exit(1)

    dmg_path = os.path.abspath("dist/PrankJumpAndRun.dmg")
    volume_name = "PrankJumpAndRun"
    temp_dmg = os.path.abspath("build/temp.dmg")
    dmg_content = os.path.abspath("build/dmg_content")

    # Clean
    if os.path.exists(dmg_content):
        shutil.rmtree(dmg_content)
    os.makedirs(dmg_content, exist_ok=True)

    # Copy .app
    shutil.copytree(app_path, os.path.join(dmg_content, "PrankJumpAndRun.app"))

    # Create Applications symlink
    os.symlink("/Applications", os.path.join(dmg_content, "Applications"))

    # Create temp DMG
    if os.path.exists(temp_dmg):
        os.remove(temp_dmg)

    result = subprocess.run(
        [
            "hdiutil", "create",
            "-volname", volume_name,
            "-srcfolder", dmg_content,
            "-ov",
            "-format", "UDZO",
            temp_dmg,
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"hdiutil create failed: {result.stderr}")
        sys.exit(1)

    # Convert to compressed DMG
    if os.path.exists(dmg_path):
        os.remove(dmg_path)

    result = subprocess.run(
        [
            "hdiutil", "convert",
            temp_dmg,
            "-format", "UDZO",
            "-o", dmg_path,
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"hdiutil convert failed: {result.stderr}")
        sys.exit(1)

    # Cleanup
    if os.path.exists(temp_dmg):
        os.remove(temp_dmg)
    if os.path.exists(dmg_content):
        shutil.rmtree(dmg_content)

    print(f"Done: .dmg created at {dmg_path}")


if __name__ == "__main__":
    main()
