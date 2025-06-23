from robot import *
droite()
placerMarqueur(1)
while hauteurColonne() != 0:
    droite()
gauche()
placerMarqueur(2)
while briqueAttendue() != 0:
    allerAuMarqueur(1)
    while briqueDuDessus() == 2:
        prendre()
        allerAuMarqueur(2)
        poser()
        allerAuMarqueur(1)
    droite()
    placerMarqueur(1)
    allerAuMarqueur(2)
    gauche()
    placerMarqueur(2)
    
