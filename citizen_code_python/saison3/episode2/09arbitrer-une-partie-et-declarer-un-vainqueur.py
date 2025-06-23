from robot import *
def estGagnant(type, colonne):
    return gagneDiagonaleGauche(type, colonne) or gagneDiagonaleDroite(type, colonne) or gagneVertical(type, colonne) or gagneHorizontal(type, colonne)

allerColonne(9)
prendre()

colonne = 1
for loop in range(7):
    allerColonne(colonne)
    lacher()
    type = 8
    if estGagnant(type, colonne):
        colonneGagnante = colonne
    prendre()
    colonne += 1

allerColonne(colonneGagnante)
lacher()