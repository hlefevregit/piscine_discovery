from robot import *
def gagneHorizontal(briqueCherchee, colonne):
    allerColonne(colonne)
    allerLigne(7)
    prevType = 0
    nbBriqueCherchee = 0
    
    while lireBrique() == 0:
        descendre()
        
    while lireBrique() == briqueCherchee and colonneGrue() > 1:
        gauche()
        
    if lireBrique() != briqueCherchee:
        droite()
        
    nbBriqueCherchee = 0
    
    while lireBrique() == briqueCherchee:
        nbBriqueCherchee += 1
        droite()
        
    allerColonne(colonne)
    return nbBriqueCherchee == 4

colonne = jouerCoup(1)

if gagneHorizontal(8, colonne):
    allerColonne(9)
    prendre()
    gauche()
    poser()