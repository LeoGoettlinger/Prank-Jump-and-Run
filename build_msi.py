#!/usr/bin/env python3
"""
Builds a .msi installer for Windows using WiX Toolset v4.
Creates desktop shortcuts and supports seamless upgrades.
"""
import os
import subprocess
import sys


def main():
    exe_path = os.path.abspath("dist/PrankJumpAndRun.exe")
    icon_path = os.path.abspath("creeper.ico")

    print(f"=== MSI BUILD DEBUG ===")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Looking for exe at: {exe_path}")
    print(f"Looking for icon at: {icon_path}")
    print(f"Contents of dist/: {os.listdir('dist') if os.path.exists('dist') else 'dist/ does not exist!'}")
    print(f"=======================")

    if not os.path.exists(exe_path):
        print(f"FATAL ERROR: {exe_path} not found!")
        sys.exit(1)

    exe_size_mb = os.path.getsize(exe_path) / (1024 * 1024)
    print(f"Found exe: {exe_size_mb:.1f} MB")

    has_icon = os.path.exists(icon_path)
    
    # Use forward slashes for WiX compatibility
    exe_path_wix = exe_path.replace("\\", "/")
    icon_path_wix = icon_path.replace("\\", "/") if has_icon else ""

    icon_section = f'<Icon Id="app.ico" SourceFile="{icon_path_wix}" /><Property Id="ARPPRODUCTICON" Value="app.ico" />' if has_icon else ''
    icon_attr = 'Icon="app.ico"' if has_icon else ''

    wxs_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
    <Package Name="Prank Jump and Run"
             Manufacturer="Leo Goettlinger"
             Version="1.0.0"
             UpgradeCode="12345678-1234-1234-1234-123456789abc"
             Scope="perMachine"
             Compressed="yes">

        <MajorUpgrade DowngradeErrorMessage="A newer version is already installed."
                      AllowSameVersionUpgrades="yes" />

        {icon_section}

        <StandardDirectory Id="ProgramFiles6432Folder">
            <Directory Id="APPLICATIONFOLDER" Name="PrankJumpAndRun">
                <Component Id="MainExecutable" Guid="*" Bitness="always64">
                    <File Id="PrankJumpAndRunExe"
                          Name="PrankJumpAndRun.exe"
                          Source="{exe_path_wix}"
                          KeyPath="yes" />
                </Component>
            </Directory>
        </StandardDirectory>

        <StandardDirectory Id="ProgramMenuFolder">
            <Directory Id="ApplicationProgramsFolder" Name="Prank Jump and Run">
                <Component Id="StartMenuShortcut" Guid="*">
                    <Shortcut Id="StartMenuShortcut"
                              Name="Prank Jump and Run"
                              Description="Its a Prank! Jump and Run"
                              Target="[APPLICATIONFOLDER]PrankJumpAndRun.exe"
                              WorkingDirectory="APPLICATIONFOLDER"
                              {icon_attr} />
                    <RemoveFolder Id="RemoveApplicationProgramsFolder"
                                  Directory="ApplicationProgramsFolder"
                                  On="uninstall" />
                    <RegistryValue Root="HKCU"
                                   Key="Software\\PrankJumpAndRun"
                                   Name="installed"
                                   Type="integer"
                                   Value="1"
                                   KeyPath="yes" />
                </Component>
            </Directory>
        </StandardDirectory>

        <StandardDirectory Id="DesktopFolder">
            <Component Id="DesktopShortcut" Guid="*">
                <Shortcut Id="DesktopShortcut"
                          Name="Prank Jump and Run"
                          Description="Its a Prank! Jump and Run"
                          Target="[APPLICATIONFOLDER]PrankJumpAndRun.exe"
                          WorkingDirectory="APPLICATIONFOLDER"
                          {icon_attr} />
                <RemoveFolder Id="RemoveDesktopFolder"
                              Directory="DesktopFolder"
                              On="uninstall" />
                <RegistryValue Root="HKCU"
                               Key="Software\\PrankJumpAndRun"
                               Name="desktop_shortcut"
                               Type="integer"
                               Value="1"
                               KeyPath="yes" />
            </Component>
        </StandardDirectory>

        <Feature Id="MainFeature" Title="Prank Jump and Run" Level="1">
            <ComponentRef Id="MainExecutable" />
            <ComponentRef Id="StartMenuShortcut" />
            <ComponentRef Id="DesktopShortcut" />
        </Feature>
    </Package>
</Wix>'''

    wxs_path = "installer.wxs"
    with open(wxs_path, "w", encoding="utf-8") as f:
        f.write(wxs_content)
    print("Created: installer.wxs")

    msi_path = os.path.abspath("dist/PrankJumpAndRun.msi")
    result = subprocess.run(
        ["wix", "build", wxs_path, "-o", msi_path, "-arch", "x64", "-v"],
        capture_output=True,
        text=True,
    )

    if result.stdout:
        print(f"WiX STDOUT:\n{result.stdout}")
    if result.stderr:
        print(f"WiX STDERR:\n{result.stderr}")

    if result.returncode != 0:
        print(f"WiX build FAILED with exit code {result.returncode}")
        sys.exit(1)

    size_mb = os.path.getsize(msi_path) / (1024 * 1024)
    print(f"Done: .msi installer created at {msi_path} ({size_mb:.1f} MB)")

    if size_mb < 50:
        print(f"ERROR: MSI is only {size_mb:.1f} MB but should be ~104 MB.")
        sys.exit(1)


if __name__ == "__main__":
    main()