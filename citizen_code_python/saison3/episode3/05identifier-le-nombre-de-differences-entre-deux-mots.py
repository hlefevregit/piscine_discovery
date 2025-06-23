# Partie 1

from robot import *
from debug import *
def nbDifferences(mot1, mot2):
    nbDiff = 0
    for pos in range(len(mot)):
        if mot1[pos] != mot2[pos]:
            nbDiff += 1
    return nbDiff

motAttendu1 = lireMotAttendu(9)
motAttendu2 = lireMotAttendu(10)
motAttendu3 = lireMotAttendu(11)

for numMot in range(3):
    ligne = 3 - numMot
    mot = lireMot(ligne)
    if nbDifferences(mot, motAttendu1) < 2:
        placerEnColonne(ligne, 9)
    elif nbDifferences(mot, motAttendu2) < 2:
        placerEnColonne(ligne, 10)
    elif nbDifferences(mot, motAttendu3) < 2:
        placerEnColonne(ligne, 11)

# Partie 2

from robot import *
from debug import *
def placerEnColonneInversee(ligneSource, colDest):
    placerGrappin(colDest, 7)
    placerProjecteur()
    for colSource in range(2, 8):
        placerGrappin(colSource, ligneSource)
        detacherObjet()
        placerGrappin(colDest, colSource - 1)
        attacherObjet()

def inverserMot(mot):
    motInverse = ""
    for pos in range(len(mot)):
        motInverse = mot[pos] + motInverse
    return motInverse

def placerMotOuInverse(ligneSource, mot, motAttendu, colonne):
    log(mot + " comparé à  " + motAttendu)
    log("inverses : " + inverserMot(motAttendu))
    if mot == motAttendu:
        placerEnColonne(ligneSource, colonne)
    elif mot == inverserMot(motAttendu):
        placerEnColonneInversee(ligneSource, colonne)

motAttendu1 = lireMotAttendu(9)
motAttendu2 = lireMotAttendu(10)
motAttendu3 = lireMotAttendu(11)

for numMot in range(3):
    ligne = 3 - numMot
    mot = lireMot(ligne)
    placerMotOuInverse(ligne, mot, motAttendu1, 9)
    placerMotOuInverse(ligne, mot, motAttendu2, 10)
    placerMotOuInverse(ligne, mot, motAttendu3, 11)