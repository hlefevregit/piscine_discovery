# Partie 1

from robot import *
def allerColonneAGauche(colonne):
        while colonneGrue() > colonne:
                gauche()

allerColonneAGauche(9)
prendre()
allerColonneAGauche(4)
lacher()

# Partie 2

from robot import *
def allerColonne(colonne):
    while colonneGrue() < colonne:
        droite()
    while colonneGrue() > colonne:
        gauche()

allerColonne(9)
prendre()
allerColonne(5)
lacher()