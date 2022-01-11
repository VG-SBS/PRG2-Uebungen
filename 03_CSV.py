# Wir erstellen eine CSV Datei
import csv

# Datei öffnen und lesen mit "r"
file1 = open("daten1.csv", "r")

# csv Händler anlegen (reader)
reader = csv.reader(file1, delimiter = ";")

#mit (row[1]) wird nur die Spalte 1 der Liste ausgegeben
for row in reader:
    print(row[1])

file1.close()
