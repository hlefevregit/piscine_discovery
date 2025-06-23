from robot import *
from debug import *

def faireApparaitre(valeur):
    colonne = colonneGrue()
    allerColonne(7 + valeur)
    prendre()
    allerColonne(colonne)
    
faireApparaitre(3)
poser()
droite()
faireApparaitre(1)
poser()
droite()
faireApparaitre(4)
poser()
droite()
faireApparaitre(2)
poser()
droite()
faireApparaitre(6)
poser()
droite()