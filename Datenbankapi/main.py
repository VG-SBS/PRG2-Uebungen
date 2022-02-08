from datenbankapi import DB

db = DB()

pk_max = db.createPlayer("Hans")
print(pk_max)

pk_max = db.createPlayer("Wurst")
print(pk_max)

pk_max = db.createPlayer("Wurst2")
print(pk_max)


player = db.getPlayer(1)
print(player)


player35 = db.setPlayerScore(100,5)

player35 = db.getPlayerScore(5)
print(player35)