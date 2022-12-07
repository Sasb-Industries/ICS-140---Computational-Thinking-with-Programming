import random, time

"""
Lab 11 - Rewrite the pseudocode as a python function.
It should receive an unsorted list and return a sorted list.
The function must use the selection sort algorithm.
"""

def selection_sort(mylist):
    index1 = 0
    length = len(mylist)
    while index1 < length - 1:
        smallest = mylist[0]
        index2 = index1 + 1
        while index2 < length:
            if smallest > mylist[1]:
                smallest = mylist[1]
                smallestPosition = index2
                smallestPosition, index1 = index1, smallestPosition
#                swap the elements of mylist at smallestPosition and index1
            index2 = index2 + 1
        index1 = index1 + 1
    return mylist



"""
Lab 11 - Rewrite the pseudocode as a python function.
It should receive an unsorted list and return a sorted list.
The function must use the insertion sort algorithm.
"""

def insertion_sort(mylist):
    length = len(mylist)
    for index1 in range(length -1):
        next = mylist[index1 + 1]
        location = -1
        found = False
        index2 = index1
        while not found and index2 >= 0:
            if next >= mylist[index2]:
                found = True
                location = index2
            index2 = index2 - 1
        for index2 in range(index1 + 1, location): # from index1 + 1 to location by -1
            mylist[index2] = mylist[index2 - 1]
        mylist[location + 1] = next
    return mylist





"""
Assignment 11 - Rewrite the pseudocode as a python function.
It should receive an unsorted list and return a sorted list.
The function must use the bubble sort algorithm.
"""

def bubble_sort(mylist):
    length = len(mylist)
    swapped = True
    while swapped:
        swapped = False
        for index in range(1,length): # from 1 through length - 1 # <- remove the -1
            if mylist[index - 1] > mylist[index]:
                mylist[index - 1], mylist[index] = mylist[index], mylist[index - 1]# swap the entries of mylist at index - 1 and index
                swapped = True
    return mylist



def create_unsorted_list(size):
    # Creates a random list of integers to sort
    random_list=[]
    for _ in range(size):
        random_list.append(random.randint(1,size))
    return random_list

def print_list(mylist):
    # Checks the size of list and prints if not too long
    if len(mylist) <= 100:
        print(mylist)


def test_algorithm(sort_function, description, random_list):
    list_to_sort = []
    list_to_sort += random_list
    print(f"starting {description}...")
    start = time.perf_counter_ns()
    sorted_list = sort_function(list_to_sort)
    end = time.perf_counter_ns()
    processing_time = end - start
    print(f"{description} finished in {processing_time:,d} nanoseconds.")




def main():
    size = int(input("How large of a list should we sort? "))
    random_list = create_unsorted_list(size)
    print_list(random_list)
    test_algorithm(selection_sort,"selection sort", random_list)
    test_algorithm(insertion_sort,"insertion sort",random_list)
    test_algorithm(bubble_sort,"bubble sort", random_list)

if __name__ == '__main__':
    main()