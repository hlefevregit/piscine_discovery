from robot import *
placerMarqueur(1)
for i in range (5):
    droite()
placerMarqueur(2)
allerAuMarqueur(1)
def a() :
    prendre()
    allerAuMarqueur(2)
    poser()
    allerAuMarqueur(1)
def construire() :
    allerAuMarqueur(1)
    a()
    for i in range (3):
        droite()
    a()
    droite()
    a()
    droite()
    droite()
    a()

def flm ():
    construire()
    allerAuMarqueur(2)
    droite()
    droite()
    placerMarqueur(2)
    
flm()
construire()
allerAuMarqueur(2)
for i in range (3):
    droite()
placerMarqueur(2)
construire()
allerAuMarqueur(2)
droite()
placerMarqueur(2)
construire()

