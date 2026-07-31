# MSI Build Fix - Task List

## Steps

- [x] Plan approved by user
- [ ] **Step 1**: Replace `build_msi.py` with fixed version (forward-slashes, debug output, AllowSameVersionUpgrades, verbose build)
- [ ] **Step 2**: Add verify step in `.github/workflows/build.yml` between "Build Windows Portable (.exe)" and "Install WiX Toolset (Windows)"
- [ ] **Step 3**: Commit both changes with message "Fix MSI embedding, add desktop shortcut and seamless upgrades"
