class Kunde:
    # Konstruktor
    def __init__(self):
        print("Konstruktor Kunde wurde aufgerufen")
        #Attribute, private
        self.__vorname = ""
        self.__nachname = ""
        self.__nummer = 0

    # Methode definieren, public
    def set_vorname(self, str):
        # evtl. Fehlerbehandlung, ist str ein String?
        self.__vorname = str