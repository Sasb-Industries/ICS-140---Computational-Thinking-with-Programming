# gather user inputs

def isPrime(num):
    multiples = []
    for i in range(1, num + 1):
        if num % i == 0:
            multiples.append(i)
    if len(multiples) > 2:
        print(f"{user_input} is not a prime number, it is divisible by : {multiples}")
    else:
        print(f"{user_input} is a prime number")

user_input = int(input("Please enter a number : "))
isPrime(user_input)



# This was my first attempt

# if is_prime(user_input):
#     print(f'{user_input} is a prime number!')
# else:
#     print(f'{user_input} is NOT a prime number!')

# def is_prime(user_input):
#     if user_input == 1 or 2 or 3 or 5 or 7:
#         return True
#     else:
#         return False

