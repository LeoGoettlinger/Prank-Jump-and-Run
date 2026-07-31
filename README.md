# 🎮 It's a Prank Jump & Run

Ein actionreiches 2D Jump & Run Spiel, entwickelt mit Python und der Arcade-Bibliothek. Sammle Münzen, finde Schlüssel für neue Level, nutze magische Tränke und weiche den tödlichen Stacheln aus!

## 🚀 Features

### 🎮 Gameplay & Level
- **3 einzigartige Level** mit steigender Schwierigkeit
- **Geheimer Schatzraum:** Finde den versteckten Schlüssel und entdecke den Bonus-Raum mit extra Schätzen!
- **Schlüssel-System:** Sammle Schlüssel, um verschlossene Tore zu öffnen und neue Bereiche freizuschalten
- **Teleporter & Röhren:** Nutze geheime Abkürzungen und Transport-Systeme
- **Leitern & Wasser:** Klettere an bestimmten Stellen nach oben

### ⚡ Power-Ups & Tränke
- **Multi-Jump Trank:** Erlaubt dir für kurze Zeit einen Doppelsprung in der Luft
- **Jump-Boost Trank:** Springe deutlich höher und erreiche schwer zugängliche Plattformen
- **Heiltränke:** Stelle 1 oder 2 verlorene Leben wieder her
- **Münzen:** Sammle so viele wie möglich für einen höheren Score
- **Schatztruhen:** Wertvolle Truhen bringen 5× mehr Punkte als normale Münzen!

### ⚠️ Gefahren & Herausforderungen
- **Tödliche Stacheln:** Berühre sie nicht, oder du verlierst ein Leben!
- **Schaden-Immunität:** Nach einem Treffer bist du kurzzeitig unverwundbar (wird im HUD angezeigt)
- **Zeit-Limit:** In manchen Modi zählt die Zeit gegen dich

### 🎯 Schwierigkeitsgrade
- **Easy:** 6 Leben, 10 Minuten Zeit, alle Tränke verfügbar, 2 Sekunden Immunität
- **Normal:** 4 Leben, 5 Minuten Zeit, alle Tränke verfügbar, 3 Sekunden Immunität
- **Hardcore:** 3 Leben, 2 Minuten Zeit, **keine Tränke**, **keine Immunität** - nur für Profis!
- **Custom:** Stelle alles selbst ein:
  - Zeit-Limit (10 Sekunden bis 1 Stunde)
  - Anzahl der Start-Leben (1-20)
  - Tränke an/aus
  - Immunitäts-Dauer (0-30 Sekunden)
  - Zeit-Anzeige an/aus
  - Stoppuhr-Modus (Zeit läuft hoch statt runter)

### 🏆 Highscores & Erfolge
- **Automatische Speicherung:** Deine besten Runs werden lokal gespeichert
- **Score-System:** Münzen + (Schätze × 5) - Schätze sind wertvoller!
- **Top 5 Highscores:** Sieh deine besten Leistungen im Menü
- **Achievements:** Schalte Erfolge frei wie:
  - "Key gefunden!" - Wenn du einen Schlüssel aufsammelst
  - "Level 2 freigeschaltet!" - Wenn du das erste Tor öffnest
  - "Level 3 geöffnet!" - Wenn du den zweiten Schlüssel findest
  - "Schatzraum geöffnet!" - Wenn du den geheimen Raum entdeckst
- **Achievement-Stack:** Wenn du mehrere Erfolge gleichzeitig freischaltest, werden sie nacheinander angezeigt

### 🎵 Audio & Atmosphäre
- **Dynamische Musik:** Die Hintergrundmusik wechselt automatisch zu epischer Musik, sobald du Level 3 erreichst
- **Soundeffekte:** Für jede Aktion gibt es passende Sounds (Münzen, Tränke, Schaden, etc.)
- **Musik-Steuerung:** Schalte mit `M` alle Sounds und Musik an/aus
- **Menü-Musik:** Es gibt eine Menü Musik!

### 📱 Menüs & Navigation
- **Start-Menü:** Neues Spiel starten, Highscores ansehen, Tutorial lesen oder Spiel beenden
- **Tutorial:** Lerne Steuerung, Items und Tipps kennen (mit Scroll-Funktion)
- **Pause-Menü:** Mit `P` oder `ESC` pausieren und:
  - Weiterspielen
  - Highscores ansehen
  - Tutorial lesen
  - Level neu starten
  - Neues Spiel mit anderen Einstellungen beginnen
  - Zurück zum Hauptmenü
