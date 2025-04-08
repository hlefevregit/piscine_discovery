from robot import *
for loop in range(4):
    droite()
for x in range(4):
    for y in range(3):
        prendre()
        for z in range(4 - x):
            droite()
        poser()
        for z in range(4 - x):
            gauche()
    gauche()