from robot import *
for loop in range(2):
    droite()
    for loop in range(5):
        prendre()
        for loop in range(3):
            droite()
        if (briqueTransportee() == briqueDuDessus()):
            poser()
        else:
            droite()
            poser()
            gauche()
        for loop in range(3):
            gauche()
for loop in range(4):
    droite()
for loop in range(2):
    prendre()
    gauche()
    gauche()
    poser()
    droite()
    droite()