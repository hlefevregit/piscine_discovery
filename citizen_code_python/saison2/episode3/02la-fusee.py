from robot import *
while briqueAttendue() == 0:
    droite()
for i in range (7):
    gauche()
    while hauteurColonne() == 0:
        gauche()
    prendre()
    while briqueAttendue() == 0:
        droite()
    poser() 