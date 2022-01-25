from verwaltung.fahrzeug import Fahrzeug

class Auto(Fahrzeug):
    def __init__(self):
        print("Konstruktor Auto aufgerufen")
        super().__init__()
        self.__farbe = ""
        self.__leistung = ""
        self.__anzahlRaeder = ""
        self.__anzahl_tueren = 0
        self.__anzahl_scheiben = 0

    def set_anzahl_tueren(self,nr):
        self.__anzahl_tueren = nr

    def get_anzahl_tueren(self):
        return self.__anzahl_tueren

    def set_anzahl_scheiben(self,nr):
        self.__anzahl_scheiben = nr

    def get_anzahl_scheiben(self):
        return self.__anzahl_scheiben


class Motorrad(Fahrzeug):
    print("Konstruktor Motorrad aufgerufen")
    def __init__(self):
        super().__init__()

    def get_sound(self):
        return "bruuuuum"