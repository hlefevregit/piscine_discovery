# Partie 1
from robot import *
def colonneVide():
    colonne = 0
    for loop in range(7):
            if hauteurColonne() < 2:
                    colonne = colonneGrue()
            droite()
    return colonne

colonne = colonneVide()
droite()
prendre()
allerColonne(colonne)
poser()

# Partie 2

from robot import *
def jouerCoup(tour):
    allerColonne(11)
    retourner()
    prendre()
    colonne = briqueTransportee()
    droite()
    poser()
    gauche()
    gauche()
    if tour == 1:
       gauche()
    prendre()
    allerColonne(colonne)
    poser()
    return colonne

tour = 1

for loop in range(6):
    jouerCoup(tour)
    if tour == 1:
        tour = 2
    else:
        tour = 1