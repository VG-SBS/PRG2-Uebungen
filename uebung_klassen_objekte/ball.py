# Klassennamen beginnen mit einem Großbuchstaben.
class Ball:
    # Konstruktor zum erzeugen des Objektes __init__(self)
    def __init__(self):
        print("Konstruktor wurde aufgerufen")
       # Attribute innerhalb der Klasse
        self.dx = 0
        self.dy = 0
        self.x = 0
        self.y = 0
        self.r = 3