# 🎮 It's a Prank Jump & Run

Ein actionreiches 2D Jump & Run Spiel, entwickelt mit Python und der Arcade-Bibliothek. Sammle Münzen, finde Schlüssel für neue Level, nutze magische Tränke und weiche den tödlichen Stacheln aus!

## 🚀 Features

- **Interaktives Terminal-Setup:** Bevor das eigentliche Spiel startet, kannst du in der Konsole Parameter wie Start-Leben, Zeitlimits und Unverwundbarkeits-Dauer anpassen.
- **Power-Ups & Tränke:** - Multi-Jump-Tränke (erlaubt Doppelsprünge für eine bestimmte Zeit)
  - Jump-Boost-Tränke (höhere Sprungkraft)
  - Lebens-Tränke (+1 oder +2 Herzen)
- **Rätsel & Entdeckungen:**
  - Sammle Schlüssel, um Tore zu öffnen und in neue Level (bis Level 3) vorzudringen.
  - Finde den geheimen Schlüssel für den Schatz-Raum!
  - Nutze Teleporter und Röhren, um über die Map zu reisen.
- **Gefahren:** Weiche Stacheln aus. Wirst du getroffen, verlierst du ein Leben, erhältst aber kurzzeitig Schaden-Immunität.
- **Dynamische Musik:** Die Hintergrundmusik ändert sich, sobald du Level 3 erreichst (Epic Music!).
- **Settings:** Diese werden bei jedem Start/Restart aufegerufen. Dort kannst du viele Einstellungen machen!
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

## 👨‍💻 Entwickler

Code & Design by: **SampleCraft (Leo Göttlinger)**
© 2025-2026 Leo Göttlinger

Projekt-Repository: [https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git](https://github.com/LeoGoettlinger/Prank-Jump-and-Run.git)

---

https://www.swisstransfer.com/d/ca752f69-7821-4db4-a6bd-c4f313bab005

1. Projektübersicht
Entwickle einen vollumfänglichen, modularen Multipurpose Discord Bot namens SC‑Systems Bot.  
Der Bot muss alle Features aus sämtlichen angehängten Quellcodes übernehmen und in ein einheitliches, modulares System integrieren.

Branding:
- Name: SC‑Systems Bot  
- Beschreibung: Ultimate Purpose Discord Bot! Made by SampleCraft!  
- Profilbild: (angehängt)  
- Banner: (angehängt)

Der Bot muss automatisch sicherstellen, dass:
- Name  
- Nickname  
- Avatar  
- Banner  
- Aktivitätsstatus  
niemals dauerhaft verändert werden können.  
Änderungen werden sofort zurückgesetzt.

---

2. Aktivitätsrotation (nur Owner editierbar)
Der Bot zeigt eine rotierende Aktivität, die:
- alle 3 Sekunden wechselt  
- alle aktivierten Features durchläuft  

Wichtig:  
- Nur der Bot‑Owner darf Aktivitäten bearbeiten  
- Änderungen erfolgen ausschließlich über eine Datei (activities.yml)  
- Keine Commands für Aktivitäten  

---

3. Modulares System mit eigener YML pro Modul
Jedes Modul erhält eine eigene Datei:
Zum Beispiel:

modules/
  moderation.yml
  economy.yml
  tickets.yml
  leveling.yml
  music.yml
  ...


Anforderungen:
- Module können:
  - global aktiviert/deaktiviert werden  
  - pro Server aktiviert/deaktiviert werden  
  - per Datei oder per Command (nur auf Admin‑Discord) gesteuert werden  
- Module laden dynamisch  
- Hot‑Reload ohne Neustart  
- Module dürfen sich nicht gegenseitig blockieren  

---

4. Server‑spezifische Modul‑Konfiguration
Jeder Discord‑Server erhält eine eigene Datei:


servers/<serverID>/config.yml


Diese Datei enthält:
- Server‑Einstellungen  
- Aktivierungsstatus  
- Key‑Informationen  
- Einen Abschnitt für jedes Modul, zum Beispiel:

`yaml
modules:
  moderation:
    enabled: true
    config:
      warn_limit: 3
      mute_duration: "10m"

  tickets:
    enabled: false
    config:
      category: "Support"
`

Steuerung:
- Per Command (nur auf Admin‑Discord)  
- Per Datei (direkt editierbar)  

---

5. Multi‑Server Aktivierungssystem (Key‑System)
Der Bot darf nicht automatisch auf jedem Server aktiv sein.  
Stattdessen gibt es ein Key‑basiertes Aktivierungssystem.

5.1 Key‑Generierung (nur Admin‑Discord)
Ein Admin kann Keys generieren mit:
- Anzahl erlaubter Server  
- Ablaufzeit  
- Beschreibung  
- Manuelle Deaktivierung  

5.2 Key‑Einlösung
- Server‑Admin gibt Key per Command ein  
- Bot aktiviert sich  
- Aktivierung wird gespeichert in:
  - keys.yml  
  - servers/<id>/config.yml  

5.3 Richtlinien‑Check
Der Bot muss automatisch prüfen, ob das Key‑System Discord‑konform ist.

Er prüft:
- Discord Developer Terms  
- Discord ToS  
- Bot Verification Rules  
- Monetarisierungsrichtlinien  

Wenn ein Key‑System‑Vorgang gegen Richtlinien verstößt:
- Aktivierung wird verweigert  
- Warnung wird ausgegeben  
- Log‑Eintrag wird erstellt  

---

6. Global Broadcast System
Der Bot kann:
- Nachrichten an alle aktivierten Server senden  
- in den Setup‑Channel  
- optional zeitgesteuert  
- nur steuerbar vom Admin‑Discord  

---

7. Setup & Installation
Der Bot wird als ZIP‑Archiv ausgeliefert mit:
- vollständigem Bot‑Code  
- allen Modulen  
- allen Ressourcen  
- Setup‑Dateien für:
  - Windows → .bat  
  - Linux → .sh  
  - macOS → .sh  

Setup‑Dateien müssen:
- alle Abhängigkeiten installieren  
- Umgebungsvariablen setzen  
- Startskripte erstellen  
- Logs konfigurieren  
- optional Autostart aktivieren  

---

8. Feature‑Import
Übernehme alle Features aus allen angehängten Bots, sofern Discord‑konform.

Bei redundanten Features:
- beste Version wählen  
- vereinheitlichen  
- modular integrieren  

---

9. Konfigurationssystem
Der Bot benötigt folgende Dateien:

Global:
- config.yml  
- modules.yml (globale Modulverwaltung)  
- keys.yml  
- activities.yml (nur Owner editierbar)  

Pro Modul:
- modules/<modulname>.yml

Pro Server:
- servers/<id>/config.yml  
  - inkl. Modul‑Abschnitten  
  - inkl. Key‑Status  
  - inkl. Server‑Konfiguration  

Alles muss:
- live reloadbar  
- logisch strukturiert  
- kommentiert  
- sicher  
sein.

---

10. Rückfragen
Falls Informationen fehlen, stelle bitte gezielte Rückfragen, bevor du mit der Generierung beginnst.
