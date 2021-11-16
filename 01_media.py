# Importieren des OS - Modules
import os

# Die Liste aller Dateien des Pfades aufrufen
path = "/Users/student/music"

#Variable mit dem Befehl der Ausgabe definieren
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# Alle Dateien ausgeben
print(dir_list)