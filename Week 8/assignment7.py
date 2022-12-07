population = float(input("Number of starting organisms : "))
increase = float(input("Daily percentage increase : "))
days = int(input("Days to multiply : "))

for x in range(days):
    print(f"Day: {x + 1}")
    population = population * (increase/100) + population
    print(f"Population: {population}")