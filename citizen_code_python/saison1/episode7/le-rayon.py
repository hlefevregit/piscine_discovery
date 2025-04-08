from robot import *

for loop in range(8):
    droite()
    for loop in range(4):
        prendre()
        if briqueTransportee() == 2:
            droite()
            poser()
            gauche()
        else:
            gauche()
            poser()
            droite()
    for loop in range(2):
        gauche()
        prendre()
        droite()
        poser()
    for loop in range(2):
        droite()
        prendre()
        gauche()
        poser()
