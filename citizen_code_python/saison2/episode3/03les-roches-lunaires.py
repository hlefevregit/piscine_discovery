from robot import *
while hauteurColonne() == 2:
    prendre()
    while hauteurColonne() != 0 :
        droite()
    droite()
    while hauteurColonne() > 1 :
        droite()
    poser()
    while hauteurColonne() != 1:
        gauche()
    droite()
