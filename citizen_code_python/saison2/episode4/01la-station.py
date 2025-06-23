# Partie 1

from robot import *
for loop in range(11):
    droite()
    if hauteurColonne() == 1 or hauteurColonne() == 3:
        while hauteurColonne() > 0:
            lacher()
            prendre()


# Partie 2

from robot import *
for loop in range(13):
    droite()
    if hauteurColonne() == 1 or hauteurColonne() == 3 or hauteurColonne() == 5 or hauteurColonne() == 3:
        while hauteurColonne() > 0:
            lacher()
            prendre()