from robot import *
for loop in range(14):
    droite()
    if hauteurColonne() == 3:
        prendre()
    if hauteurColonne() == 1:
        poser()
