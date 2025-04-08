from robot import *
for loop in range(6):
    droite()
for x in range(4):
    droite()
    for loop in range(4 - x):
        prendre()
        for loop in range(4):
            gauche()
        poser()
        for loop in range(4):
            droite()