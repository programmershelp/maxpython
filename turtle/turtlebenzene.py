import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
board = turtle.Pen()
turtle.bgcolor('black')
turtle.speed(200)

for x in range(360):
    board.pencolor(colors[x%6])
    board.width(x/100 + 1)
    board.forward(x)
    board.left(59)