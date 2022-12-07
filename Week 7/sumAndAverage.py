print("This program will take any numbers you input and calculate their sum and average.")
print("Please enter numbers and type in 0 when you are finished")

number = float(input("Enter a number : "))
numberOfInputs = 0
additionalNumber = 1

while additionalNumber != 0:
    additionalNumber = float(input("Enter another number : "))
    number += additionalNumber
    numberOfInputs += 1
    

print("the sum of all your numbers is: ", number)
print("the average of all your numbers is: ", number/numberOfInputs)