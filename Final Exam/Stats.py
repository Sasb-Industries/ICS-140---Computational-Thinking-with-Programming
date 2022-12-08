import random


def main():
    list_length = get_input()
    generated_list = generate_list(list_length)
    total = get_total(generated_list)
    average = get_average(generated_list)
    sorted_list, median = get_median(generated_list)
    print(f"Your generated list is : {generated_list}")
    print(f"That list sorted is this : {sorted_list}")
    print(f"Total of your list is {total}")
    print(f"The average of your list is {average}")
    print(f"The median of your list is {median}")

def get_input():
    size = int(input("Please enter a number 1 - 20 : "))
    while size < 1 or size > 20:
        size = int(input("Invalid input. Please enter a number 1 - 20 : "))
    return size

def generate_list(length):
    list = []
    for _ in range(length):
        list.append(random.randint(1,30))
    return list

def get_total(list):
    total = 0
    for item in list:
        total += item
    return total

def get_average(list):
    total = get_total(list)
    average = total / len(list)
    return average

def get_median(list):
    sorted_list = []
    sorted_list += list
    sorted_list = sort_list(sorted_list)
    if len(list) % 2 == 1:
        median = sorted_list[len(list)//2]
    else:
        lower_number = sorted_list[int((len(sorted_list)/2) - 1)]
        higher_number = sorted_list[int((len(sorted_list)/2))]
        median = (lower_number + higher_number) / 2
    return sorted_list, median

# I just copied this from the lab I did two weeks ago so don't sue me !
def sort_list(mylist):
    length = len(mylist)
    swapped = True
    while swapped:
        swapped = False
        for index in range(1,length):
            if mylist[index - 1] > mylist[index]:
                mylist[index - 1], mylist[index] = mylist[index], mylist[index - 1]
                swapped = True
    return mylist

main()