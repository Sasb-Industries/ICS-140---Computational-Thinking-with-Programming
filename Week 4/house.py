# ask user for size of house and colors of roof/house
size = int(input("How large would you like the house to be? : "))
square = input("What color would you like the bottom of the house to be? : ")
roof = input("What color would you like the roof to be? : ")

# Draw the desired house
import turtle

al = turtle.Turtle()

al.fillcolor(square)
al.begin_fill()
al.forward(size)
al.left(90)
al.forward(size)
al.left(90)
al.forward(size)
al.left(90)
al.forward(size)
al.end_fill()
al.penup()
al.left(180)
al.forward(size)

al.right(30)
al.pendown()
al.fillcolor(roof)
al.begin_fill()
al.forward(size)
al.right(120)
al.forward(size)
al.right(120)
al.forward(size)
al.end_fill()

turtle.done()