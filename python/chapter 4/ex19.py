import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(3)

side = 80
sides = 8
angle = 360 / sides

t.penup()
t.goto(-side / 2, side / 2)
t.setheading(0)
t.pendown()

for i in range(sides):
    t.forward(side)
    t.right(angle)

t.penup()
t.goto(0, -70)
t.pendown()
t.write("STOP", align="center", font=("Arial", 24, "bold"))

turtle.done()
