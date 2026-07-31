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
    
    if not os.path.exists(icon_path):
        print(f"Warning: {icon_path} not found. Using default icon.")
        icon_path = ""

    # WICHTIG: Compressed="yes" damit die .exe wirklich ins MSI gepackt wird!
    wxs_content = '''<?xml version="1.0" encoding="UTF-8"?>
<Wix xmlns="http://wixtoolset.org/schemas/v4/wxs">
    <Package Name="Prank Jump and Run"
         Manufacturer="Leo Goettlinger"
         Version="1.0.0"
         UpgradeCode="12345678-1234-1234-1234-123456789abc"
         Scope="perMachine"
         Compressed="yes">
        
        <MajorUpgrade DowngradeErrorMessage="A newer version is already installed." />
        
        {icon_section}
        
        <StandardDirectory Id="ProgramFiles6432Folder">
            <Directory Id="APPLICATIONFOLDER" Name="PrankJumpAndRun">
                <Component Id="MainExecutable" Guid="*" Bitness="always64">
                    <File Id="PrankJumpAndRunExe" Name="PrankJumpAndRun.exe" Source="{exe_source}" KeyPath="yes" />
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
                              WorkingDirectory="APPLICATIONFOLDER" {icon_attr} />
                    <RemoveFolder Id="RemoveApplicationProgramsFolder" Directory="ApplicationProgramsFolder" On="uninstall" />
                    <RegistryValue Root="HKCU" Key="Software\\PrankJumpAndRun" Name="installed" Type="integer" Value="1" KeyPath="yes" />
                </Component>
            </Directory>
        </StandardDirectory>
        
        <StandardDirectory Id="DesktopFolder">
            <Component Id="DesktopShortcut" Guid="*">
                <Shortcut Id="DesktopShortcut"
                          Name="Prank Jump and Run"
                          Description="Its a Prank! Jump and Run"
                          Target="[APPLICATIONFOLDER]PrankJumpAndRun.exe"
                          WorkingDirectory="APPLICATIONFOLDER" {icon_attr} />
                <RemoveFolder Id="RemoveDesktopFolder" Directory="DesktopFolder" On="uninstall" />
                <RegistryValue Root="HKCU" Key="Software\\PrankJumpAndRun" Name="desktop_shortcut" Type="integer" Value="1" KeyPath="yes" />
            </Component>
        </StandardDirectory>
        
        <Feature Id="MainFeature" Title="Prank Jump and Run" Level="1">
            <ComponentRef Id="MainExecutable" />
            <ComponentRef Id="StartMenuShortcut" />
            <ComponentRef Id="DesktopShortcut" />
        </Feature>
    </Package>
</Wix>'''.format(
        exe_source=exe_path,
        icon_section=f'<Icon Id="app.ico" SourceFile="{icon_path}" /><Property Id="ARPPRODUCTICON" Value="app.ico" />' if icon_path else '',
        icon_attr='Icon="app.ico"' if icon_path else ''
    )

    wxs_path = "installer.wxs"
    with open(wxs_path, "w", encoding="utf-8") as f:
        f.write(wxs_content)
    print("Created: installer.wxs")

    # Build .msi with WiX v4
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
