from uebung_klassen_objekte.ball import *

# Objekt erzeugen -> eine Instanz(Objekt) von Ball erzeugen

# ball_player = Objekt / Ball = Klasse
ball_player = Ball()
print(ball_player.x)
print(ball_player.y)
print(ball_player.r)

# ball machine erzeugen
ball_machine = Ball()
print(ball_machine.r)
ball_machine.r = 17
print(ball_machine.r)
print(ball_player.r)