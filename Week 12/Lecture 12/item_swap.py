# swapping variables
# x,y = 1,2



# x = 1
# y = 2
# print("x is",x)
# print("y is",y)

# generalized technique using a temp variable.
# temp = x
# x = y
# y = temp

# print("x is",x)
# print("y is",y)
# python-specific technique to simultaneously swap values
# x,y = y,x

# print("x is",x)
# print("y is",y)

# Now let's try the same thing with a list
# swap mylist[0] and mylist[1]
mylist = [2,1,3]
print(mylist)


# general techinqe using a temp variable.

# temp = mylist[0]
# mylist[0] = mylist[1]
# mylist[1] = temp
# print(mylist)


# python-specific technique to simultaneously swap values
mylist[0],mylist[1] = mylist[1],mylist[0]
print(mylist)

