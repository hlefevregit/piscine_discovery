
from robot import *
def deplacerPion():
    tirerAuDe()
    if sensBriqueDuDessus() == 1:
        prendre()
        for loop in range(valeurDe()):
            droite()
    else:
        prendre()
        for loop in range(valeurDe()):
            gauche()
    poser()
    retournerDessous()
    
deplacerPion()
jouerActionCarte()

