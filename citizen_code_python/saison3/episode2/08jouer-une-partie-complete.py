from robot import *
def estGagnant(type, colonne):
    return gagneDiagonaleGauche(type, colonne) or gagneDiagonaleDroite(type, colonne) or gagneVertical(type, colonne) or gagneHorizontal(type, colonne)
gagnant = 0
joueur = 1
while gagnant == 0:
    colonne = jouerCoup(joueur)
    type = joueur + 7
    if estGagnant(type, colonne):
        gagnant = joueur
    joueur = 3 - joueur

allerColonne(9)
if gagnant == 2:
    droite()
    prendre()
    gauche()
else:
    prendre()
gauche()
poser()