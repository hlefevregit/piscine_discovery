# Partie 1

from robot import *


def ramenerPion():
    for i in range(6):
        droite()
    prendre()
    for i in range(6):
        gauche()
    poser()
        
ramenerPion()

# Partie 2

from robot import *
placerMarqueur(1)
def tirerAuDe() :
    allerAuMarqueur("D")
    prendre()
    lacher()
    allerAuMarqueur(1)
    
tirerAuDe() 