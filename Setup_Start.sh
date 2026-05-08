#!/bin/bash

echo "========================================================="
echo "   It's a Prank Jump & Run - Auto-Installer (Mac/Linux)"
echo "========================================================="
echo ""

PYTHON_CMD="python3"

# 1. SYSTEM-ABHÄNGIGKEITEN INSTALLIEREN (OS ERKENNUNG)
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS SETUP
    if ! command -v brew &> /dev/null; then
        echo "[INFO] Homebrew (Paketmanager für Mac) fehlt. Wird installiert..."
        echo "[HINWEIS] Möglicherweise wirst du nach deinem Mac-Passwort gefragt!"
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        # Füge Brew zum Pfad hinzu (für Apple Silicon & Intel)
        eval "$(/opt/homebrew/bin/brew shellenv 2>/dev/null)"
        eval "$(/usr/local/bin/brew shellenv 2>/dev/null)"
    fi
    if ! command -v git &> /dev/null; then
        echo "[INFO] Installiere Git..."
        brew install git
    fi
    if ! command -v python3.12 &> /dev/null; then
        echo "[INFO] Installiere Python 3.12..."
        brew install python@3.12
    fi
    PYTHON_CMD="python3.12"

elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # LINUX SETUP (Debian/Ubuntu-basiert)
    if ! command -v git &> /dev/null || ! command -v python3 &> /dev/null || ! command -v python3-venv &> /dev/null; then
        echo "[INFO] Fehlende System-Tools werden installiert..."
        echo "[HINWEIS] Bitte gib dein Linux-Passwort ein:"
        sudo apt-get update
        sudo apt-get install -y git python3.12 python3.12-venv python3-pip
    fi
    PYTHON_CMD="python3"
fi

# 2. REPOSITORY KLONEN
if [ ! -d "Prank-Jump-and-Run" ]; then
    echo "[INFO] Lade Spiel-Dateien von GitHub herunter..."
    git clone -b main https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git
else
    echo "[INFO] Spiel-Dateien existieren bereits. Suche nach Updates..."
    cd Prank-Jump-and-Run || exit
    git pull origin main
    cd ..
fi

cd Prank-Jump-and-Run || exit

# 3. VIRTUELLE UMGEBUNG & SPIEL-ABHÄNGIGKEITEN INSTALLIEREN
echo "[INFO] Richte geschützte Python-Umgebung ein..."
$PYTHON_CMD -m venv venv
source venv/bin/activate

echo "[INFO] Installiere Arcade und Pyglet..."
$PYTHON_CMD -m pip install --upgrade pip -q
pip install arcade==3.3.2 pyglet==2.0.17 -q

# 4. SPIEL STARTEN
echo ""
echo "========================================================="
echo "Alles erfolgreich geladen! Das Spiel startet jetzt..."
echo "========================================================="
$PYTHON_CMD Spiel.py
