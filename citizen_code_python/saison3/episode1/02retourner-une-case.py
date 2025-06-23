# Partie 1

from robot import *

def amenerAu9():
    retourner()
    prendre()
    for loop in range(7):
        droite()
    poser()
    for loop in range(7):
        gauche()
        
amenerAu9()
amenerAu9()

# Partie 2

from robot import *

def retournerDessous():
    prendre()
    droite()
    poser()
    gauche()
    retourner()
    droite()
    prendre()
    gauche()
    poser()

retournerDessous()
prendre()
droite()
droite()
poser()
retournerDessous()