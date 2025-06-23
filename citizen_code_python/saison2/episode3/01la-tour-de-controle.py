# Partie 1

from robot import *
prendre()
while hauteurColonne() == 0:
    droite()
poser()

# Partie 2

from robot import *
prendre()
while hauteurColonne() == 0:
    droite()
poser()

while hauteurColonne() != 1:
    gauche()
prendre()

while hauteurColonne() == 0:
    droite()
poser()