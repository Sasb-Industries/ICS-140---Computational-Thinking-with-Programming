number = int(input("Input a number 0-36: "))

while number > 36 or number < 0:
    print("Invalid input, please make sure the number is 0-36")
    number = int(input("Input a number 0-36: "))

if number == 0:
    print("Pocket is green")
elif 0 < number < 11:
    if number % 2 == 0:
        print("Pocket is black")
    else:
        print("Pocket is red")
elif 10 < number < 19:
    if number % 2 == 0:
        print("Pocket is red")
    else:
        print("Pocket is black")
elif 18 < number < 29:
    if number % 2 == 0:
        print("Pocket is black")
    else:
        print("Pocket is red")
elif 28 < number < 37:
    if number % 2 == 0:
        print("Pocket is red")
    else:
        print("Pocket is black")
else:
    print("ERROR")