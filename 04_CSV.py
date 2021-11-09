#iris.csv öffnen
#jede Zeile ausgeben, in der die erste Spalte den Wert größer gleich 5 hat

import csv
file1 = open("iris.csv","r")

reader = csv.reader(file1, delimiter = ",")

for row in reader:
    tmp = float(row[0])
    if tmp >= 5:
        print(row)

file1.close