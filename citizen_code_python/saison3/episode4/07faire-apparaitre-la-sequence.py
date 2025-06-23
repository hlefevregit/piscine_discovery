from robot import *
from debug import *


reponse = [0, 0, 0, 0, 0]

for rangee in range(1,5):
    allerLigne(rangee)
    allerColonne(1)
    mot = []
    for col in range(5):
        mot.append(lireBrique())
        droite()
    for col in range (5):
        droite()
        if lireBrique() == 31:
            reponse[col] = mot[col]

allerLigne(5)
allerColonne(1)
for col in range(5):
    faireApparaitre(reponse[col])
    poser()
    droite()