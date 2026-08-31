#For loop

# for i in range(5):
#     print(i) #print first 5 interger starting from '0'

# for i in range(1, 6):
#     print(i)    #print all interger from 1 to 5 stop before 6

# for i in range(1, 12, 3):
#     print(i) #print intergers from 1 to 10 moving by 3 at each step.

# for i in range(5, 0, -1):
#     print(i) #print from 5 to 1 in descending order. use for counter

#loop on a string
# password = "Glsroenbfn363na7n%554"
# for character in password:
#     print(character) #Python display each character from the string, one at a time.

# for character in password:
#     if character.isdigit(): #asks If this character a digit?
#         print(f"{character} is a digit")

#While 
  #is 1<=5? yes print 1
# while number <= 5:
#  number += 1. is 2 <=5 ? yes and so on until number =6
#  print(number) #while loop repeats while a condition is true.
  
#break tells Python Stop the loop immediately.

# for i in range(1, 10):
#      if number ==5:
#          break
#      print (number)

#continue is different  it means Skip the current iteration and continue with the next one.
# number = 1
# for number in range (1, 8):
#     if number == 5:
#         continue
#         print(number) #Python sees 5, executes continue, and skips the print() for that iteration.

# count = 0

# for number in range(1, 6):
#     count += 1

# print(count)

#Accumulators stores a vvalue that grows as the loop runs
# total = 0

# for number in range(1, 6):
#     total += number

# print(total)

#Lists are built-in , mutable and ordered collection of items enclosed into square brackets [] seperate by commas

# empty_list = []
# numbers = [1, 2, 3]
# mixed_list = ["Alice, 42, True, 314"]

# students = ["Arnauld", "John", "Sarah", "David"]

# for student in students:
#     print(student)

# scores = [45, 47, 60, 58, 72]

# for score in scores:
#     if score >=60:
#         print(f"{score}: Pass")
#     else:
#         print(f"{score}: Fail")

#Nested loops

# for i in range(3):
#     for j in range(3):
#         print(i, j) #The inner loop runs completely for each iteration of the outer loop.

# numbers = [10, 20, 30, 40, 50]
# total = 0
# for number in numbers:
#     total += number
#     average = total / len(numbers)
# print(average)


# number = int(input("Enter a number: "))
# for i in range(1, 11):
#      print(f"{number} x {i} = {number * i}")

# word = input("Enter a word: ")

# for character in word:
#     print(character)

# DAY3 MINI-PROJECT ---PASSWORD ANALYSER

password = input("enter your password: ")
password_length = len(password)
has_digit = False
has_uppercase = False
has_special = False
satisfied_criteria = 0
print(f"password lenght: {password_length}")

for character in password:
    if character.isdigit():
        has_digit = True

    if character.isupper():
        has_uppercase = True
    if not character.isalpha() and not character.isdigit():
        has_special = True

if has_digit:
    satisfied_criteria += 1
if has_uppercase:
    satisfied_criteria += 1
if has_special:
    satisfied_criteria += 1
if password_length >= 8:
    satisfied_criteria += 1

if password_length < 6:
    strength = "weak"
elif password_length <= 9:
    strength = "medium"
else:
    strength = "strong"

print(f"Contains a digit: {has_digit}")
print(f"Contains an uppercase letter: {has_uppercase}")
print(f"contain a special character: {has_special}")
print(f"Satisfied criteria: {satisfied_criteria}/4")
print(f"Password strength: {strength}")
