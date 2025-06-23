# Partie 1

from robot import *
nbPions = 0
for loop in range(7):
    descendre()
for loop in range(7):
    if lireBrique() == 8:
        nbPions = nbPions + 1
        if nbPions > 4:
            colonne = colonneGrue()
            prendre()
            allerColonne(12)
            poser()
            allerColonne(colonne)
            for loop in range(7):
                descendre()
    droite()

# Partie 2

from robot import *
def prochainJoueur():
    nbRed = 0
    nbYellow = 0
    for loop in range(7):
        for loop in range(7):
            descendre()
            if lireBrique() == 8:
                nbRed += 1
            if lireBrique() == 9:
                nbYellow += 1
        for loop in range(7):
            monter()
        droite()
    if nbRed > nbYellow:
        return 2
    else:
        return 1

joueur = prochainJoueur()
jouerCoup(joueur)
