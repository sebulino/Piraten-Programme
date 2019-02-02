# Piraten-Programme
Hier finden sich die Programme der Piratenpartei Deutschland.
Im jeweiligen Ordner in der Datei README.md ist jeweils das Inhaltsverzeichnis.

## Vorgehensweise bei Aktualisierung des Programms:

Jeder angenommene Antrag zu einem Programm oder der Satzung wird als Issue angelegt. Zum Beispiel hier:
https://github.com/sebulino/Piraten-Programme/issues/new
Das neue Issue wird erhält drei Tags:
+ eins zur Kennzeichnung des Textkörpers, der von der Änderung betroffen ist (Programm, Europaprogramm, Satzung).
+ eins zur Kennzeichnung des Parteitags, in dem der Antrag angenommen wurde.
+ eins zur Kennzeichnung des Kapitels, in dem der Antrag zu änderungen führt. Sollte ein neues Kapitel eingefügt werden, dann mit der Kennzeichnung "neu".

Der Name des Branches [name_of_your_new_branch] besteht aus
'[Parteitag des Beschlusses]\_[Nummer des bearbeiteten Issues]'

### Für erfahrene Git-User:
+ Repo clonen bzw. 'git pull'
+ 'git checkout -b [name_of_your_new_branch]'
+ 'git push origin [name_of_your_new_branch]:[name_of_your_new_branch]'
Um zu prüfen, dass man im richtigen Branch ist:
'git branch'
+ Nach Änderungen bzw. dem Einarbeiten eines Issues:
'git commit -a -m '[Issue Nr.]'
+ Auf master Branch wechseln mit 'git checkout master'
+ 'git push https://github.com/sebulino/Piraten-Programme.git [name_of_your_new_branch]:[name_of_your_new_branch]'
+ 'git request-pull https://github.com/sebulino/Piraten-Programme.git master:[name_of_your_new_branch]'
+ delete your local branch with 'git branch -d [name_of_your_new_branch]'


---

1. __Angenommene Anträge__ der Bundesparteitage werden als Issue im Git Repository eingetragen.
2. Jedes Issue bekommt zwei Tags:
    + eins zur Kennzeichnung des Parteitags, in dem der Antrag angenommen wurde.
    + eins zur Kennzeichnung des Kapitels, in dem der Antrag zu änderungen führt. Sollte ein neues Kapitel eingefügt werden, dann mit der Kennzeichnung "neu".
3. Im Issue sollte auch ein Link zum Antrag festgehalten werden.
4. Für das __Einarbeiten der Anträge__ wird zunächst ein Issue zur Bearbeitung ausgesucht. Hierfür wird ein __Branch__ eröffnet bzw. ausgecheckt/darauf gewechselt. Dies kann man beispielsweise durch eine entsprechende Auswahl im Drop-Down Menü "Branch:".
5. Die entsprechenden Änderungen an den unmittelbar betroffenen Dateien werden vorgenommen. Dies Änderungen werden mit sprechendem Titel des Commits und der Issue-Nummer in der ersten Zeile des Nachrichtentexts ins Repository "committed". Anschließend wird der aktuelle Branch als Pull Request an das zentrale Repositorium gestellt.
WICHTIG: Bei Änderungen die die Nummerierung betreffen bitte entsprechende Änderungen im Inhaltsverzeichnis des Programms vornehmen.
6. Die Antragskommission bearbeitet die Pull Requests und überführt die jeweiligen Änderungen nach Überprüfung in das Repo. Nach dem Merge löscht der Bearbeiter den entsprechenden Branch.
