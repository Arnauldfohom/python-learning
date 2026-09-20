#Part 1 : Whatis Sorting? meaans arranging data according to some order.

# 1- buble Sort O(n2): the larger values bubble' (go to) toward the end

# numbers = [3, 5, 8, 1]

# for i in range (len(numbers)):
#     for j in range(len(numbers)- 1):
#         if numbers[j] > numbers[j+1]:
#             swap them

#numbers[j], numbers[j + 1] = numbers[j+1], numbers[j] swapping. a, b = b, a

# numbers = [6, 3, 8, 2]

# for j in range (len(numbers)- 1):
#     if numbers[j] > numbers[j+1]:
#         numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
# print(numbers) #print the first pass only

# for i in range(len(numbers)): #this loop repete the pass
#     for j in range(len(numbers)-1): #this loop compares neighboring element
#         if numbers[j]>numbers[j+1]:
#             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
# print(numbers) 



# def buble_sort(numbbers):
#     for i in range(len(numbers)):
#         swapped = False
#         for j in range(len(numbers)-1):
#             if numbers[j]>numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#                 swapped = True
#         if not swapped:
#             break
#     return numbers

#Optimized buble sort algorithm:

# def bubble_sort(numbers):

#     for i in range(len(numbers)):

#         swapped = False

#         for j in range(len(numbers) - 1 - i):

#             if numbers[j] > numbers[j + 1]:
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j] swap element at index j with element at index j+1
#                 swapped = True

#         if not swapped:
#             break

#     return numbers

# print(bubble_sort(numbers))

#2- Selection Sort

def selection_sort (numbers):
    for i in range (len(numbers)): #i is the position we're currently fixing
        min_index = i #assume this is the smallest
        for j in range(i+1 , len(numbers)): # search the remaining elements with j 
            if numbers[j]< numbers[min_index]: #if with find something, 
                min_index = j # we updates min_index
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i] # swap the smallest element with element at i and move to the next position.
    return numbers

numbers = [7, 4, 9, 2, 5]

print(selection_sort(numbers))


# Insertion sort- Big O is O(n²)

numbers = [5,3, 8, 1, 2]

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

    return numbers
