#PART 1 — FILES 📁
#we use file to save our programs informations permanently in order to be reuse later

#Opening a file with open(): file = open("stidents.txt", "r")

# file = open("students.txt", "r")
# content = file.read()
# file.close()

# with open("students.txt", "r") as file:
#     content = file.read()
# print(content) # Pyton automatically close the file. 

# with open("days.txt", 'r') as file:
#     content = file.read()
# print(content)

# Reading line by line: 
# with open("students.txt", "r") as file:
#     students = file.readlines()
# print(students)

# with open("students.txt", "r") as file:
#     for line in file:
#         print(line.strip()) # .strip() removes unnecessarry whitespace and the newline.

# Exercice 1

# with open("names.txt", "r") as file:
#     for line in file:
#         print(line.strip())


# PART 2 — WRITING FILES ✍️ : we use "w"

# with open("students.txt", "w") as file: # "w" replace the file's previous content.
#     file.write("Paul\n")
#     file.write("Jennifer\n")
#     file.write("Linda\n")

# # Adding without deleting:

# with open("names.txt", "a") as file: # with "a"(append) the previous content remains
#     file.write("Max\n")

# Exercice 2 -- Write and append

# with open("languages.txt", "w") as file:
#     file.write("Python\n")
#     file.write("Java\n")
#     file.write("C++\n")
# with open("languages.txt", "a") as file:
#     file.write("Javascript\n")

# PART 3 — EXCEPTIONS ⚠️

#try and except 

# try: 
#     number = int(input("Enter a number: "))
#     print(number)
# except ValueError:
#     print("place a valid number.")

# Exercice 3 - Exception handling

# try:
#     number = int(input("Enter a number: "))
#     result = 100 / number
#     print(f"result: {result}")
# except ZeroDivisionError:
#     print("Cannot divide by zero") 

# Modules 
# import math
# import random

# print (math.sqrt(25))

# number = random.randint(1, 10)
# print(number)

# from math import sqrt
# print(sqrt(25))

# PART 5 — CREATING YOUR OWN MODULE 🧩

#calculator.py : module creation
# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b

# #main.py. import the module calculator in a different file
# import calculator 
# print(calculator.add(10, 5))
# print(calculator.subtract(10, 5))

# MINI-PROJECT — STUDENT RECORDS

def add_student(name, score):
    try:
        score = int(score)

        if score <= 0:
            print("Invalid score. Please enter a positive number.")
            return

        with open("students.txt", "a") as file:
            file.write(f"{name}, {score}\n")

    except ValueError:
        print("Invalid score. Please enter a number.")

def display_students():
    with open("students.txt", "r") as file:
        for line in file:
         name, score  = line.strip().split(",")
         print(name, "->", score)

add_student("Arnauld", 98)
add_student("Steve", 80)
add_student("John", "hello")
add_student("Mike", -5)

display_students()