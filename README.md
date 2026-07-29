# 🎮 It's a Prank Jump & Run

Ein actionreiches 2D Jump & Run Spiel, entwickelt mit Python und der Arcade-Bibliothek. Sammle Münzen, finde Schlüssel für neue Level, nutze magische Tränke und weiche den tödlichen Stacheln aus!

## 🚀 Features

- **Interaktives Setup/Settings:** Bevor das eigentliche Spiel startet, kannst du nach dem Start in einer grafischen UI Parameter wie Start-Leben, Zeitlimits und Unverwundbarkeits-Dauer anpassen.
- **Power-Ups & Tränke:** - Multi-Jump-Tränke (erlaubt Doppelsprünge für eine bestimmte Zeit)
  - Jump-Boost-Tränke (höhere Sprungkraft)
  - Lebens-Tränke (+1 oder +2 Herzen)
- **Rätsel & Entdeckungen:**
  - Sammle Schlüssel, um Tore zu öffnen und in neue Level (bis Level 3) vorzudringen.
  - Finde den geheimen Schlüssel für den Schatz-Raum!
  - Nutze Teleporter und Röhren, um über die Map zu reisen.
- **Gefahren:** Weiche Stacheln aus. Wirst du getroffen, verlierst du ein Leben, erhältst aber kurzzeitig Schaden-Immunität.
- **Dynamische Musik:** Die Hintergrundmusik ändert sich, sobald du Level 3 erreichst (Epic Music!).
- **Sounds:** Es gibt Sounds für alles!
- **Achievements:** Es gibt auch viele verschiedene Achievements.
- **Custom Schriftarten:** Wir haben eine Custom Schrift.
- **Presets:** Es gibt Presets für einen Start!
- **Hardcore Preset:** Es gibt einen Hardcore Preset, perfekt fürs Speedrunnen!
- **Verbleibende Zeit:** Challenge deine Freunde: Wer schaft es schneller durchzuspielen?

---

## 🛠 Installation & Setup

Dieses Projekt installiert alle nötigen Abhängigkeiten fast von selbst. Die Skripte prüfen, ob **Git** und **Python** vorhanden sind und richten eine isolierte Spielumgebung ein.

### Windows (10/11)
1. Lade die Datei `Setup_Start.bat` aus diesem Repository herunter.
2. Doppelklicke auf `Setup_Start.bat`.
3. **Hinweis:** Falls Git oder Python (3.12.2) noch nicht auf deinem PC sind, installiert das Skript diese. Falls du dazu aufgefordert wirst, schließe das Konsolenfenster nach der Installation und starte die `.bat` Datei einfach **ein zweites Mal**.
4. Das Skript klont das Repository, erstellt eine virtuelle Umgebung und installiert automatisch Arcade (3.3.2) und Pyglet (2.0.17).

### macOS & Linux
1. Lade die Datei `Setup_Start.sh` herunter.
2. Öffne ein Terminal im entsprechenden Ordner.
3. Mache das Skript ausführbar:
```
chmod +x Setup_Start.sh
```
5. Starte das Skript(bash):
```
./Setup_Start.sh
```


5. Fehlende Pakete werden automatisch via Homebrew (Mac) oder APT (Linux) installiert und das Spiel startet anschließend.

---

## 🎮 Steuerung

* **Bewegen:** Pfeiltasten `Links`/`Rechts` oder `A` / `D`
* **Springen:** `Leertaste`, `Pfeiltaste Oben` oder `W`
* **Spiel beenden (Quit):** `Q`
* **Spiel neu starten (Reset):** `R` (Nützlich, wenn du gewonnen oder verloren hast)
* **Musik an/ausschalten:** `M`

---

## 📦 Systemvoraussetzungen (Automatisch verwaltet)

Das Spiel benötigt folgende Versionen, welche durch die Start-Skripte automatisch lokal eingerichtet werden:

* **Python:** 3.12.2
* **Arcade:** 3.3.2
* **Pyglet:** 2.0.17

---

## 🐛 Bugs & Feedback

Hast du einen Fehler gefunden oder eine coole Idee für ein neues Level, neue Hindernisse oder Tränke?

* **Bug melden:** Falls das Spiel abstürzt oder eine Kollision nicht funktioniert, erstelle bitte ein "Issue".
* **Empfehlungen:** Du hast Ideen für das Gameplay? Schreib es uns ebenfalls in die Issues!

👉 [Hier Bugs melden oder Empfehlungen abgeben](https://github.com/LeoGoettlinger/Prank-Jump-and-Run/issues)

---

## LICENSE

**Dieses Spiel ist mit der Apache 2 Lizenz gesichert!**

---

## 👨‍💻 Entwickler

Code & Design by: **SampleCraft (Leo Göttlinger)**
© 2025-2026 Leo Göttlinger

Projekt-Repository: [https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git](https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git)

---
