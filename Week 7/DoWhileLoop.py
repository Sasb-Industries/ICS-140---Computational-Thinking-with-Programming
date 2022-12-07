keepGoing = "y"

while keepGoing == "y":
    sales = float(input("Enter Sales: "))
    commRate = float(input("Enter comission rate: "))
    comission = sales * commRate
    print("Your comission is: ", comission)
    keepGoing = input("Would you like to calculate another comission? (y or n)")