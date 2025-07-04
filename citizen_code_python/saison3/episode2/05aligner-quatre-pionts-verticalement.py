from robot import *

def gagneVertical(briqueCherchee, colonne):
    allerColonne(colonne)
    allerLigne(7)
    nbBriqueCherchee = 0
    descendre()
    while lireBrique() != briqueCherchee:
        descendre()
    while lireBrique() == briqueCherchee:
        descendre()
        nbBriqueCherchee += 1
    return nbBriqueCherchee == 4

colonne = jouerCoup(1)

if gagneVertical(8, colonne):
   allerColonne(9)
   prendre()
   allerColonne(8)
   poser()
