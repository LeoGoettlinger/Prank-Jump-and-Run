@echo off
echo =========================================================
echo    It's a Prank Jump & Run - Auto-Installer (Windows)
echo =========================================================
echo.

:: 1. PRUEFEN UND INSTALLIEREN VON GIT
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Git fehlt. Installiere...
    winget install --id Git.Git -e --silent --accept-package-agreements --accept-source-agreements
    echo [WICHTIG] Bitte dieses Fenster SCHLIESSEN und die Datei NEU STARTEN!
    pause
    exit
)

:: 2. PRUEFEN UND INSTALLIEREN VON PYTHON 3.12
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Python fehlt. Installiere...
    winget install --id Python.Python.3.12 -e --silent --accept-package-agreements --accept-source-agreements
    echo [WICHTIG] Bitte dieses Fenster SCHLIESSEN und die Datei NEU STARTEN!
    pause
    exit
)

:: 3. REPOSITORY KLONEN
if not exist "Prank-Jump-and-Run\.git" (
    echo [INFO] Klone Repository neu...
    rmdir /s /q "Prank-Jump-and-Run" 2>nul
    git clone -b main https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git
) else (
    echo [INFO] Suche nach Updates...
    cd Prank-Jump-and-Run
    git pull origin main
    cd ..
)

:: 4. VIRTUELLE UMGEBUNG & INSTALLATION
cd Prank-Jump-and-Run
python -m venv venv
call venv\Scripts\activate

echo [INFO] Update Pip...
python -m pip install --upgrade pip

echo [INFO] Installiere Bibliotheken (Flexible Versionen)...
:: Wir nutzen >= für bessere Kompatibilität
python -m pip install "arcade>=3.0.0"
python -m pip install "pyglet>=2.0.0"

:: 5. START
echo.
echo =========================================================
echo Startvorgang läuft...
echo =========================================================
python Spiel.py
pause
