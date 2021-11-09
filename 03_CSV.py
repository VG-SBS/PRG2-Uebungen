# Wir erstellen eine CSV Datei
import csv

# Datei öffnen und lesen mit "r"
file1 = open("daten1.csv", "r")

# csv Händler anlegen (reader)
reader = csv.reader(file1, delimiter = ";")

for row in reader:
    print(row)

file1.close()
