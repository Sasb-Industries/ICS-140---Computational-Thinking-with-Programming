import math
def currency(num):
    print("Your number is", "${:.2f}".format(num))
    return num

input = float(input("Please enter a number: "))

currency(input)

def circle_measurements(radius):
    area = math.pi*radius**2
    circumference = math.pi*2*radius
    return area,circumference

area, circumference = circle_measurements(5)

def calculations(num1,num2):
    sum = num1 + num2
    average = sum/2
    return sum,average

total, mean = calculations(1,2)
