assert 10 > 5 #10 er større enn 5, derfor gjør denne ingenting

try:
    assert 18 > 20 #18 er ikke større enn 20, derfor gir denne en feilmelding
except:
    print("Hei på deg")


# Oppgave: definer en funksjon med navn areal, som tar en høyde og en bredde og returnerer arealet av et rektangel med tilsvarende høyde og bredde
def areal(høyde, bredde):
    return høyde * bredde

def omkrets(høyde, bredde):
    return høyde + høyde + bredde + bredde #Om man for eksempel hadde glemt å skrive en bredde her hadde det vært en logisk feil fordi man trenger to bredder for å finne omkretsen

# Oppgave: test funkjsonen areal på 3 forskjellige rektangler
assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12

# Opgave: test funksjonen areal på 1 funksjon som ikke funker
#assert areal(3,4) == 13

# Oppgave: test funkjsonen omkrets på 3 forskjellige rektangler
assert omkrets(3,2) == 10
assert omkrets(3,3) == 12
assert omkrets(3,3) == 12
assert omkrets(3,4) == 14




print("koden er ferdig")