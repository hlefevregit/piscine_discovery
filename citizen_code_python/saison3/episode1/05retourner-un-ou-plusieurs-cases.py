# Partie 1

from robot import *
retourner()
if briqueDuDessus() == 3:
    gauche()
    retourner()
elif briqueDuDessus() == 4:
    droite()
    retourner()

# Partie 2

from robot import *
deplacerPion()
prendre()
gauche()
poser()
droite()
if briqueDuDessus() == 3:
    gauche()
    prendre()
    droite()
    poser()
    gauche()
    retourner()
    droite()
    prendre()
    gauche()
    poser()
elif briqueDuDessus() == 4:
    droite()
    retourner()
    gauche()
    gauche()
    prendre()
    droite()
    droite()
    poser()
else:
    gauche()
    prendre()
    droite()
    poser()


