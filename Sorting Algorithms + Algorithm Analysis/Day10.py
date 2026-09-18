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
    for i in range (len(numbers)):
        min_index = i 
        for j in range(i+1 , len(numbers)):
            if numbers[j]< numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

numbers = [7, 4, 9, 2, 5]

print(selection_sort(numbers))