# factorial is calculated as the following:
# f(1) = 1
# f(n) = n * f(n-1)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Enter a number for n: "))
print(f"The factorial of {n} is {factorial(n)}")
