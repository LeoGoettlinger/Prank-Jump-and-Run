#!/bin/bash

echo "========================================================="
echo "   It's a Prank Jump & Run - Auto-Installer (Mac/Linux)"
echo "========================================================="

PYTHON_CMD="python3"

# 1. SYSTEM-CHECK
if [[ "$OSTYPE" == "darwin"* ]]; then
    if ! command -v brew &> /dev/null; then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    PYTHON_CMD="python3"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt-get update && sudo apt-get install -y git python3-venv python3-pip
    PYTHON_CMD="python3"
fi

# 2. REPOSITORY AUS GITHUB HOLEN / AKTUALISIEREN
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_URL="https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git"
cd "$PROJECT_DIR" || exit

if [ -d ".git" ]; then
    echo "[INFO] Repository gefunden. Aktualisiere auf die neueste Version..."
    git fetch origin main
    git reset --hard origin/main
else
    echo "[INFO] Kein lokales Repository gefunden. Klone Repository aus GitHub..."
    rm -rf "$PROJECT_DIR"/* "$PROJECT_DIR"/.git* 2>/dev/null
    git clone -b main "$REPO_URL" "$PROJECT_DIR"
fi

# 3. UMGEBUNG & INSTALLATION
$PYTHON_CMD -m venv venv
source venv/bin/activate

echo "[INFO] Update Pip & Installation..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# 4. START
python3 Spiel.py
