from robot import *
droite()
if briqueDuDessus() == 2:
    prendre()
    droite()
    poser()
    gauche()
droite()
droite()
if briqueDuDessus() == 1:
    prendre()
    gauche()
    poser()