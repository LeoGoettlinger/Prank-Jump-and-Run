#!/bin/bash

echo "===================================================="
echo "     It's a Prank Jump & Run - Setup (Mac/Linux)    "
echo "===================================================="
echo ""

# Prüfen, ob Python3 installiert ist
if ! command -v python3 &> /dev/null; then
    echo "[FEHLER] Python3 ist nicht installiert!"
    echo "Bitte installiere Python 3.12.2 für dein Betriebssystem."
    exit 1
fi

# Prüfen, ob Git installiert ist
if ! command -v git &> /dev/null; then
    echo "[FEHLER] Git ist nicht installiert!"
    echo "Bitte installiere Git."
    exit 1
fi

echo "[1/4] Klone das GitHub Repository (Branch: main)..."
if [ ! -d "Prank-Jump-and-Run" ]; then
    git clone -b main https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git
else
    echo "Ordner existiert bereits. Ziehe neueste Updates..."
    cd Prank-Jump-and-Run || exit
    git pull origin main
    cd ..
fi

echo "[2/4] Erstelle eine lokale virtuelle Python-Umgebung..."
python3 -m venv venv

echo "[3/4] Aktiviere die Umgebung und update pip..."
source venv/bin/activate
python3 -m pip install --upgrade pip

echo "[4/4] Installiere Arcade 3.3.2 und Pyglet 2.0.17..."
pip install arcade==3.3.2 pyglet==2.0.17

echo ""
echo "===================================================="
echo "Setup erfolgreich abgeschlossen!"
echo "Du kannst das Spiel nun mit ./start.sh starten."
echo "===================================================="