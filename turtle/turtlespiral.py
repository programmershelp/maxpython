import turtle

board = turtle.Turtle()
board.speed(0)
board.color("#FF0000")

side=400
board.penup()
board.goto(-200,-200) #position cursor at the bootom right of the screen
board.pendown()

#Start Spiral
for i in range (1,100):
   board.forward(side)
   board.left(90)
   side=side-4