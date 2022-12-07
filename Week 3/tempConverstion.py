# Get user input fpr temp in celsius
celsius = float(input("Please enter a temperature in Celsius: "))

# Convert celsius to Farenheit
farenheit = ( 9 / 5 * celsius) + 32

# Display the converted value
print(format(farenheit, '.2f'))