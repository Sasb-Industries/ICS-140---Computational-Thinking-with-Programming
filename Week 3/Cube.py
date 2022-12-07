print(format(.75,'.0%'))
length = int(input("Please enter how long you want the sides of your cube to be: "))

import turtle
al = turtle.Turtle()

for x in range(0,4):
    al.forward(length)
    al.left(90)

al.penup()
al.left(90)
al.forward(length)
al.right(45)
al.pendown()
al.forward(length)
al.right(45)
al.forward(length)
al.right(90)
al.forward(length)
al.right(45)
al.forward(length)

turtle.done()