from robot import *

for i in range (9):
    droite()
    placerMarqueur(1)
    for i in range (4):
        prendre()
        if briqueTransporteeCassee():
            allerAuMarqueur("A")
            poser()
            allerAuMarqueur(1)
        else:
            droite()
            poser()
            gauche()
    for i in range (3):
        droite()
        prendre()
        gauche()
        poser()