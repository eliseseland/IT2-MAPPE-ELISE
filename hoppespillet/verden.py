import pygame as pg
from spiller import Spiller
from hinder import Hinder
import time

spiller1 = Spiller()
hindere = []

for i in range(3):
    nytt_hinder = Hinder()
    hindere.append(nytt_hinder)

pg.init()
VINDU_BREDDE = 500
VINDU_HØYDE = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HØYDE])


fortsett = True
while fortsett:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            forsett = False
    vindu.fill((255,255,255)) #farger bakgrunnen hvit
    # vindu.fill((rød,grønn,blå)) # andel rød, grønn og blå mellom 0-255
    for hinder in hindere:
        hinder.flytt_venstre()
        hinder.tegn(vindu)
    # pg.draw.rect(vindu, (r,g,b), (x-koordinat, y-koordinat, bredde, høyde))
    spiller1.tegn(vindu)
    # pg.draw.circle(vindu, (r,g,b), (x-koordinat, y-koordinat), radius)

    pg.display.flip() # Oppdaterer pygame-vinduet - Denne MÅ være med!
    time.sleep(1/60)


pg.quit() #avslutter pygame
print("Ferdig")