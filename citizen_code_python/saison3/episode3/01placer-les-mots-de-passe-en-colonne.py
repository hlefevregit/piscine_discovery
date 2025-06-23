# Partie 1

from robot import *
from debug import *

def placerGrappin(colonne, ligne):
    while colonneGrue() < colonne:
            droite()
    while colonneGrue() > colonne:
            gauche()
    while ligneGrue() < ligne:
            monter()
    while ligneGrue() > ligne:
            descendre()

for ligne in range(1, 7):
    placerGrappin(8 - ligne, 1)
    detacherObjet()
    placerGrappin(9, ligne)
    attacherObjet()


# Partie 2

from robot import *
from debug import *

def placeGrappin(colonne, ligne):
	while colonneGrue() < colonne:
		droite()
	while colonneGrue() > colonne:
		gauche()
	while ligneGrue() < ligne:
		monter()
	while ligneGrue() > ligne:
		descendre()

def placerLigneEnColonne(ligneSource, colDest):
    for ligne in range(1, 7):
        placeGrappin(8 - ligne, ligneSource)
        detacherObjet()
        placeGrappin(colDest, ligne)
        attacherObjet()
        
placerLigneEnColonne(3, 10)
placerLigneEnColonne(2, 11)
placerLigneEnColonne(1, 9)