# Promt the user to input miles driven and gallons of gas used
miles = float(input("How many miles did you drive? "))
gallons = float(input("How many gallons of gas did you use? "))

# Calculate the MPG
mpg = miles / gallons

# Print mpg to user
print("You got", format(mpg, '.3f'), "miles per gallon")