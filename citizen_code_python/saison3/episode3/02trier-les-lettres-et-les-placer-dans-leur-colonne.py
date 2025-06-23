# Partie 1

from robot import *
from debug import *
def lettreAttachee():
    typeBrique = lireTypeAttache()
    return chr(ord("A") + typeBrique - 1)

lettresPosees = 0

for colonne in range(2, 8):
        placerGrappin(colonne, 1)
        lettre = lettreAttachee()
        detacherObjet()
        if lettre == "A":
            placerGrappin(9, lettresPosees + 1)
            lettresPosees += 1
        attacherObjet()


# Partie 2

from robot import *
from debug import *
def lettreAttachee():
    typeBrique = lireTypeAttache()
    return chr(ord("A") + typeBrique - 1)

for colonne in range(2, 8):
    for ligne in range(1, 4):
	    placerGrappin(colonne, ligne)
	    lettre = lettreAttachee()
	    if lettre == "A":
		    colDest = 9
		elif lettre == "D":
		    colDest = 10
		else:
		    colDest = 11
		detacherObjet()
		placerGrappin(colDest, 1)
		while lireTypeAttache() != 0:
		    monter()
		attacherObjet()