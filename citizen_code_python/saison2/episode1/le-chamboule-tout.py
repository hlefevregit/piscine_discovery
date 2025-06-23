from robot import *
placerMarqueur(1)
for i in range (5):
    droite()
placerMarqueur(2)
allerAuMarqueur(1)
for i in range (4):
    prendre()
    allerAuMarqueur(2)
    poser()
    allerAuMarqueur(1)
    prendre()
    allerAuMarqueur(2)
    droite()
    poser()
    allerAuMarqueur(1)
    prendre()
    allerAuMarqueur(2)
    droite()
    droite()
    poser()
    allerAuMarqueur(1)
    prendre()
    allerAuMarqueur(2)
    for i in range (3):
        droite()
    poser()
    allerAuMarqueur(2)
    droite()
    placerMarqueur(2)
    allerAuMarqueur(1)
    droite()
    placerMarqueur(1)
        


