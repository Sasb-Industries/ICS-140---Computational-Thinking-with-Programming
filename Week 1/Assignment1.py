import turtle

mike = turtle.Turtle()

mike.left(90)
mike.forward(200)
mike.penup()
mike.right(90)
mike.forward(100)
mike.right(90)
mike.pendown()
mike.forward(200)
mike.penup()
mike.right(90)
mike.forward(200)
mike.right(90)
mike.forward(66)
mike.right(90)
mike.pendown()
mike.forward(300)
mike.penup()
mike.left(90)
mike.forward(68)
mike.left(90)
mike.pendown()
mike.forward(300)
mike.penup()
mike.right(90)
mike.forward(15)
mike.right(90)
mike.forward(50)

# make an X
mike.left(180)
mike.forward(25)
mike.right(135)
mike.pendown()
mike.forward(90)
mike.penup()
mike.left(135)
mike.forward(60)
mike.left(135)
mike.pendown()
mike.forward(90)
mike.penup()
mike.right(135)
mike.forward(50)

#move to other X location
mike.left(90)
mike.forward(175)
mike.left(90)

#place another X
mike.left(180)
mike.forward(25)
mike.right(135)
mike.pendown()
mike.forward(90)
mike.penup()
mike.left(135)
mike.forward(60)
mike.left(135)
mike.pendown()
mike.forward(90)
mike.penup()
mike.right(135)
mike.forward(50)

# move to a circle location
mike.right(180)
mike.forward(225)

# Draw 1st circle
mike.pendown()
mike.circle(30)
mike.penup()

# Move to another circle location
mike.left(90)
mike.forward(95)
mike.left(90)
mike.forward(110)
mike.right(180)

# Draw 2nd circle
mike.pendown()
mike.circle(30)
mike.penup()

# Move to 3rd X location
mike.right(180)
mike.forward(95)

# Draw 3rd X
mike.forward(25)
mike.right(135)
mike.pendown()
mike.forward(90)
mike.penup()
mike.left(135)
mike.forward(60)
mike.left(135)
mike.pendown()
mike.forward(90)
mike.penup()
mike.right(135)
mike.forward(50)

# Draw winners line
mike.left(90)
mike.forward(100)
mike.right(180)
mike.pendown()
mike.forward(250)

turtle.done()