from microbit import *
from random import randint

com_board = [[0 for i in range (5)] for j in range (5)]
while not button_a.is_pressed():
    display.scroll("Hold A to start")
    
com_board[randint(0,4)][randint(0,4)]=1
com_board[randint(0,4)][randint(0,4)]=1

display.scroll("Game start!")
sleep(200)
display.clear()

player_point = 0
current = 0
for turns in range(20):
    if player_point ==2:
        break
     x_cooard = 0
     y_cooard = 0
     while True:
         display.set_pixel(x_cooard,y_cooard,9)
         if button_a.is_pressed and button_b.is_pressed():
             if com_board[y_cooard][x_cooard] ==0:
                 display.set_pixel(x_cooard,y_cooard,2)
                 display.show(Image.SAD)
                 sleep(3000)
              else:
                  display.set_pixel(x_cooard,y_cooard,9)
                  player_point+=1
                  display.show(Image.HAPPY)
                  sleep(1000)
               break
          elif button_a.is_pressed() or button_b.is_pressed():
              display.set_pixel(x_cooard, y_cooard)
              if button_a.is_pressed():
                  x_cooard = (x_cooard + button_a.get_presses())%5
               else:
                   y_cooard = (y_cooard - button_b.get_presses())%5
               current = display.get_pixel(x_cooard, y_cooard)
if player_point == 2:
    display.show("player wins!")
else:
    display.show("computer wins!")