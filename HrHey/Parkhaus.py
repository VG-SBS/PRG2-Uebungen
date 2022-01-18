parkhaus_ebene_1 = [[True] * 75, [True] * 75, [True] * 75, [True] * 75]

def einparken(ebene,reihe,position):

    if reihe < 0:
        raise IndexError("Reihe: Index zu klein")
    elif reihe >= len(ebene):
       raise IndexError("Reihe: Index zu Groß")

    if position <0:
        raise IndexError("Nummer: Index zu klein")
    elif position >= len(ebene[reihe]):
       raise IndexError("Nummer: Index zu Groß")

    if ebene[reihe][position] == True:
        ebene[reihe][position] = False
    else:
        print("Dieser Platz ist bereits belegt")

def ausparken(ebene,reihe,position):

    if reihe <0:
        raise IndexError("Reihe: Index zu klein")
    elif reihe >= len(ebene):
       raise IndexError("Reihe: Index zu Groß")

    if position <0:
        raise IndexError("Nummer: Index zu klein")
    elif position >= len(ebene[reihe]):
       raise IndexError("Nummer: Index zu Groß")

    if ebene[reihe][position] == False:
        ebene[reihe][position] = True
    else:
        print("Hier steht kein Auto...")

einparken(parkhaus_ebene_1,3,20)
einparken(parkhaus_ebene_1,1,22)
einparken(parkhaus_ebene_1,2,23)
einparken(parkhaus_ebene_1,1,26)
einparken(parkhaus_ebene_1,3,18)
einparken(parkhaus_ebene_1,0,10)

print(parkhaus_ebene_1[0].count(True), "Plätze in Reihe 1 sind noch frei")
print(parkhaus_ebene_1[1].count(True), "Plätze in Reihe 2 sind noch frei")
print(parkhaus_ebene_1[2].count(True), "Plätze in Reihe 3 sind noch frei")
print(parkhaus_ebene_1[3].count(True), "Plätze in Reihe 4 sind noch frei")

print("Insgesamt sind noch", parkhaus_ebene_1[0].count(True) + parkhaus_ebene_1[1].count(True) + parkhaus_ebene_1[2].count(True) + parkhaus_ebene_1[3].count(True), "Plätze auf Ebene 1 frei")
