import random

guessAttempts = 1
number = random.randint(1,10)
print("I am thinking of a number between 1 and 10")
# print("Pssst! its",number) # Keep in temporarily for testing porpoises
userGuess = int(input("Please enter a guess 1 through 10 : "))

while userGuess != number:
    if userGuess > number:
        print("Too high! Please guess a lower number!")
    else:
        print("Too low! Please guess a higher number!")
    guessAttempts += 1
    userGuess = int(input("Please enter a guess 1 through 10 : "))

print("Congratulations! You guessed correctly!")
print("It only took you",guessAttempts,"attempts!")