# Vern mot kjøretøysfeil og logiske feil i prograemmet

## Kjøretidsfeil

Håndtering av kjøretidsfeil i Python gjøres med nøkkelordene try og excpt
Python forsøker å kjøre kodeblokken som ligger under 'try:', hvis python får en feilmelsing, vil den kjøre kodeblokken som ligger under 'except:'.

```python
while True:
try:
    alder = int(input("Alder: "))
    fødselsår = 2022 - alder
    print(f"Fødselsår: {fødselsår} ")   
except:
    print("Feil: alder må være et heltall)

print("Koden fortsetter)
    

```


### Ekseperttips: while-løkke med try-except

```python
while True:
try:
    alder = int(input("Alder: "))
    assert alder >= 0
    break
except:
    print("Feil: alder må være et heltall")
fødselsår = 2022 - alder
print(f"Fødselsår: {fødselsår} ")
```


## LOgiske feil i programmer

For å oppdage logiske feil i python-programmet kan vi bruke nøkkelordet 'assert' for å forsikre oss om at koden gir korrekte resultat.

Eksempel:

```python
assert 10 > 5 #10 er større enn 5, derfor gjør denne ingenting
assert 18 > 20 #18 er ikke større enn 20, derfor gir denne en feilmelding
```

Eksempel: test av funksjoner med assert

```python
def areal(høyde, bredde):
    return høyde * bredde

def omkrets(høyde, bredde):
    return høyde + høyde + bredde + bredde #Om man for eksempel hadde glemt å skrive en bredde her hadde det vært en logisk feil fordi man trenger to bredder for å finne omkretsen


assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12
assert omkrets(3,2) == 10
assert omkrets(3,3) == 12
assert omkrets(3,3) == 12
assert omkrets(3,4) == 14
```

## Eksperttips: Håndtering av kjøretidsfeil og logisk feil

```python
while True:
    try:
        alder = int(input("Alder: "))
        assert alder >= 0
        break
    except:
        print("Alder må være et positivt heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")
```


