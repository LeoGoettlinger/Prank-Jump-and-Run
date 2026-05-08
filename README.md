# 🎮 It's a Prank Jump & Run

Ein dynamisches und unterhaltsames Jump & Run Spiel, entwickelt mit Python und der Arcade-Bibliothek. Navigiere deine Spielfigur durch herausfordernde Level, weiche Hindernissen aus und erlebe die "Prank"-Features!

## 🚀 Features

- **Intelligente Engine:** Nutzt Python 3.12.2 und Arcade 3.3.2 für flüssiges Gameplay.
- **Einzigartige Spielmechaniken:**
    - **Ghost Rooms:** Nachrichten und Elemente verschwinden nach einer festgelegten Zeit.
    - **Privacy Mode:** Erstelle Chats oder Aktionen im Inkognito-Modus.
    - **Dead Man's Switch:** Ein Sicherheits-Feature für deine "virtuellen Identitäten".
    - **Ghost Switch:** Ein spezieller Schalter für die Chat-Interaktion.
- **Virtuelle Identitäten:** Setze Namen, User-Tags, Beschreibungen und Avatare für deine Schatten-Identitäten.
- **Media Transcoding:** Automatische Optimierung von Bildern und Videos im Hintergrund.

---

## 🛠 Installation & Setup

Dieses Projekt ist so konzipiert, dass es sich auf einem "frischen" System fast vollständig von selbst installiert. Die mitgelieferten Skripte prüfen, ob **Git** und **Python** vorhanden sind und installieren diese bei Bedarf automatisch.

### Windows (10/11)
1. Lade die Datei `Start_Spiel.bat` aus diesem Repository herunter.
2. Doppelklicke auf `Start_Spiel.bat`.
3. **Hinweis:** Falls Git oder Python noch nicht auf deinem PC sind, installiert das Skript diese im Hintergrund. Falls du dazu aufgefordert wirst, schließe das Fenster nach der Installation und starte die `.bat` Datei einfach **ein zweites Mal**.
4. Das Skript klont das Repository, erstellt eine virtuelle Umgebung und installiert alle Abhängigkeiten (Arcade 3.3.2, Pyglet 2.0.17).

### macOS & Linux
1. Lade die Datei `start_spiel.sh` herunter.
2. Öffne ein Terminal im entsprechenden Ordner.
3. Mache das Skript ausführbar:
   ```bash
   chmod +x start_spiel.sh

```

4. Starte das Skript:
```bash
./start_spiel.sh

```


5. Das Skript installiert fehlende Pakete (via Homebrew auf Mac oder APT auf Linux) und startet das Spiel.

---

## 🎮 Steuerung

* **Bewegen:** Pfeiltasten oder `W`, `A`, `S`, `D`.
* **Springen:** `Leertaste` oder `Pfeil oben`.
* **Reset:** Drücke `R`, wenn du gewonnen oder verloren hast, um das Level neu zu starten.
* **Interaktion:** Nutze die speziellen In-Game-Schalter für den **Ghost Mode** oder den **Dead Man's Switch**.

---

## 📦 Systemvoraussetzungen (Automatisch verwaltet)

Das Spiel benötigt und installiert lokal folgende Versionen:

* **Python:** 3.12.2
* **Arcade:** 3.3.2
* **Pyglet:** 2.0.17
* **Git:** Zum Abrufen der neuesten Spiel-Updates.

---

## 🐛 Bugs & Feedback

Hast du einen Fehler gefunden oder hast du eine coole Idee für ein neues "Prank"-Feature? Wir freuen uns über jeden Beitrag!

* **Bug melden:** Falls das Spiel abstürzt oder etwas nicht funktioniert, erstelle bitte ein "Issue" auf unserer GitHub-Seite.
* **Verbesserungen:** Du hast Empfehlungen für das Gameplay oder das UI? Schreib es uns ebenfalls in die Issues!

👉 [Hier Bugs melden oder Feedback geben](https://www.google.com/search?q=https://github.com/LeoGoettlinger/Prank-Jump-and-Run/issues)

---

## 👨‍💻 Entwickler

Erstellt von **Leo Göttlinger**.
Projekt-Repository: [https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git](https://www.google.com/search?q=https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git)

---

*Viel Spaß beim Spielen! Pass auf, dass du nicht geprankt wirst!* 🃏

```

***

### Tipps zum Hinzufügen:
1. **GitHub Issues:** Da du nach der Bug-Report-Seite gefragt hast, habe ich den Link direkt unter der Sektion "Bugs & Feedback" eingefügt.
2. **Icons:** Ich habe ein paar Emojis hinzugefügt, damit das README auf GitHub moderner und einladender aussieht.
3. **Pflege:** Wenn du neue Features einbaust (z.B. neue Tastenbelegungen), vergiss nicht, sie kurz in der Sektion "Steuerung" zu ergänzen!

```
