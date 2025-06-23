# Partie 1

from robot import *

retourner()
if briqueDuDessus() == 3:
    gauche()
else:
    droite()
retourner()

# Partie 2

from robot import *

def jouerActionCarte():
    prendre()
    if briqueDuDessus() == 3:
        gauche()
        poser()
        retournerDessous()
    elif briqueDuDessus() == 4:
        droite()
        poser()
        retournerDessous()
    else:
        poser()
deplacerPion()
jouerActionCarte()