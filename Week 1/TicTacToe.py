import turtle

al = turtle.Turtle()

# Function for drawing an X
def drawX():
    al.forward(50)
    al.left(45)
    al.forward(50)
    al.right(180)
    al.pendown()
    al.forward(50)
    al.left(90)
    al.forward(50)
    al.penup()
    al.right(180)
    al.forward(50)
    al.left(90)
    al.forward(50)
    al.right(180)
    al.pendown()
    al.forward(50)
    al.left(90)
    al.forward(50)
    al.penup()
    al.right(180)
    al.forward(50)
    al.right(135)
    al.forward(50)

# Draw a circle
def drawCircle():
    al.forward(10)
    al.right(90)
    al.pendown()
    al.circle(40)
    al.penup()
    al.right(90)
    al.forward(10)



# draw grid and recenter pen

al.penup()
al.forward(50)
al.left(90)
al.pendown()
al.forward(300)
al.penup()
al.left(90)
al.forward(100)
al.left(90)
al.pendown()
al.forward(300)
al.penup()
al.right(90)
al.forward(100)
al.right(90)
al.forward(100)
al.right(90)
al.pendown()
al.forward(300)
al.penup()
al.left(90)
al.forward(100)
al.left(90)
al.pendown()
al.forward(300)
al.penup()
al.left(90)
al.forward(200)
al.left(90)
al.forward(150)
al.left(90)

# Go to first X
al.left(90)
al.forward(100)
al.right(90)

drawX()

# Return to center
al.left(90)
al.forward(100)
al.left(90)

#go to first circle
al.forward(100)

# Draw first circle
drawCircle()

# Return to center
al.forward(100)
al.right(180)

# Go to second X
al.right(90)
al.forward(100)
al.left(90)
al.forward(200)

# Draw second X
drawX()

# Return to Center
al.forward(200)
al.right(90)
al.forward(100)
al.right(90)

# Move to second circle
al.left(90)
al.forward(100)
al.right(90)
al.forward(200)

#Draw second circle
drawCircle()

#Return to Center
al.forward(200)
al.left(90)
al.forward(100)
al.left(90)

#Move to third X
al.right(90)
al.forward(100)
al.left(90)

#draw third x
drawX()

#Return to center
al.right(90)
al.forward(100)
al.right(90)

#Draw last circle
drawCircle()

#Return to center
al.right (180)

#Move to winning X
al.right(90)
al.forward(100)
al.left(90)
al.forward(100)

#Draw winning X
drawX()

#Draw Winning line
al.forward(100)
al.right(180)
al.pendown()
al.forward(300)

#return to center
al.penup()
al.right(180)
al.forward(300)
al.right(90)
al.forward(100)
al.right(90)

turtle.done()