# Innhente, analysere og presentere data

## Tegning av grafer

Plotting av grafer i Python gjøres med "pyplot", som man får tilgang til ved å importere biblioteket «matplotlib.pyplot».
Så kan man bruke funksjonen plot() og angi x- og y-verdier. Deretter må man bruke funskjonen show() for at grafen skal vises.

```python

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [10, 20, 25, 10, 12]

plt.plot(x, y)  # oppretter graf
plt.show()      # viser graf

```


### Eksperttis: En graf må være lett å lese
Det er viktig at en graf er lett å lese.
En lettlest graf kan man få til ved å legge til farger, navn på graf og navn på akser.
Det fins ferdiglagde design i python eller man kan velge selv.

```python

import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)
yverdier = xverdier**2

# Skriver ut en oversikt over tilgjengelige stiler
print(plt.style.available)

# Angir at vi vil bruke stilen "bmh"
plt.style.use("bmh")

plt.plot(xverdier, yverdier)

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.xlim(0, 20)
plt.ylim(0, 400)

plt.show()

```

### Eksperttips 2: Man kan også plotte grafer i stolpeform

```python

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

```



## Reelle datasett

Når man skal behandle datasett i python er det en fordel å ha tekstfilen lagret i samme mappe som programfila.
Ofte skjønner ikke python de særnorske bokstavene æ, ø og å, og da må man bruke encoding="utf-8" som gjør at de bokstavene blir vist frem på riktig måte.
Ved å bruke metoden read() vil alt innholdet fra en fil, bli lest inn på en gang. Og ved å bruke 'with' lukkes fila automatisk når blokka er ferdig


### Lese fra tekstfil

```python
filnavn = "MikkelRev.txt"

with open(filnavn, encoding="utf-8") as fil:
  innhold = fil.read()

print(innhold)
```

Om man vil ha mellomrom mellom linjer i en tekst kan man bruke en for-løkke for å lese inn en linje av gangen:

```python
filnavn = "MikkelRev.txt"

with open(filnavn, encoding="utf-8") as fil:
  for linje in fil:
    print(linje)
```

Om man vil fjerne mellomrommet mellom linjene igjen, kan man bruke string-metoden rstrip():

```python
filnavn = "MikkelRev.txt"

with open(filnavn, encoding="utf-8") as fil:
  for linje in fil:
    print(linje.rstrip())
```


### Skrive til fil

For å skrive til fil gjør vi mye av det samme som når vi leser fra en fil.
Vi angir et filnavn og åpner fila, men for å skrive til en fil legger vi til "w" for write. Hvis fila ikke eksisterer fra før av, blir den opprettet.

```python
filnavn = "teksten_min.txt"

tekst = "Hei, jeg liker å programmere. Nå skal jeg bruke programmering for å lagre akkurat denne teksten i en fil."

with open(filnavn, "w") as fil:
  fil.write(tekst)
```

Man kan legge til ting i filen ved å bruke "a" for append. På slutten av linjen skal man bruke \n for å få et linjeskift slik at tekstene havner på hver sin side:

```python

filnavn = "tekst_om_deg_selv.txt"

with open(filnavn, "a") as fil:
    fil.write(input("Skriv noe om deg selv: \n"))

```


### Eksperttips: Man kan hente ut enkelte ting i en CVS-fil

```python

import csv

filnavn = "Befolkning_1951-2022.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)
  print(overskrifter)

  for rad in filinnhold:
    print(rad[0]) #Her får man ut årstall, om man skriver rad[1] får man ut innbyggertallet

```
