import turtle

print(" ")
print("This program will draw a selected shape")
print("Please look at our menu and enter the number of the chape you wish to draw")
print("1. Square")
print("2. Triangle")
print("3. Star")

selection = int(input("enter a number : "))

while selection < 1 or selection > 3:
    print("That is not a valid input")
    selection = int(input("please enter a number from our menu : "))

if selection == 1:
    al = turtle.Turtle()
    for x in range(4):
        al.forward(100)
        al.right(90)
elif selection == 2:
    al = turtle.Turtle()
    for x in range(3):
        al.forward(100)
        al.right(120)
elif selection == 3:
    al = turtle.Turtle()
    for x in range(5):
        al.forward(100)
        al.right(144)

turtle.done()