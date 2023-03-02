
# alder = int(input("Alder: ")) #Her får man feil hvis man skriver noe annet enn alder
# fødselsår = 2022 - alder
# print(f"Fødselsår: {fødselsår} ")

#Får en melding om hva man må skrive:
# try:
#     alder = int(input("Alder: "))
#     fødselsår = 2022 - alder
#     print(f"Fødselsår: {fødselsår} ")
# except:
#     print("Feil: alder må være et heltall")

while True:
    try:
        alder = int(input("Alder: "))
        break
    except:
        print("Feil: alder må være et heltall")
fødselsår = 2022 - alder
print(f"Fødselsår: {fødselsår} ")
        