packages = int(input("Enter how many packages you are buying: "))
purchase_amount = 99

if packages > 99:
    print("The discount is 40%")
    print(f"The purchase amount is ${purchase_amount * packages * .6}")
elif packages > 49:
    print("The discount is 30%")
    print(f"The purchase amount is ${purchase_amount *packages * .7}")
elif packages > 19:
    print("The discount is 20%")
    print(f"The purchase amount is ${purchase_amount * packages * .8}")
elif packages > 9:
    print("The discount is 10%")
    print(f"The purchase amount is ${purchase_amount * packages * .9}")
else:
    print(f"No discount available.")
    print(f"Your purchase price is ${purchase_amount * packages}")