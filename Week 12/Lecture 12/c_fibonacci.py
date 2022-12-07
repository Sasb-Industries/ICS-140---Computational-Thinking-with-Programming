# The fibonacci sequence uses the following rules
# f(1) = 1
# f(2) = 1
# f(n) = f(n-1) + f(n-2)

# produces list: 1,1,2,3,5,8,13....
def fibonacci(n):
    if n in [1,2]:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a number for n: "))
print(f"The {n} digit in the fibonacci sequence is {fibonacci(n)}")












# def fibonacci(n):
#     if n in [1,2]:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)

# # for x in range(1,10):
# #     print(fibonacci(x))

# print(fibonacci(10))
