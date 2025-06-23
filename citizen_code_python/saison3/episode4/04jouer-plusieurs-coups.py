from robot import *
from debug import *

def jouerCoup(briques, objectif):
    placerRangee(briques)
    if briques == objectif:
        afficherMessage("Vous avez gagné !")

objectif = lireObjectif()

jouerCoup([5, 6, 1, 3, 2], objectif )
jouerCoup([2, 4, 6, 5, 3], objectif )
jouerCoup([6, 1, 2, 6, 4], objectif )
jouerCoup([1, 2, 3, 4, 5], objectif )
jouerCoup([6, 4, 3, 2, 1], objectif )