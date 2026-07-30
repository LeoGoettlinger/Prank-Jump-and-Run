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

:: 3. REPOSITORY AUS GITHUB HOLEN / AKTUALISIEREN
set "PROJECT_DIR=%~dp0"
set "REPO_URL=https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git"
cd /d "%PROJECT_DIR%"

if exist ".git" (
    echo [INFO] Repository gefunden. Aktualisiere auf die neueste Version...
    git fetch origin main
    git reset --hard origin/main
) else (
    echo [INFO] Kein lokales Repository gefunden. Klone Repository aus GitHub...
    if exist "Spiel.py" (
        echo [WARN] Spielordner vorhanden, aber kein Git-Repository. Bitte den Ordner löschen oder als neues Repo initialisieren.
    )
    rmdir /s /q "%PROJECT_DIR%" 2>nul
    git clone -b main "%REPO_URL%" "%PROJECT_DIR%"
)

:: 4. VIRTUELLE UMGEBUNG & INSTALLATION
python -m venv venv
call venv\Scripts\activate

echo [INFO] Update Pip...
python -m pip install --upgrade pip

echo [INFO] Installiere Bibliotheken (Flexible Versionen)...
python -m pip install -r requirements.txt

:: 5. START
echo.
echo =========================================================
echo Startvorgang läuft...
echo =========================================================
python Spiel.py
pause
