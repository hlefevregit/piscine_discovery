from robot import *
from debug import *

def lettreAttendue():
    typeBrique = briqueAttendueDansCase()
    return chr(ord("A") + typeBrique - 1)

def lireMotAttendu(colonne):
    mot = ""
    placerGrappin(colonne, 8)
    placerProjecteur()
    for numLettre in range(1, 7):
        placerGrappin(colonne, 7 - numLettre)
        mot += lettreAttendue()
    return mot

motAttendu1 = lireMotAttendu(9)
motAttendu2 = lireMotAttendu(10)
motAttendu3 = lireMotAttendu(11)

for numMot in range(1, 4):
    ligne = 4 - numMot
    mot = lireMot( ligne)
    if mot == motAttendu1:
        placerEnColonne(ligne, 9)
    elif mot == motAttendu2:
        placerEnColonne(ligne, 10)
    else:
        placerEnColonne(ligne, 11)