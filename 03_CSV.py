# Wir erstellen eine CSV Datei
import csv

# Datei öffnen und lesen mit "r"
file1 = open("daten1.csv", "r")

# csv Händler anlegen (writer)
writer = csv.writer(file1, delimiter = ";")
writer.writerow(["ID", "Vorname", "Nachname"])
writer.writerow([1, "Max", "Meier"])
writer.writerow([2, "Hans", "Schmidt"])
file1.close()
#T