from robot import *
for loop in range(5):
    prendre()
    for loop in range(14):
        if briqueTransportee() == briqueDuDessus():
            droite()
            poser()
            gauche()
            prendre()
            gauche()
            poser()
            droite()
            droite()
            prendre()
            gauche()
            poser()
            gauche()
            prendre()
            droite()
        droite()
    poser()
    for loop in range(14):
        gauche()