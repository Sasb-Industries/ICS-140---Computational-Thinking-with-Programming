mylist = [1,2,3,4,5]
print("This is the length", len(mylist))
print("The first item is", mylist[0])
print("The last item is",mylist[4])
mylist[0] = 6 
mylist.append(7)
# mylist.extend([8,9,10])
mylist += [8,9,10]
print(mylist)


my2list = [[1,2],[3,4],[5,6,7]]
print(my2list[2][2])
