from robot import *
placerMarqueur(1)
droite()
droite()
droite()
placerMarqueur(2)
while hauteurColonne() != 0:
    while hauteurColonne() != 1:
        prendre()
        gauche()
        poser()
        droite()
    prendre()
    allerAuMarqueur(1)
    poser()
    allerAuMarqueur(2)
    droite()
    placerMarqueur(2)
gauche()
gauche()
placerMarqueur(2)
while hauteurColonne() != 0:
    while hauteurColonne() != 0:
        prendre()
        droite()
        poser()
        gauche()
    allerAuMarqueur(2)
    gauche()
    placerMarqueur(2)
        