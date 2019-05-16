# twisted-realities script



## Installation der Requirements

Mache einen neuen Ordner indem der Twist-Code arbeiten kann. 
Dann das Terminal öffnen und folgende Befehle rein kopieren und Enter drücken (fragt nach Computerpasswort):

```bash
sudo easy_install pillow
git clone https://github.com/juhu92/twiste-realyties-script.git ~/Documents/twisted-realities-script
cd ~/Documents/twisted-realities-script/
open .

```


## Twist erstellen

Jetzt kann es los gehen. In den Ordner `./input` die Bilddateien im PNG Format abspeichern. Wichtig ist, dass genau so viele Dateien dort gespeichert sind, wie ein Bild hoch ist. Es müssen für ein 1024px hohes Bild als 1024 PNG Files platziert werden. Der Dateiname MUSS genau eine sechsstellige Zahl sein und mit "000000.png" beginnen. Das zweite Bild muss den Namen "000001.png" haben usw…
Sind die Bilder im Input-Ordner abgelegt, folgenden Befehl ins Terminal eingeben:
```bash
python make-frames.py
```
Für das rendern eines einzelnen Frames die 1 und dann Enter drücken. Um alle Frames zu rechnen 2 und Enter eingeben.
