from robot import *
droite()
droite()
droite()
for loop in range(8):
    prendre()
    if briqueTransportee() == 1:
        gauche()
        gauche()
        poser()
        droite()
        droite()
    elif briqueTransportee() == 2:
        droite()
        droite()
        poser()
        gauche()
        gauche()