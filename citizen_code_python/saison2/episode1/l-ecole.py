from robot import *
for loop in range(5):
    droite()
placerMarqueur(6)
for x in range(5):
    for loop in range(x):
        droite()
    prendre()
    placerMarqueur(6-x)
    allerAuMarqueur(6)
    poser()
    for loop in range(x):
        gauche()
    prendre()
    placerMarqueur(6+x)
    allerAuMarqueur(6-x)
    poser()
    allerAuMarqueur(6)
    prendre()
    allerAuMarqueur(6+x)
    poser()
    allerAuMarqueur(6)
    