- **Gewonnen/Verloren Screen:** Am Ende siehst du deine Statistiken und kannst direkt neu starten

### 💾 Sicherheit & Komfort
- **Automatische Speicherung:** Alle Einstellungen und Highscores werden sicher gespeichert
- **Plattformübergreifend:** Funktioniert auf Windows, macOS und Linux
- **Einmalige Lizenz-Akzeptierung:** Beim ersten Start musst du die Lizenz akzeptieren, danach nie wieder
- **Keine Internet-Verbindung nötig:** Das Spiel funktioniert komplett offline

---

## 🛠 Installation & Spielen

Es gibt zwei Wege, das Spiel zu spielen: Die **einfache Methode** (fertige Versionen herunterladen) für normale Spieler und die **Entwickler-Methode** für alle, die den Code bearbeiten oder eigene Maps testen möchten. Dadurch seit ihr auch immer Up-To-Date!

### 🎮 Für Spieler (Empfohlen)
Du brauchst **weder Python noch Git** auf deinem PC! Lade dir einfach das fertige Paket für dein Betriebssystem aus dem [Releases-Bereich](https://github.com/LeoGoettlinger/Prank-Jump-and-Run/releases) herunter!
Dann müsst ihr aber SELBSTSTÄNDIG merken wenn es einen neuen Release gibt, diesen herunterladen und installieren/starten!

#### 🪟 Windows
- **Portable (.exe):** Einfach herunterladen und per Doppelklick starten. Keine Installation nötig.
- **Installer (.msi):** Herunterladen, Doppelklick und den Installations-Anweisungen folgen (erstellt automatisch Desktop-Icons und Startmenü-Einträge).
- *Hinweis:* Da das Spiel ein Indie-Projekt ist und nicht offiziell von Microsoft signiert wurde, zeigt der Windows SmartScreen eventuell eine Warnung ("Der Computer wurde geschützt"). Klicke einfach auf *"Weitere Informationen"* ➔ *"Trotzdem ausführen"*.

#### 🍎 macOS
- **Disk Image (.dmg):** Herunterladen, öffnen und das App-Icon in den "Programme"-Ordner ziehen.
- **App Bundle (.app):** Herunterladen und direkt starten.
- *Wichtiger Hinweis für Mac-Nutzer:* Da die App nicht bei Apple registriert ist (was 100$/Jahr kostet), blockiert macOS den ersten Start aus Sicherheitsgründen. **Die Lösung:** Mache einen **Rechtsklick auf die App** ➔ Wähle **"Öffnen"** ➔ Bestätige das Popup erneut mit **"Öffnen"**. Danach läuft das Spiel für immer problemlos!

#### 🐧 Linux
- **Debian/Ubuntu/Mint (.deb):** Herunterladen und per Doppelklick öffnen. Der Software-Center startet und fragt nach deinem Admin-Passwort zur Installation. Das Spiel landet danach automatisch im Startmenü.
- **Andere Distributionen (.AppImage):** Herunterladen und einmalig ausführbar machen (Rechtsklick ➔ Eigenschaften ➔ Zugriffsrechte ➔ *"Datei als Programm ausführen"* oder im Terminal `chmod +x PrankJumpAndRun.AppImage`). Danach einfach per Doppelklick starten – keine Installation nötig!

---

### 💻 Für Entwickler (Aus dem Quellcode)
Falls du am Code arbeiten, eigene Maps im Tiled-Editor bauen oder das Spiel lokal testen möchtest:

**Voraussetzungen:**
- **Python 3.11** (Python 3.12+ funktioniert aktuell noch nicht fehlerfrei mit Arcade 3.x)
- **Git**

**Automatisches Setup:**
Die Skripte prüfen, ob alles vorhanden ist, erstellen eine isolierte virtuelle Umgebung und installieren automatisch alle nötigen Pakete (wie `arcade` und `pyglet`).
- **Windows:** Doppelklick auf die `Setup_Start.bat`.
- **macOS & Linux:** Öffne ein Terminal im Ordner und führe aus:
  ```bash
  chmod +x Setup_Start.sh
  ./Setup_Start.sh

---

## 🎮 Steuerung

* **Bewegen:** Pfeiltasten `Links`/`Rechts` oder `A` / `D`
* **Springen:** `Leertaste`, `Pfeiltaste Oben` oder `W`
* **Spiel beenden (Quit):** `Q`
* **Spiel neu starten (Reset):** `R` (Nützlich, wenn du gewonnen oder verloren hast)
* **Sounds an/ausschalten:** `M`
* **Pause Menü:** `P`/``Esc`

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
