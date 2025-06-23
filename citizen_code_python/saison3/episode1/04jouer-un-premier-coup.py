# Partie 1

from robot import *
gauche()
prendre()
lacher()
for i in range (valeurDe()):
    droite()
    retourner()

# Partie 2

from robot import *


def deplacerPion():
    gauche()
    prendre()
    lacher()
    droite()
    prendre()
    for i in range(valeurDe()):
        droite()
    droite()
    poser()
    gauche()
    retourner()
    droite()
    prendre()
    gauche()
    poser()
    
deplacerPion()
    

    