from robot import *
for i in range (3):
    placerMarqueur(i+1)
    droite()
droite()
droite()
placerMarqueur(4)
for i in range (4):
    for i in range (3):
        prendre()
        if briqueTransportee() == 1:
            allerAuMarqueur(1)
            poser()
            allerAuMarqueur(4)
        elif briqueTransportee() == 2:
            allerAuMarqueur(2)
            poser()
            allerAuMarqueur(4)
        else:
            allerAuMarqueur(3)
            poser()
            allerAuMarqueur(4)
    droite()
    placerMarqueur(4)
    