import matplotlib.pyplot as plotter

# Farbpunkte pro Einheit (dots per unit)
dpu = 100
offset = -5

x = [i / dpu + offset for i in range(0 * dpu, 10 * dpu)]

m_1 = 3.0
m_2 = 4
m_3 = 5

y_1 = [m_1 * i + 6 for i in x]
y_2 = [m_2 * i + 6 for i in x]
y_3 = [m_3 * i + 6 for i in x]

plotter.plot(x, y_1, label="$m = {:.1f}$".format(m_1))
plotter.plot(x, y_2, label="m = {:.1f}".format(m_2))
plotter.plot(x, y_3, label="m = {:.1f}".format(m_3))

plotter.title("Lineare Funktionen: $f(x) = y = m \dot x + t$")
plotter.xlabel("x")
plotter.ylabel("y")
plotter.legend()

plotter.show()

#Übung 1
"""Plotten Sie die Graphen einer linearen Funktion mit m = 1.0 und t_1"""