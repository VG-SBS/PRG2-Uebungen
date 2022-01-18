from verwaltung import Kunde

kunde_a = Kunde()

# nicht so!!!
#kunde_a.__vorname = "Hans"

#sondern so:
kunde_a.set_vorname("Hans")
