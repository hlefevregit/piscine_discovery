from robot import *
while hauteurColonne() != 1:
    prendre()
    droite()
    while hauteurColonne() == 0:
        droite()
    poser()
    gauche()
    while hauteurColonne() == 0:
        gauche()
    