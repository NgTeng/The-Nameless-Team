from microbit import *

# we need pipes
# generate pipes 
# bird
# generate bird, display bird, allow bird to fly.

#CONSTANTS - very important
# these label your values, allowing your code to be changed. Only meant to be accessed.
# named with CAPITAL LETTERS. These values are not meant to be changed. Only meant to be accessed
DELAY = 20                 # delay betwenn frames is 20ms.
FRAMES_PER_WALL_SHIFT = 20 # move the walls every 20 frames. 20x20=400ms / 0.4 seconds
FRAMES_PER_NEW_WALL = 100  # generate a new wall every 100 frames.
FRAMES_PER_SCORE = 50      # 50 frames for one point
# allows your entire program to "live" in these variables... if you change them here, you won't have to
# change every instance of the variable/every usage of this value

#global variables
y = 50     # the bird's (starting) position along the y-axis. between 0-99 inclusive (100 numbers)
speed = 0  # this is the speed of your bird ;). There will be a download acceleration, and download direction is taken as positive
score = 50 # the player's score
frame = 50

#let's go

def make_pipe():
    pipe = Image("00003:00003:00003:00003:00003") # only the last colum is lit.
    """00003
       00003
       00003
       00003
       00003
       """
    gap = random.randint(0,3)  # note that random is another module
                               # we can only go from 0-3, then make a gap two pixels wide
    pipe.set_pixel (4, gap, 0) # (x,y,brightness) --> x-postion 4 points at the column of 3's
    pipe.set_pixel (4, gap+1, 0) # we don't need to edit an entire Image string.
    return pipe
    
    pipe = make_pipe(1)
 
 # game loop
 while True:
     # game lives in this loop
     
     display.show(pipe)
     # display the pipe each time
     
     # bird
     # break free :D
     if button_a.is_pressed():
         #now we flip
         speed = -8 # --> upward is negative because downward is positive
                    # using calculations, this allows the bird to travel 1,8 pixels upward or -36 units
                    # one press
     # gravity
     speed += 1 # acceleration of 1 unit s^-2
     if speed > 2: #terminal velocity ;)
          speed = 2 # if it gets any bigger, it goes back to 2.
          
     # move the brid :|
     # the speed is the rate of change of the y value/ y coordinate
     y += speed # here, the y changes according to the speed 
     # 0 <= y <= 99
     if y > 99:
         y = 99
     if y < 0:
         y = 0 # keep it withi the display!
         
     #draw the bird.
     bird_y = int(y/20) # ignores decimal places.
     display.set_pixel(1, bird_y, 9) # at coordinate (1, bird_y) the brightness is now 9.
     # yey yor bird is now a little red dot
     
     # check for collision
     if pipe.get_pixel(1, bird_y) !=0 #get_pixel takes the coordinate and returns the brightness.
        # if the bird is inside the pipe, it's DED
        display.show(Image.SAD) # :( rip
        sleep(500)
        display.scroll("Score: " + str(score))
        break # break out of the while loop
    
     # move wall left.
     if frame % FRAMES_PER_WALL_SHIFT == 0:
         # 0, 1, 2, 3, 4... 20 --> 20%20 ==0
         pipe = pipe.shift_left(1)# another trick
                                  # shifts the image left by one pixel. There's also ones for right, up and down.
     
     # generate new pipe
     if frame % FRAMES_PER_WALL_SHIFT == 0:
         pipe = make_pipe(1)reset pipe.
     
     # increase score
     if frame % FRAMES_PER_WALL_SHIFT == 0:
         score += 1
     
     sleep(DELAY)
     frame += 1
     
     
          