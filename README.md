# Piraten-Programme
Hier finden sich die Programme der Piratenpartei Deutschland.
Im jeweiligen Ordner in der Datei README.md ist jeweils das Inhaltsverzeichnis.

## Vorgehensweise bei Aktualisierung des Programms:
1. __Angenommene Anträge__ der Bundesparteitage werden als Issue im Git Repository eingetragen.
2. Jedes Issue bekommt zwei Tags:
    + eins zur Kennzeichnung des Parteitags, in dem der Antrag angenommen wurde.
    + eins zur Kennzeichnung des Kapitels, in dem der Antrag zu änderungen führt. Sollte ein neues Kapitel eingefügt werden, dann mit der Kennzeichnung "neu".
3. Im Issue sollte auch ein Link zum Antrag festgehalten werden.
4. Für das __Einarbeiten der Anträge__ wird zunächst ein Issue zur Bearbeitung ausgesucht. Hierfür wird ein __Branch__ eröffnet bzw. ausgecheckt/darauf gewechselt. Dies kann man beispielsweise durch eine entsprechende Auswahl im Drop-Down Menü "Branch:".
5. Die entsprechenden Änderungen an den unmittelbar betroffenen Dateien werden vorgenommen. Dies Änderungen werden mit sprechendem Titel des Commits und der Issue-Nummer in der ersten Zeile des Nachrichtentexts ins Repository "committed". Anschließend wird der aktuelle Branch als Pull Request an das zentrale Repositorium gestellt.
WICHTIG: Bei Änderungen die die Nummerierung betreffen bitte entsprechende Änderungen im Inhaltsverzeichnis des Programms vornehmen.
6. Die Antragskommission bearbeitet die Pull Requests und überführt die jeweiligen Änderungen nach Überprüfung in das Repo. Nach dem Merge löscht der Bearbeiter den entsprechenden Branch.
