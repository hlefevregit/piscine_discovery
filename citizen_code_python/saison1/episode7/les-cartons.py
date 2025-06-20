from robot import *
droite()
droite()
for loop in range(7):
    prendre()
    droite()
    droite()
    if briqueTransporteeCassee():
        poser()
        gauche()
    else:
        gauche()
        poser()
    gauche()
for loop in range(4):
    droite()
    prendre()
    gauche()
    poser()