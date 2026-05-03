#!/bin/bash

echo "Starte It's a Prank Jump & Run..."

if [ ! -f "venv/bin/activate" ]; then
    echo "[FEHLER] Das Setup wurde noch nicht ausgeführt! Bitte starte zuerst ./setup.sh."
    exit 1
fi

source venv/bin/activate
cd Prank-Jump-and-Run || exit
python3 Spiel.py