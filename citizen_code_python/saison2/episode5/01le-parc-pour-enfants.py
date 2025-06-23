from robot import *
droite()
placerMarqueur(1)
for i in range (9):
    droite()
placerMarqueur(2)
for i in range (3):
    allerAuMarqueur(1)
    for i in range (3):
        prendre()
        allerAuMarqueur(2)
        poser()
        allerAuMarqueur(1)
        droite()
        placerMarqueur(1)
    allerAuMarqueur(2)
    droite()
    placerMarqueur(2)