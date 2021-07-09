import turtle

screen = turtle.Screen()
board = turtle.Turtle()


# method to draw square
def draw():
    for i in range(4):
        board.forward(30)
        board.left(90)

    board.forward(30)


# Driver Code
if __name__ == "__main__":

    # set screen dimensions
    screen.setup(400, 500)

    # set turtle speed
    board.speed(250)

    # loops for board
    for i in range(8):


        board.up()
        # set position for every row
        board.setpos(-100, -30 * i)
        board.down()

        # row
        for j in range(8):

            # black and white colors
            if (i + j) % 2 == 0:
                color = 'black'

            else:
                color = 'white'

            # fill with color
            board.fillcolor(color)

            # start filling with color
            board.begin_fill()

            # call method
            draw()
			
            # stop filling
            board.end_fill()

    board.hideturtle()
    turtle.done()
