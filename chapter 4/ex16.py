import turtle

STARTING_X = -4
STARTING_Y = 4
STARTING_SIZE = 8
NUM_SQUARES = 50
STEP = 2
NUM_SIDES = 4
ANGLE = 90
ANIMATION_SPEED = 0

turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

x = STARTING_X
y = STARTING_Y
size = STARTING_SIZE

for count in range(2, 100, 2):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    for s in range(NUM_SIDES):
        turtle.forward(size)
        turtle.right(ANGLE)

    x = x - 4
    y = y + 4
    size = size + 4
turtle.done()
