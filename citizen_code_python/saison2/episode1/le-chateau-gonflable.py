from robot import *
placerMarqueur("start")
for loop in range(12):
    droite()
placerMarqueur("end")
allerAuMarqueur("start")
droite()
droite()
placerMarqueur(0)
for x in range(5):
    prendre()
    allerAuMarqueur("end")
    poser()
    allerAuMarqueur(x)
    droite()
    droite()
    placerMarqueur(x + 1)