# Prompt user for rectangle area inputs
lengthOne = int(input("Please enter a length for the first rectangle : "))
widthOne = int(input("Please enter enter a width for the first rectangle : "))

lengthTwo = int(input("Please enter a length for the second rectangle : "))
widthTwo = int(input("Please enter enter a width for the second rectangle : "))

# Calculate the two areas
areaOne = lengthOne * widthOne
areaTwo = lengthTwo * widthTwo

# Output appropriate response
if areaOne > areaTwo:
    print("The first rectangle is larger")
elif areaOne < areaTwo:
    print("The second rectangle is larger")
elif areaOne == areaTwo:
    print("The two rectangles have teh same size!")
else:
    print("Error!")