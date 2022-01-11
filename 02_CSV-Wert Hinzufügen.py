# Wir erstellen eine CSV Datei
import csv

# Datei anlegen
# Option a -> wenn vorhanden, Datei öffnen und anfügen (daten1.csv); sonst wird eine neue Datei erstellt
file1 = open("daten1.csv", "a")

# csv Händler anlegen (writer)
writer = csv.writer(file1, delimiter = ";")
writer.writerow([3, "Fritz", "Geier"])
file1.close()


