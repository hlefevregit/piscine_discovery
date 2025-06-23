# Partie 1

from robot import *
retourner()
while colonneGrue() < 9 and briqueDuDessus() == 2:
    droite()
    retourner()

# Partie 2

from robot import *
def jouerCoup():
    deplacerPion()
    prendre()
    while briqueDuDessus() != 2 and sensBriqueDuDessus() == 1:
        poser()
        jouerActionCarte()
        prendre()
    poser()


jouerCoup()