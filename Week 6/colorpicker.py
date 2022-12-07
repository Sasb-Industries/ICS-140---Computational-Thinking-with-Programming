# Gather 2 colors from the user
print("Primary colors are red, blue, and yellow")
first_primary = input("Enter a primary color: ")
second_primary = input("Enter a second primary color: ")

# Calculate the seconday color

if first_primary == second_primary:
    print("You entered the same color twice my guy!")
elif first_primary == "red":
    if second_primary =="blue":
        print("Red and blue make Purple!")
    elif second_primary =="yellow":
        print("Red and Yellow make Orange!")
elif first_primary == "yellow":
    if second_primary =="blue":
        print("Yellow and Blue make Green!")
    elif second_primary =="red":
        print("Yellow and Red make Orange!")
elif first_primary =="blue":
    if second_primary =="yellow":
        print("Blue and Yellow make Green!")
    elif second_primary =="red":
        print("Blue and Red make Purple!")
else:
    print("Error!")