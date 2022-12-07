# for x in range(10):
#     print(x +1)

# for number in [8,6,7,5,3,0,9]:
#     if number % 2 == 0:
#         print(f'{number} is even')
#     else:
#         print(f'{number} is odd')

import turtle

al = turtle.Turtle()

x = 300

al.penup()
al.left(90)
al.forward(200)
al.right(90)
al.forward(200)
al.pendown()

for _ in range(15):
    al.right(90)
    al.forward(x)
    al.right(90)
    al.forward(x)
    x = x-20

turtle.done()