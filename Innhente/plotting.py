# import matplotlib.pyplot as plt

# x = [0, 1, 2, 3, 4]
# y = [10, 20, 25, 10, 12]

# plt.plot(x, y)  # oppretter graf
# plt.show()      # viser graf



# import matplotlib.pyplot as plt
# import numpy as np

# xverdier = np.linspace(0, 20, 50)
# yverdier = xverdier**2

# # Skriver ut en oversikt over tilgjengelige stiler
# print(plt.style.available)

# # Angir at vi vil bruke stilen "bmh"
# plt.style.use("bmh")

# plt.plot(xverdier, yverdier)

# plt.xlabel("$x$")
# plt.ylabel("$y$")
# plt.xlim(0, 20)
# plt.ylim(0, 400)

# plt.show()



import matplotlib.pyplot as plt

utdanningsprogram = [
  "Kina", 
  "Japan",
  "Tyskland",
  "USA",
  "Sør-Korea",
  "India",
  "Spania",
  "Mexico",
  "Brasil",
  "England"
]

antall = [24000000, 7000000, 5000000, 4000000, 3900000, 3600000, 2300000, 1900000, 1700000, 1700000]

plt.figure(figsize=(10, 5))          # Angir dimensjoner for figure-objektet

plt.barh(utdanningsprogram, antall)  # Lager stolpediagrammet

plt.subplots_adjust(left=0.4)        # Øker plassen på venstre side av diagrammet

plt.title("Antall biler produsert av de 10 landene som produserer flest biler")

plt.grid(axis="x")                   # Legger til rutenett (bare vertikale linjer)
plt.grid(axis="y")                   # Legger til rutenett (bare horisontale linjer)

plt.show()                           # Viser diagrammet


