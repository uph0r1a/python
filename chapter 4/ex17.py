import turtle

turtle.penup()
turtle.backward(100)
turtle.pendown()

n = 4

angle = 180 - 180 / n
for i in range(2 * n):
    turtle.forward(200)
    turtle.right(angle)
