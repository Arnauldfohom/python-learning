#Define and calling functions:
# def say_hello():
#     print("Hello, welcome to python") #new function 

# say_hello()    #calling the function

# def show_name():
#     name = input("Enter your name: ")
#     print(f"Hello, {name}")

# def show_age():
#     age = int(input("Enter your age: "))
#     print(f"you're {age} years old.")

# show_name()
# show_age()

#Parameters & Arguments:A parameter is a variable defined inside the function declaration. An argument is the actual value passed to the function.

# def greet(name): #name is a parameter
#     print(f"Hello, {name}")

# greet("Arnauld") #Arnauld is an argument

# def introduce(name, age):
#     print(f"My name is {name} and I'm {age} years old")
# introduce("Arnauld", 26)

# def calculate_area(length, width):
#     area = length * width
#     print(f"area={area}")

# calculate_area(23, 12)

#Return a value

# def add(a, b):
#     return a + b  #with return , you can store the result in a variabble and call it later

# result = add(2, 3)
# print(result)
# #print: display a value while return: sends a value back.
# if result>3:
#     print("Greater than 3")

# def calculate_average(a, b, c):
#     return (a+b+c)/3
# average = calculate_average(2,3,4)
# print(average)

# def is_even(number):
#    return number % 2 == 0
    
# print(is_even(8))

# def is_passed(score):
#     return score >= 50
    
# print(is_passed(6))

#FUNCTIONS + Loops

# def count_vowels(text):
#     count = 0
#     text = text.lower()

#     for character in text:
#        if character in "aeiou":
#            count +=1
#     return count

# print(count_vowels("PAUL is my best fRiend"))

#Functions + Lists preview

# numbers = [2, 3, 4, 5, 6, 7]

# def calculate_average(numbers):
#     total = 0
#     for number in numbers:
#         total += number
#     return total/len(numbers)

# print(calculate_average(numbers))

#DEFAULT PARAMETERS / PARAMÈTRES PAR DÉFAUT

# def calculate_price(price, tax=0.19):
#      return price * (1 + tax)
# print(calculate_price(2000, 0.5))

#VARIABLE SCOPE / PORTÉE DES VARIABLES
#local variable

# def test():
#     number = 10 #number only exist inside the function

#Global variable
# number =10
# def test():
#     return number #number exist out of the function

#MINI PROJECT — STUDENT GRADE ANALYZER


def get_student_name():
    name = input("Enter student name: ")
    return name


def get_grades():
    grades = []
    num_of_grades = int(input("How many grades? "))
    for i in range(num_of_grades):
        grade = int(input(f"Enter grade {i+1}: "))
        grades.append(grade)
    return grades
    
def calcul_average(grades): 
    average = sum(grades)/len(grades)
    return average

def check_result(average):
    if average >= 50:
        status = "Passed"
    else:
       status = "Failed"
    return status

def display_result(name, average, status):
    print(f"Student: {name}")
    print(f"Average: {average}")
    print(f"Status: {status}")
    
def main():
    name = get_student_name()
    grades = get_grades()
    average = calcul_average(grades)  
    status = check_result(average)   
    display_result(name, average, status)  

main()  