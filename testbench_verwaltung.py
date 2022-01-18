from verwaltung import Kunde

kunde_a = Kunde()

# nicht so!!!
#kunde_a.__vorname = "Hans"

#sondern so:
kunde_a.set_vorname("Hans")
kunde_a.set_nachname("Müller")
kunde_a.set_nummer(2)

# Ausgabe mit get_Funktion
print(kunde_a.get_vorname())
print(kunde_a.get_nachname())
print(kunde_a.get_nummer())
