from robot import *
placerMarqueur(1)
droite()
droite()
droite()
while hauteurColonne() != 0:
    prendre()
    gauche()
    poser()
    droite()
    placerMarqueur(2)
gauche()
placerMarqueur(3)
allerAuMarqueur(1)
while hauteurColonne() !=7:
    allerAuMarqueur(3)
    prendre()
    while briqueTransportee() != briqueDuDessus():
        gauche()
    placerMarqueur(4)
    allerAuMarqueur(2)
    poser()
    allerAuMarqueur(4)
    prendre()
    allerAuMarqueur(1)
    poser()
    
    
    
 