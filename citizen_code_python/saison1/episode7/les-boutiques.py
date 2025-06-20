from robot import *
prendre()
for loop in range(13):
    droite()
    if briqueDuDessusCassee():
        lacher()
        prendre()