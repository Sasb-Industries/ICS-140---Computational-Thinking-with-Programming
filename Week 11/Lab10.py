import turtle

al = turtle.Turtle()

coordinate_list = [[120,80],[180,160],[380,140],[400,100],[340,80],[320,0],[230,-20],[200,-100],[100,-80],[40,-100],[40,-180],[20,-140],[0,-160],[-20,-140],[-40,-180],[-40,-100],[-100,-80],[-200,-100],[-230,-20],[-320,0],[-340,80],[-400,100],[-380,140],[-180,160],[-120,80],[-30,60],[-30,80],[-40,120],[-20,100],[-10,80],[10,80],[20,100],[40,120],[30,80],[30,60],[120,80]]

def draw_coordinate_list(coordinates):
    al.pendown()
    al.begin_fill()
    for coords in coordinates:
        x,y = coords
        al.goto(x,y)
    al.end_fill()

draw_coordinate_list(coordinate_list)

turtle.done()