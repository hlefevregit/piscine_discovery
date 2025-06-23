# Partie 1

from robot import *

def ramenerPion():
    placerMarqueur("A")
    for loop in range(6):
        droite()
    prendre()
    allerAuMarqueur("A")
    poser()

ramenerPion()

# Partie 2

from robot import *

def tirerAuDe():
    placerMarqueur("A")
    allerAuMarqueur("D")
    prendre()
    lacher()
    allerAuMarqueur("A")

tirerAuDe()