# ask user for prices of breakfast, lunch, and dinner

breakfast = float(input("How much did your breakfast cost? : $"))
lunch = float(input("How much did your lunch cost? : $"))
dinner = float(input("How much did your dinner cost? : $"))

# Calculate daily total and avg cost per meal

total = breakfast + lunch + dinner
average = total / 3

# Output the total cost and average cost per meal to the user
print(f"Your total spending for the day was ${round(total, 2)}")
print(f"Your total spending for the day was ${round(average, 2)}")