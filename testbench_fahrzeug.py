from verwaltung import Fahrzeug
from verwaltung import Auto
from verwaltung import Motorrad

fahrzeug_a = Fahrzeug()
auto_a = Auto()
motorrad_a = Motorrad()

auto_a.set_farbe("rot")
auto_a.set_leistung("45PS")
auto_a.set_anzahl_raeder("4")
auto_a.set_anzahl_tueren("5")
auto_a.set_anzahl_scheiben("6")

print(auto_a.get_farbe())
print(auto_a.get_leistung())
print(auto_a.get_anzahl_raeder())
print(auto_a.get_anzahl_tueren())
print(auto_a.get_anzahl_scheiben())