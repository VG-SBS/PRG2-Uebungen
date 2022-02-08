import sqlite3

#beim ersten Aufruf wird die Datenbank erzeugt, sonst nur verbunden
connection = sqlite3.connect('database1.db')

#für SQL Statements brauchen wir den cursor
cursor = connection.cursor()

#Tabelle erstellen
cursor.execute('''
CREATE TABLE IF NOT EXISTS user
(id INT PRIMARY KEY NOT NULL, givenname TEXT, surname TEXT, Geburtsdatum Date)
''')

#Tabelle füllen
cursor.execute('''
INSERT INTO user VALUES (12, 'Max', 'Musterman',"1.6.1990")
''')
#kkk

#Tabelle füllen
cursor.execute('''
INSERT INTO user VALUES (22, 'Eva', 'Musterfrau',"6.5.1992")
''')

#Änderungen speichern
connection.commit()

#Tabelle ausgeben
cursor.execute('''
SELECT * FROM user
''')
print(cursor.fetchall())

#Änderungen vornehmen
cursor.execute('''
update user
set surname = "Mustermann"
where id = 10
''')

#Tabelle füllen
cursor.execute('''
insert into user values(31,"Martin","Schmidt","7.6.1993")
''')

#Teil der Tabelle ausgeben
cursor.execute('''
select * from user
where Geburtsdatum > "2.2.1992"
''')
#Änderungen speichern
connection.commit()
print(cursor.fetchall())

#Verbindung schließen
cursor.close()

#Kommentar
