from microbit import *
compass.calibrate()
#compass need to be calibrated when used

while True:
    sleep(180)
    #delay the reading by 0.1s
    needle = ((15 - compass.heading())//30)%12 # // means integer division
                                               # clock does not start from 1
    display.show(Image.ALL_CLOCKS[needle]) # image in the documentation   
    
    