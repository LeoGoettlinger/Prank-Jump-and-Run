@echo off
echo Starte It's a Prank Jump & Run...

IF NOT EXIST "venv\Scripts\activate" (
    echo [FEHLER] Das Setup wurde noch nicht ausgefuehrt! Bitte starte zuerst setup.bat.
    pause
    exit /b
)

call venv\Scripts\activate
cd Prank-Jump-and-Run
python Spiel.py

pause