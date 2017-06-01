from microbit import *
frame = 0
while True:
    frame+=1
    if frame %2 == 0:
        display.show(Image.COW)
        sleep(2000)
        display.clear()
    else:
        pin0.write_digital(1)
        sleep(2000)
        pin0.write_digital(0)