@echo off
echo ====================================================
echo      It's a Prank Jump & Run - Setup (Windows)
echo ====================================================
echo.

REM Pruefen, ob Python installiert ist
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [FEHLER] Python ist nicht installiert oder nicht im PATH!
    echo Bitte lade Python 3.12.2 von python.org herunter und setze den Haken bei "Add Python to PATH".
    pause
    exit /b
)

REM Pruefen, ob Git installiert ist
git --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [FEHLER] Git ist nicht installiert oder nicht im PATH!
    echo Bitte lade Git von git-scm.com herunter.
    pause
    exit /b
)

echo [1/4] Klone das GitHub Repository (Branch: main)...
IF NOT EXIST "Prank-Jump-and-Run" (
    git clone -b main https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git
) ELSE (
    echo Ordner existiert bereits. Ziehe neueste Updates...
    cd Prank-Jump-and-Run
    git pull origin main
    cd ..
)

echo [2/4] Erstelle eine lokale virtuelle Python-Umgebung...
python -m venv venv

echo [3/4] Aktiviere die Umgebung und update pip...
call venv\Scripts\activate
python -m pip install --upgrade pip

echo [4/4] Installiere Arcade 3.3.2 und Pyglet 2.0.17...
pip install arcade==3.3.2 pyglet==2.0.17

echo.
echo ====================================================
echo Setup erfolgreich abgeschlossen! 
echo Du kannst das Spiel nun mit start.bat starten.
echo ====================================================
pause