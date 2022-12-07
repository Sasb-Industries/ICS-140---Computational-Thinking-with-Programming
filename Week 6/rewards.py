# Get number of books bought by user

books = int(input("Enter number of book purchsed: "))

# Calculate points earned byt user

if books >= 8:
    print("You have earned 60 points!")
elif books >= 6:
    print("You have earned 30 points!")
elif books >= 4:
    print("You have earned 15 points!")
elif books >= 2:
    print("You have earned 5 points!")
else:
    print("You have earned 0 points!")