from verwaltung.kunde import Kunde

class VIPKunde(Kunde):

    def __init__(self, vn, nn, nu, ba):
        print("Konstruktor VIP Kunde wurde aufgerufen")
        super(VIPKunde, self).__init__(vn,nn,nu)
        self.__bearbeiter = ba

    def set_bearbeiter(self, str):
        self.__bearbeiter = str

    def get_bearbeiter(self):
        return self.__bearbeiter

    #Methode der Elternklasse kann überschrieben werden!
    def get_type(self):
        return "VIPKunde"