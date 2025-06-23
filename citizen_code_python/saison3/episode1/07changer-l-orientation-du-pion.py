from robot import *
def deplacerPion():
    tirerAuDe()
    for loop in range(valeurDe()):
        if sensBriqueDuDessus() == 1:
            prendre()
            droite()
        else:
            prendre()
            gauche()
        poser()
        if colonneGrue() == 9:
            retourner()
        if colonneGrue() == 2:
            retourner()
    retournerDessous()
    
deplacerPion()
jouerActionCarte()

