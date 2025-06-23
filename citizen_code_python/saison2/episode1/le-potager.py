from robot import *
placerMarqueur(1)
for i in range (7):
    droite()
placerMarqueur(2)
allerAuMarqueur(1)
for i in range (50):
    if hauteurColonne() > 0:
        droite()
    else:
        placerMarqueur(2)
        for i in range (4):
            allerAuMarqueur(1)
            prendre()
            allerAuMarqueur(2)
            poser()
        allerAuMarqueur(1)
        droite()
        placerMarqueur(1)
    
    