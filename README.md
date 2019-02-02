# Piraten-Programme
Hier finden sich die Programme der Piratenpartei Deutschland.
Im jeweiligen Ordner in der Datei README.md ist jeweils das Inhaltsverzeichnis.

## Vorgehensweise bei Aktualisierung des Programms:

### Angenommene Anträge als Issue erfassen
Jeder angenommene Antrag zu einem Programm oder der Satzung wird als Issue angelegt. Zum Beispiel hier:
https://github.com/sebulino/Piraten-Programme/issues/new

Das neue Issue wird erhält drei Tags:

eins zur Kennzeichnung des Textkörpers, der von der Änderung betroffen ist (Programm, Europaprogramm, Satzung).
* eins zur Kennzeichnung des Parteitags, in dem der Antrag angenommen wurde.
* eins zur Kennzeichnung des Kapitels, in dem der Antrag zu änderungen führt. Sollte ein neues Kapitel eingefügt werden, dann mit der Kennzeichnung "neu".

Der Name des Branches [branchname] besteht aus
"[Parteitag des Beschlusses]\_[Nummer des bearbeiteten Issues]", also z.B. "18\_2_59" für das Issue #59, das einen Antrag auf dem Bundesparteitag 18.2 beschreibt.


### Einarbeiten der Issues - ohne git-Erfahrung
1. Auswahl eines Issues, das eingearbeitet werde muss. Vorzugsweise wird ein Issue des am weitesten zurückliegenden Bundesparteitags gewählt. Hierbei helfen die Label weiter.
2. In der Ordnerstruktur wird nun der entsprechende Textkörper ausgewält, z.B. "Satzung".
3. Hier wird nun die im Antrag zur Änderung oder Ergänzung beschriebene Textpassage gesucht.
4. Nach dem Klicken auf den Stift kann man nun die entsprechenden Änderungen an der Datei vornehmenn.
5. Nach Abschluss der Änderungen können im Formular am Ende des Textfeldes die Änderungen eingegeben werden. Hierzu wird der Name/Titel des Issues in der oberen Zeile eingegeben. Im Textfeld drunter wird die Nummer des Issues eingetragen, als z.B. "59".
6. Anschließend die Checkbox "Create new branch" (oder anderssprachiges Äquivalent) auswählen und einen Branch-Namen eintragen. Dieser besteht aus
"[Parteitag des Beschlusses]\_[Nummer des bearbeiteten Issues]", also z.B. "18\_2_59" für das Issue #59, das einen Antrag auf dem Bundesparteitag 18.2 beschreibt.
7. Abschließend "Propose File Change" (oder anderssprachiges Äquivalent) anklicken. Im folgenden Fenster reicht es aus auf "Create pull request" zu klciken.

Vielen Dank!

### Einarbeiten der Issues - für erfahrene git-User
+ Repo clonen `git clone https://github.com/sebulino/Piraten-Programme.git` bzw. `git pull`
+ `git checkout -b [branchname]`

Um zu prüfen, dass man im richtigen Branch ist: `git branch`
+ Nach Änderungen bzw. dem Einarbeiten eines Issues:

```
git add .
git commit -a -m "[Issue Nr.]", zum Beispiel (git commit -a -m "#17")
```

+ Auf master Branch wechseln mit `git checkout master`
+ Ins Github Repo pushen und Pull Request anlegen:

```
git push https://github.com/sebulino/Piraten-Programme.git [branchname]:[branchname]
git request-pull https://github.com/sebulino/Piraten-Programme.git master:[branchname]
```

+ Lokalen Branch löschen mit `git branch -d [branchname]`


Vielen Dank!
