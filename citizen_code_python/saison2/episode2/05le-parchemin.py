from robot import *
placerMarqueur(1)
for i in range (5):
    droite()
placerMarqueur(2)
droite()
placerMarqueur(3)
droite()
placerMarqueur(4)
allerAuMarqueur(1)
def chaine ():
    prendre()
    allerAuMarqueur(2)
    poser()
    allerAuMarqueur(1)
def canard ():
    prendre()
    allerAuMarqueur(4)
    poser()
    allerAuMarqueur(1)
    
def heat ():
    prendre()
    allerAuMarqueur(3)
    poser()
    allerAuMarqueur(1)
    
    
def switch ():
    droite()
    placerMarqueur(1)

def opti ():
    chaine()
    canard()
    
heat()
chaine()
heat()
canard()
opti()
chaine()
switch()
canard()
heat()
canard()
for i in range (4):
    heat()
switch()
opti()
chaine()
for i in range (2):
    opti()
