from robot import *
from debug import *

def placeLigneEnColonne(ligneSource, colDest):
    for ligneDest in range(1, 7):
        placerGrappin(8 - ligneDest, ligneSource)
        detacherObjet()
        placerGrappin(colDest, ligneDest)
        attacherObjet()

def detruireLettres(ligneSource):
    for ligneDest in range(1, 7):
        placerGrappin(8 - ligneDest, ligneSource)
        detacherObjet()
        detruireObjet()

def lireMot(ligne):
    mot = ""
    for col in range(2, 8):
        placerGrappin(col, ligne)
        retourner()
        mot = mot + lettreAttachee()
    return mot

for pos in range(4):
    droite()
    
motAttendu = "FACHEE"

for ligne in range(1, 4):
    mot = lireMot(4 - ligne)     
    if mot == motAttendu:
        placeLigneEnColonne(4 - ligne, 11)
    else:
	    detruireLettres(4 - ligne)