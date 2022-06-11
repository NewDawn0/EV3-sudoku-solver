# Info
## Inhaltsverzeichnis
- Anforderungen
- Einrichtung
- Kredite
- Zusätzliche Informationen

## Anforderungen
- EV3-Steine
- Wifi-Dongle
- Legos (insbesondere Lego Technic)
- Laptop/PC (unabhängig vom Betriebssystem, vorzugsweise ein UNIX-basiertes System)
- [VSCode](https://code.visualstudio.com)
- [NodeJS](https://nodejs.org/en/)

## Einrichtung
### Vor installation
Klone das Projekt auf ihr Gerät</br>
Gehen sie in den EV3-Sudoku-Solver-Ordner</br>
Öffnen Sie den Ordner in VSCode</br>
```bash
git clone <projectName>
cd ev3-sudoku-solver
code .
```
Installiere die [EV3 VS Code](https://marketplace.visualstudio.com/items?itemName=lego-education.ev3-micropython) Erweiterung und verbinde sie mit deinem EV3-Gerät</br>
Stecken Sie den Wi-Fi-Dongle in den EV3 Brick und prüfen Sie, ob das Internet verfügbar ist.
Öffne ein SSH-Terminal und verwende den folgenden Befehl im ssh-Terminal</br>
```bash
# Opening an SSH terminal
ssh robot@ev3dev.local

# Checking for internet in the ssh session
ping google.com
```
### Ändern Sie die IP in der main.py Datei in Zeile 34 auf Ihre IP
Ermitteln Sie Ihre IP mit:
In Linux:
```bash
hostname -I
```
In MacOs:
```bash
ifconfig | grep "inet " | grep -Fv 127.0.0.1 | awk '{print $2}'
```
In Windows (nicht getestet)
```Powershell
Get-NetIPAddress -AddressFamily IPv4 -InterfaceIndex $(Get-NetConnectionProfile | Select-Object -ExpandProperty InterfaceIndex) | Select-Object -ExpandProperty IPAddress
```
Ersetzen Sie die aktuelle IP durch Ihre IP mit der folgenden Syntax:</br>
```python
# main.py line 34
Board = os.system('curl -s <YourIP>:3000/api/boardOut | grep -o "[0-9]*" > io.txt')
```
### Starten Sie den Webserver für die Website auf Ihrem Laptop/PC (das Gerät mit der gerade eingegebenen IP)</br>
Öffnen Sie ein neues Terminal, wechseln Sie in das Verzeichnis der Website und starten Sie den Server
```bash
cd site
npm start
```
Wenn Sie eine Ausgabe wie die folgende sehen, läuft Ihr Server und Sie sind startklar
```javascript
> site@1.0.0 start
> node server.js

0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 0 
Server is running on port 3000
```
Sie sollten nun in der Lage sein, ein Browser-Tab auf einem beliebigen Gerät inm Wi-Fi Netzwerk zu öffnen und die Website mit der folgenden URL zu öffnen:
```javascript
<YourIP>:3000
```
### Und als letzter Schritt testen sie, ob es funktioniert
Das Programm muss nun nur noch heruntergeladen und ausgeführt werden, indem sie <br>
*<span style="color:coral">fn </span> + <span style="color:coral">f5 </span>* auf ihrem Laptop/PC in VS Code drücken
Wenn alles erfolgreich verlaufen ist, wird der Bot das Brett von der Website nehmen und es lösen

## Kredite
Hier ist eine Liste der externen Codequellen, die ich in diesem Projekt verwendet habe
- Code aus [diesem video](https://www.youtube.com/watch?v=S4uRtTb8U-U) wurde verwendet, um den größten Teil des Frontends für die Website zu erstellen
- Code aus [diesem](https://levelup.gitconnected.com/sudoku-solver-python-using-backtracking-1aff17a3340) and [diesem ](https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/) blog wurden verwendet, um Teile des Lösungsalgorithmus zu erstellen
- Der Rest ist alles Originalcode

## Zusätzliche Informationen
### Projektstruktur
```
EV3-Sudoku-Solver
├── .vscode
│  ├── extensions.json
│  ├── launch.json
│  ├── settings.json
│  └── tasks.json
├── old
│  └── testing
│     └── //Old test files
├── site
│  ├── node_modules
│  │  └── //NodeJS libraries
│  ├── public
│  │  ├── comfyWaves.jpg
│  │  ├── index.html
│  │  ├── script.js
│  │  └── style.css
│  ├── package-lock.json
│  ├── package.json
│  └── server.js
├── .gitignore
├── io.txt
├── main.py
└── README.md
```
### site Ordner
Im Websiteordner befinden sich alle erforderlichen Komponenten für die Website

### "old" Ordner
Der alte Ordner ist ein Ordner, der alle älteren Versionen und Testdateien für das Projekt enthält, wie die optimierte C++-Version und andere nicht verwendete Dateien. Keine der Dateien im alten Ordner werden benötigt, d.h. Sie können diesen Ordner löschen, um Speicherplatz zu sparen, und das Projekt wird trotzdem laufen

### Wichtige Dateien
- Die Datei main.py ist die Datei, die auf dem EV3 Stein ausgeführt wird.
- Die Datei io.txt ist eine temporäre Datei, die gelöscht werden kann, aber vom Programm wiederhergestellt wird, wenn es erneut ausgeführt wird
Sie speichert temporär die Daten vom Webserver

