from robot import *
placerMarqueur(0)
droite()
placerMarqueur(1)
for loop in range(5):
    droite()
placerMarqueur(6)
allerAuMarqueur(0)
for x in range(9):
    prendre()
    if briqueTransportee() == 2:
        allerAuMarqueur(6 + x)
        poser()
        droite()
        placerMarqueur(7 + x)
        allerAuMarqueur(0)
    else:
        allerAuMarqueur(1 + x)
        poser()
        droite()
        placerMarqueur(2 + x)
        allerAuMarqueur(0)