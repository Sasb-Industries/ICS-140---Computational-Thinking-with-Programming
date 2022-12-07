numbers = []

for x in range(5):
    numbers.append(x+1)

numbers.append(6)

numbers.insert(0,0)

print(numbers)

number = [3,1,4] * 2
print(number)

heroes = ["superman", "wonder woman", "batman"]
heroes.sort()
for hero in heroes:
    print(hero)

range_list = list(range(2,11,2))
print(range_list)
print(len(range_list))

marvel = ["Ant Man", "Black Panther", "Captain Marvel"]
dc = ["superman", "wonder woman", "batman"]
mixed_heroes = marvel + dc
mixed_heroes.sort()
print(mixed_heroes)

avengers = ["Captain America", "Iron Man", "Hulk", "Thor", "Black Widow", "Hawkeye"]
sliced_list = avengers[2:5]
print(sliced_list)

if "Black Panther" in avengers:
    print("It is")
else:
    print("it is not")

avengers += marvel

print(avengers)

avengers.append("Spiderman")

i = avengers.index("Thor")+1

avengers.insert(i, "Loki")
print(avengers)
avengers.remove("Loki")
print(avengers)

marvel_characters = [["Thor", "Loki", "Odin"], ["Hawkeye", "Black Widow"], ["Captain America", "Bucky"]]

print(marvel_characters[0])

print(marvel_characters[1][1])

marvel_characters[2][0] = "falcon"
print(marvel_characters)

for heros in marvel_characters:
    for hero in heros:
        print(hero)