# draw hexagon using Turtle
import turtle
board = turtle.Turtle()
 
sides = 6
side_length = 70
angle = 360.0 / sides
 
for i in range(sides):
    board.forward(side_length)
    board.right(angle)
     
turtle.done()