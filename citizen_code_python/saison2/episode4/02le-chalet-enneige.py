from robot import *
for i in range(13):
    droite()
    while briqueDuDessus() == 1 and hauteurColonne() > 4:
            lacher()
            prendre()