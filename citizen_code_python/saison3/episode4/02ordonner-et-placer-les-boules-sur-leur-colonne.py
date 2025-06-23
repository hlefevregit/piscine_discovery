# Partie 1

from robot import *
from debug import *

def placerLettres(colonneSource, destination):
    for pos in range(6):
        allerColonne(colonneSource[pos])
        prendre()
        allerColonne(desitnation)
        poser()
    
placerLettres([2, 5, 7, 8, 10, 11], 14)
placerLettres([1, 3, 4, 6, 9, 12], 13)

# Partie 2

from robot import *
from debug import *

def placeRangee(briques):
    allerColonne(1)
    for iBrique in range (5):
        faireApparaitre(briques[iBrique])
        poser()
        droite()
        
placeRangee([3, 1, 4, 2, 6])
placeRangee([4, 2, 6, 6, 1])
placeRangee([2, 2, 5, 1, 3])
placeRangee([4, 3, 1, 2, 4])
