# Searching 
#linear Search : limited for a large amount of data.

# numbers = [4, 8, 15, 16, 23, 42]

# def linear_search(numbers, target):
#     for number in numbers:
#         if number == target:
#             return True
#     return False

# print(linear_search(numbers , 99))    

# Big O : describes how an algorithm's work grows as the amount of data increases.
# For linear search O(n) where n  represents the number of element.
#O(1): complexity equal to 1 : no change as the number of element grows

# def find_index(numbers, target):

#     for index, number in enumerate(numbers): # give me both position and value.
#         if number == target:
#             return index           
        
#     return -1 

# print(find_index(numbers , 16))    


# Part2: Binary search O(log n) : works on a sorted list. it impies that at every step, eliminate half of the remaining search space.

numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45]

# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1

#     while left <= right:
#         middle = (left + right)//2  # // : is the interger division

#         if numbers[middle] == target:
#             return True

#         elif numbers[middle] < target:
#             left = middle +1

#         else:
#             right = middle -1

#     return False


# Part3: O(n2)

# Complexity	Meaning	         Example
# O(1)	        Constant	     Accessing numbers[0] -> perfect
# O(log n)        Linear	         Linear search.       -> very good
# O(n)	    Logarithmic	     Binary search.       -> good
# O(n²)	        Quadratic	     Two nested loops     -> can become very slow

# Nested loop : a loop inside another loop

#Final chalenge 

# for student in students:
#     print(student["name"])

# students → the whole list

# student → one dictionary

# student["name"] → the name inside that dictionary

students = [
    {"name": "John", "score": 72},
    {"name": "Sarah", "score": 91},
    {"name": "Mike", "score": 45},
    {"name": "Anna", "score": 84}
]

def find_student(students, name):

    for student in students:
        
        if student["name"] == name:
            print(students["name"])

   

find_student(students, "John")