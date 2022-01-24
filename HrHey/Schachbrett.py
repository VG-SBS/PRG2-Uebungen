schachbrett = [["leer"]*8, ["BauerS"] * 8,["leer"]*8,["leer"]*8,["leer"]*8,["leer"]*8,["BauerW"]*8,["leer"]*8, ]

schachbrett[0][0] = "TurmS"
schachbrett[0][7] = "TurmS"
schachbrett[7][0] = "TurmW"
schachbrett[7][7] = "TurmW"

schachbrett[0][1] = "SpringerS"
schachbrett[0][6] = "SpringerS"
schachbrett[7][1] = "SpringerW"
schachbrett[7][6] = "SpringerW"

schachbrett[0][2] = "LäuferS"
schachbrett[0][5] = "LäuferS"
schachbrett[7][2] = "LäuferW"
schachbrett[7][5] = "LäuferW"

schachbrett[0][3] = "DameS"
schachbrett[0][4] = "KönigS"
schachbrett[7][3] = "DameW"
schachbrett[7][4] = "KönigW"

def bauer(zeile,spalte):
   try:
       # innerhalb des Index?
        if zeile > len(schachbrett) or zeile < 0:
            print("test")
            raise IndexError("Out of Index!!")
        else:

            #Figur vorhanden?
            if schachbrett[zeile][spalte] == "leer" or schachbrett[zeile][spalte].startswith("Bauer") != True:
                raise EnvironmentError("Hier befindet sich kein Bauer")
            else:

                #Wieviele Felder
                    x = int(input("Wollen Sie den Bauern 1 oder 2 Felder bewegen?"))
                    #Schwarzer Bauer?
                    if schachbrett[zeile][spalte].endswith("S") == True:
                        #Zielfeld belegt?
                        if schachbrett[zeile+x][spalte] != "leer":
                            raise ValueError("Hier steht bereits eine Figur")
                        #Zielfeld nicht belegt?
                        else:
                            schachbrett[zeile + x][spalte] = "BauerS"
                            schachbrett[zeile][spalte] = "leer"
                    #Weißer Bauer?
                    elif schachbrett[zeile][spalte].endswith("W") == True:
                        #Zielfeld belegt?
                        if schachbrett[zeile - x][spalte] != "leer":
                            raise ValueError("Hier steht bereits eine Figur")
                        #Zielfeld nicht belegt?
                        else:
                            schachbrett[zeile][spalte] = "leer"
                            schachbrett[zeile - x][spalte] = "BauerW"
    # Fehlerausgabe
   except IndexError as err:
       print(err)
   except EnvironmentError as err:
       print(err)
   except ValueError as err:
       print(err)

#Funktionsaufruf
bauer(1,3)
for i in range(len(schachbrett[0])):
    print(schachbrett[i])