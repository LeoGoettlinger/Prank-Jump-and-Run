#!/usr/bin/env python3
"""
Builds a .msi installer for Windows using WiX Toolset.
Called from .github/workflows/build.yml on the Windows runner.
"""

import os
import subprocess
import sys


def main():
    exe_path = os.path.abspath("dist/PrankJumpAndRun.exe")
    icon_path = os.path.abspath("creeper.ico")

    if not os.path.exists(exe_path):
        print(f"Error: {exe_path} not found. Build .exe first.")
        sys.exit(1)

    wxs_content = '''<?xml version="1.0" encoding="UTF-8"?>
<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
  <Package Name="Prank Jump and Run"
           Manufacturer="Leo Goettlinger"
           Version="1.0.0"
           UpgradeCode="12345678-1234-1234-1234-123456789abc"
           Scope="perMachine">

    <MajorUpgrade DowngradeErrorMessage="A newer version is already installed." />

    <Icon Id="app.ico" SourceFile="''' + icon_path + '''" />
    <Property Id="ARPPRODUCTICON" Value="app.ico" />

    <Directory Id="TARGETDIR" Name="SourceDir">
      <Directory Id="ProgramFiles64Folder">
        <Directory Id="APPLICATIONFOLDER" Name="PrankJumpAndRun">
          <Component Id="MainExecutable" Guid="*" Bitness="always64">
            <File Id="PrankJumpAndRunExe" Name="PrankJumpAndRun.exe" Source="''' + exe_path + '''" KeyPath="yes" />
          </Component>
        </Directory>
      </Directory>
      <Directory Id="ProgramMenuFolder">
        <Directory Id="ApplicationProgramsFolder" Name="Prank Jump and Run">
          <Component Id="StartMenuShortcut" Guid="*">
            <Shortcut Id="StartMenuShortcut"
                      Name="Prank Jump and Run"
                      Description="Its a Prank! Jump and Run"
                      Target="[#PrankJumpAndRunExe]"
                      WorkingDirectory="APPLICATIONFOLDER" />
            <RemoveFolder Id="RemoveApplicationProgramsFolder" Directory="ApplicationProgramsFolder" On="uninstall" />
            <RegistryValue Root="HKCU" Key="Software\\PrankJumpAndRun" Name="installed" Type="integer" Value="1" KeyPath="yes" />
          </Component>
        </Directory>
      </Directory>
      <Directory Id="DesktopFolder">
        <Component Id="DesktopShortcut" Guid="*">
          <Shortcut Id="DesktopShortcut"
                    Name="Prank Jump and Run"
                    Description="Its a Prank! Jump and Run"
                    Target="[#PrankJumpAndRunExe]"
                    WorkingDirectory="APPLICATIONFOLDER" />
          <RemoveFolder Id="RemoveDesktopFolder" Directory="DesktopFolder" On="uninstall" />
          <RegistryValue Root="HKCU" Key="Software\\PrankJumpAndRun" Name="desktop_shortcut" Type="integer" Value="1" KeyPath="yes" />
        </Component>
      </Directory>
    </Directory>

    <Feature Id="MainFeature" Title="Prank Jump and Run" Level="1">
      <ComponentRef Id="MainExecutable" />
      <ComponentRef Id="StartMenuShortcut" />
      <ComponentRef Id="DesktopShortcut" />
    </Feature>
  </Package>
</Wix>'''

    wxs_path = "installer.wxs"
    with open(wxs_path, "w") as f:
        f.write(wxs_content)
    print("Created: installer.wxs")

    # Build .msi with WiX
    msi_path = os.path.abspath("dist/PrankJumpAndRun.msi")
    result = subprocess.run(
        ["wix", "build", wxs_path, "-o", msi_path, "-arch", "x64"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"WiX build failed: {result.stderr}")
        sys.exit(1)

    print(f"Done: .msi installer created at {msi_path}")


if __name__ == "__main__":
    main()
