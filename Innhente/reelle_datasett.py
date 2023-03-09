# with open("filnavn") as fil:
#   innhold = fil.read()

# print(innhold)




# filnavn = "MikkelRev.txt"

# with open(filnavn, encoding="utf-8") as fil:
#   for linje in fil:
#     print(linje)




# filnavn = "MikkelRev.txt"

# with open(filnavn, encoding="utf-8") as fil:
#   for linje in fil:
#     print(linje.rstrip())





# filnavn = "teksten_min.txt"

# tekst = "Hei, jeg liker å programmere. Nå skal jeg bruke programmering for å lagre akkurat denne teksten i en fil."

# with open(filnavn, "w") as fil:
#   fil.write(tekst)




# filnavn = "tekst_om_deg_selv.txt"

# with open(filnavn, "a") as fil:
#     fil.write(input("Skriv noe om deg selv: \n"))



import csv

filnavn = "Befolkning_1951-2022.csv"

with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)
  print(overskrifter)

  for rad in filinnhold:
    print(rad[0]) #Her får man ut årstall, om man skriver rad[1] får man ut innbyggertallet
              
