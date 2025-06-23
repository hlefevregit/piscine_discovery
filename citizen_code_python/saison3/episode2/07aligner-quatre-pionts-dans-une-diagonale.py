from robot import *

def gagneDiagonaleGauche(briqueCherchee, colonne):
    allerColonne(colonne)
    allerLigne(7)
    nbBriqueCherchee = 0
    descendre()
    
    while lireBrique() != briqueCherchee:
        descendre()

    while ligneGrue() > 1 and colonneGrue() > 1 and lireBrique() == briqueCherchee:
        descendre()
        gauche()

    if lireBrique() != briqueCherchee:
        monter()
        droite()

    while lireBrique() == briqueCherchee:
        nbBriqueCherchee += 1
        monter()
        droite()

    allerColonne(colonne)
    return nbBriqueCherchee == 4

def gagneDiagonaleDroite(briqueCherchee, colonne):
    allerColonne(colonne)
    allerLigne(7)
    nbBriqueCherchee = 0
    descendre()

    while lireBrique() != briqueCherchee:
        descendre()
    while ligneGrue() > 1 and lireBrique() == briqueCherchee:
        descendre()
        droite()
    if lireBrique() != briqueCherchee:
        monter()
        gauche()

    while lireBrique() == briqueCherchee and colonneGrue() > 1:
        nbBriqueCherchee += 1
        monter()
        gauche()

    allerColonne(colonne)
    return nbBriqueCherchee == 4

colonne = jouerCoup(1)

if gagneDiagonaleDroite(8, colonne) or gagneDiagonaleGauche(8, colonne):
    allerColonne(9)
    prendre()
    gauche()
    poser()