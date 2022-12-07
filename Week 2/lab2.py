import turtle

# Establish variables for inputs
square_size = int(input("Please enter a square size: "))
square_color = input("Please enter a square color: ")

#d Draw square
al = turtle.Turtle()

al.color(square_color)
al.forward(square_size)
al.left(90)
al.forward(square_size)
al.left(90)
al.forward(square_size)
al.left(90)
al.forward(square_size)

turtle.done()