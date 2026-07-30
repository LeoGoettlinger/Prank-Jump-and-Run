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

# 2. REPOSITORY KLONEN
if [ ! -d "Prank-Jump-and-Run/.git" ]; then
    rm -rf Prank-Jump-and-Run
    git clone -b main https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git
else
    cd Prank-Jump-and-Run && git pull origin main && cd ..
fi

cd Prank-Jump-and-Run || exit

# 3. UMGEBUNG & INSTALLATION
$PYTHON_CMD -m venv venv
source venv/bin/activate

echo "[INFO] Update Pip & Installation..."
python3 -m pip install --upgrade pip
python3 -m pip install "arcade>=3.0.0" "pyglet>=2.0.0" "pyyaml>=6.0.0" "cryptography>=41.0.0"

# 4. START
python3 Spiel.py
