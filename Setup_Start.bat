@echo off
echo =========================================================
echo    It's a Prank Jump & Run - Auto-Installer (Windows)
echo =========================================================
echo.

:: 1. PRUEFEN UND INSTALLIEREN VON GIT
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Git ist nicht installiert. Starte automatischen Download via Winget...
    winget install --id Git.Git -e --silent --accept-package-agreements --accept-source-agreements
    echo.
    echo =================================================================
    echo [WICHTIG] Git wurde installiert! 
    echo Windows muss die Pfade aktualisieren. 
    echo Bitte SCHLIESSE dieses Fenster und STARTE DIESE DATEI NEU!
    echo =================================================================
    pause
    exit
)

:: 2. PRUEFEN UND INSTALLIEREN VON PYTHON 3.12
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Python ist nicht installiert. Starte automatischen Download via Winget...
    winget install --id Python.Python.3.12 -e --silent --accept-package-agreements --accept-source-agreements
    echo.
    echo =================================================================
    echo [WICHTIG] Python wurde installiert! 
    echo Windows muss die Pfade aktualisieren. 
    echo Bitte SCHLIESSE dieses Fenster und STARTE DIESE DATEI NEU!
    echo =================================================================
    pause
    exit
)

:: 3. REPOSITORY KLONEN
echo [INFO] Git und Python sind bereit.
if not exist "Prank-Jump-and-Run" (
    echo [INFO] Lade Spiel-Dateien von GitHub herunter...
    git clone -b main https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git
) else (
    echo [INFO] Spiel-Dateien existieren bereits. Suche nach Updates...
    cd Prank-Jump-and-Run
    git pull origin main
    cd ..
)

:: 4. VIRTUELLE UMGEBUNG & SPIEL-ABHÄNGIGKEITEN INSTALLIEREN
echo [INFO] Richte geschuetzte Python-Umgebung ein...
cd Prank-Jump-and-Run
python -m venv venv
call venv\Scripts\activate

echo [INFO] Installiere Arcade und Pyglet...
python -m pip install --upgrade pip --quiet
pip install arcade==3.3.2 pyglet==2.0.17 --quiet

:: 5. SPIEL STARTEN
echo.
echo =========================================================
echo Alles erfolgreich geladen! Das Spiel startet jetzt...
echo =========================================================
python Spiel.py

pause
