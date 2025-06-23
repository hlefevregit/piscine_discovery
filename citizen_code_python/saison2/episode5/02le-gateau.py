from robot import *
placerMarqueur(1)
droite()
placerMarqueur(2)
for i in range (3):
    droite()
placerMarqueur(3)
for i in range (3):
    for i in range (3):
        allerAuMarqueur(1)
        prendre()
        allerAuMarqueur(2)
        poser()
        allerAuMarqueur(3)
        prendre()
        allerAuMarqueur(2)
        poser()
    droite()
    placerMarqueur(2)