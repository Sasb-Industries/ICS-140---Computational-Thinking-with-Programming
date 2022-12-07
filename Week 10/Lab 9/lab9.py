"""
ICS 140
Summer 2022
Name: Sasha Johnson

Use this file to complete Lab 9.
"""

def triangle_area(base, height):
    area = base * height * .5
    return area

def triangle_perimeter(a, b, c):
    perimeter = a + b + c
    return perimeter

def main():
    base = float(input("Enter the base of the traingle : "))
    height = float(input("Enter the height of the traingle : "))
    side2 = float(input("Enter the second side of the triangle : "))
    side3 = float(input("Enter the third side of the triangle : "))
    print(f"The area of the traingle is {triangle_area(base,height)}")
    print(f"The perimeter of the triangle is {triangle_perimeter(base,side2,side3)}")
    # The main function should prompt the user for the base, height and other 2 sides of the triangle.
    # It should print out the area and peremeter of the triangle.

if __name__ == '__main__':
    main()