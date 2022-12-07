# Gather inputs from user:
#   1. Principal originally deposited
#   2. annual interst rate
#   3. number of times the interest is compounded
#   4. number of years the account will accrue interest

p = float(input("How much money did you orginially deposit? : "))
r = float(input("What is the annual interest rate? : "))
n = float(input("How many times per year is the interest compunded? : "))
t = float(input("How many years will you let the account accrue interst? : "))

# calculate total

total = p * ((1 + r/n)**(n * t))

#print 
print(f"You now have ${round(total, 2)} in your account")