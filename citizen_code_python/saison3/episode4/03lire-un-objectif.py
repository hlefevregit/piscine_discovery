# Partie 1

from robot import *
from debug import *

def lireRangee():
    allerLigne(1)
    rangee = []
    for colonne in range(5):
        rangee.append(briqueAttendueDansCase())
        droite()
    allerColonne(1)
    return rangee
    
rangee = lireRangee()
inverse = []
for pos in range(5):
    inverse.append(rangee[4 - pos])
placerRangee(inverse)


# Partie 2

from robot import *
from debug import *

objectif = []

def lireObjectif():
    allerColonne(13)
    descendre()
    objectif = []
    descendre()
    for iForme in range(5):
        descendre()
        objectif.append(briqueAttendueDansCase())
    return objectif
    
objectif = lireObjectif()
placerRangee(objectif)