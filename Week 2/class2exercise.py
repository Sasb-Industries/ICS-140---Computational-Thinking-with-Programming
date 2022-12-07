# Get Sales Price for Meal
sales_price = float(input("What was the price of your meal? "))

# Set tax rate
tax = 0.07125

# Calculate tax cost, total price and tip amounts (15, 20, 25)
tax_cost = sales_price * tax
total_price = tax_cost + sales_price
tip15 = total_price * 0.15
tip20 = total_price * 0.2
tip25 = total_price * 0.25

# Output pretax cost, tax amount, tota price, all tip amounts
print("Sales price: $", sales_price)
print("The tax amount is: $", tax_cost)
print("The total price is: $", total_price)
print("A %15 tip is: $", tip15)
print("A %20 tip is: $", tip20)
print("A %25 tip is: $", tip25)
