from robot import *
placerMarqueur(1)
for i in range (6):
    droite()
placerMarqueur(2)
allerAuMarqueur(1)
def a ():
    prendre()
    allerAuMarqueur(2)
    poser()
    allerAuMarqueur(1)
def construire ():
    a()
    droite()
    droite()
    a()
    droite()
    a()
    for i in range (4):
        droite()
    a()
    for i in range (3):
        droite()
    a()
    
for i in range (5):
    construire()
    allerAuMarqueur(2)
    droite()
    placerMarqueur(2)
    allerAuMarqueur(1)
    