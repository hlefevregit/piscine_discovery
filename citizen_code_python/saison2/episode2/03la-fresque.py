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
def base1 ():
    a()
    droite()
    a()
    droite()
    droite()
    a()
    for i in range(3):
        droite()
    a()
    
def base2 ():
    droite()
    droite()
    a()
    a()
    for i in range(3):
        droite()
    a()
    
def switch ():
    allerAuMarqueur(2)
    droite()
    placerMarqueur(2)
    allerAuMarqueur(1)

base1()
switch()
base2()
base1()
switch()
base2()
base2()
switch()
base1()
switch()
base1()
base1()

    