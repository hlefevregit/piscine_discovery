from robot import *
from debug import *

def placerEnColonne(ligneSource, colDest, colMot):
    placerGrappin(colDest, 7)
    placerProjecteur()
    for ligneDest in range(1, 7):
        placerGrappin(8 - ligneDest + colMot, ligneSource)
        detacherObjet()
        placerGrappin(colDest, ligneDest)
        attacherObjet()

def placerEnColonneInversee(ligneSource, colDest, colMot):
    placerGrappin(colDest, 7)
    placerProjecteur()
    for colSource in range(colMot + 2, colMot + 8):
        placerGrappin(colSource, ligneSource)
        detacherObjet()
        placerGrappin(colDest, colSource - colMot - 1)
        attacherObjet()

def lireMot(ligne, nbLettres):
    mot = ""
    for col in range(2, nbLettres + 2):
        placerGrappin(col, ligne)
        retourner()
        mot = mot + lettreAttachee()
    return mot

def inverse(mot):
    motInverse = ""
    for pos in range(len(mot)):
        motInverse = mot[pos] + motInverse
    return motInverse
def positionMotDansChaine(mot, chaine):
    for debut in range(3):
        trouve = True
        for pos in range(len(mot)):
            if mot[pos] != chaine[pos + debut]:
                trouve = False
        if trouve:
            return debut
    return -1

def placerMotOuInverse(ligneSource, chaine, motAttendu, colonne):
    posMot = positionMotDansChaine(motAttendu, chaine)
    if posMot >= 0:
        placerEnColonne(ligneSource, colonne, posMot)
        return
    posMot = positionMotDansChaine(inverse(motAttendu), chaine)
    if posMot >= 0:
        placerEnColonneInversee(ligneSource, colonne, posMot)
        return

def detruireLettresRestantes(ligne):
    for col in range(2, 10):
        placerGrappin(col, ligne)
        if lireTypeAttache() != 0:
            detacherObjet()
            detruireObjet()

    
motAttendu1 = lireMotAttendu(11)
motAttendu2 = lireMotAttendu(12)
motAttendu3 = lireMotAttendu(13)

for numMot in range(1, 4):
    ligne = 4 - numMot
    mot = lireMot(ligne, 8)
    placerMotOuInverse(ligne, mot, motAttendu1, 11)
    placerMotOuInverse(ligne, mot, motAttendu2, 12)
    placerMotOuInverse(ligne, mot, motAttendu3, 13)
    detruireLettresRestantes(ligne)