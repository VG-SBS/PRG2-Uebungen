class Kunde:
    # Konstruktor
    def __init__(self, vn, nn, nu):
        print("Konstruktor Kunde wurde aufgerufen")
        #Attribute, private
        self.__vorname = vn
        self.__nachname = nn
        self.__nummer = nu

    # Methode definieren, public
    def set_vorname(self, str):
        # evtl. Fehlerbehandlung, ist str ein String?
        self.__vorname = str

    def get_vorname(self):
        return self.__vorname


    def set_nachname(self, str):
        self.__nachname = str

    def get_nachname(self):
        return self.__nachname


    def set_nummer(self, str):
        self.__nummer = str

    def get_nummer(self):
        return self.__nummer

    def get_type(self):
        return "Kunde"