from robot import *
from debug import *

def afficherFeedback(formes, 
objectif ):
    allerColonne(7)
    for iForme in range(5):
        feedback = 0
        if formes[iForme] == objectif[iForme]:
            feedback = 1
        brique = feedback + 30
        faireApparaitre(brique)
        poser()
        droite()

def jouerCoup(formes, objectif):
    placerRangee(formes)
    afficherFeedback(formes, objectif)
    if formes == objectif:
        afficherMessage("Vous avez gagné !")
        
lireObjectif()
objectif = [6, 4, 3, 2, 1]
jouerCoup([5, 6, 1, 3, 2], objectif)
jouerCoup([2, 4, 6, 5, 3], objectif)
jouerCoup([6, 1, 2, 6, 4], objectif)
jouerCoup([1, 2, 3, 4, 5], objectif)
jouerCoup([6, 4, 3, 2, 1], objectif)