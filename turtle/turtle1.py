import turtle
 
board = turtle.Turtle()
board.speed(20)
board.color("blue", "red")
board.begin_fill()
 
for i in range(50):
    board.forward(300)
    board.left(170)
 
board.end_fill()
turtle.done()