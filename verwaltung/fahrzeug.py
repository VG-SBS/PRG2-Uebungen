class Fahrzeug():
    def __init__(self):
        print("Konstruktor Fahrzeug wurde aufgerufen")
        self.__farbe = ""
        self.__leistung = ""
        self.__anzahlRaeder = ""

    def set_farbe(self,str):
        self.__farbe = str

    def get_farbe(self):
        return self.__farbe

    def set_leistung(self, str):
        self.__leistung = str

    def get_leistung(self):
        return self.__leistung

    def set_anzahl_raeder(self, str):
        self.__anzahlRaeder = str

    def get_anzahl_raeder(self):
        return self.__anzahlRaeder

    def get_sound(self):
        return "brumbrum"