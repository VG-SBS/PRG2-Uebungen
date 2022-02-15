from datenbankapi import DB

#db wird aus Klasse DB erstellt
db = DB()

#Player Hans wird erstellt und gibt Händler zurück(pk_max)
pk_max = db.createPlayer("Hans")
print(pk_max)

pk_max = db.createPlayer("Wurst")
print(pk_max)

pk_max = db.createPlayer("Wurst2")
print(pk_max)

#Playername wird anhand der PK ausgegeben
player = db.getPlayer(1)
print(player)

#Player Score wird gesetzt (Scr, PK)
player35 = db.setPlayerScore(100,5)

#Playerscore wird anhand von pk ausgelesen und zurückgegeben
player35 = db.getPlayerScore(5)
print(player35)

