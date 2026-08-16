#print() function

# print("My first python program!")
# print(25)
# print(3.14)


#Variables



# print(name,age,height)
# print("My name is",name, "I'm", age , 'and Im' , height, 'tall')

# is_student = True
# has_bachelor = True
# is_dating = False

#We use type() to verify the type of a variable.
# print(type(name))
# print(type(is_student))
# print(type(height))
# print(type(age))


#Maths operations

a= 10
b= 3

a = 10
b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a%b) #rest of division of a by b
# print(a//b) #int value of a divided by b
# print(a**b) #a to the power b


#modify an interger variable (age)

# age += 1
# age -= 1
# age *= 2
# age /= 2
# print(age)

#Les chaines de caracteres str

# first_name = "Arnauld"
# last_name = "Fohom"

# full_name = first_name +" "+ last_name
# print(full_name)

# print(len(full_name))



# print(f"my name is {name} and I'm {age} years old")

# price = 185000
# quantity = 2

# total = price * quantity

# print(f"the total price is {total} fcfa")

#comparaisons
# print(age == 26)
# print(age != 26)
# print(age >= 32)
# print(age <= 27)

#input()

# name = input("enter your name: ")
# print(f"Hello {name}!")
# age = int(input("How old are you?"))
# print(f"I'm {age}")


#conversion des type:

# int()
# float()
# str()
# bool()

# age = "26" #here age is a str 
# age = int(age)  #convertion of the string to an int
# print(type(age))


#Mini-project day1

name = "Arnauld"
age= 26
height= 1.85
country = "cameroun"

nname = input("What's your name? ")
age = int(input("What's your age? "))
height = float(input("What's your height? "))
country = input("What's your country? ")

print("\n----- STUDENT INFORMATION -----")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} m")
print(f"Country: {country}")

next_year_age = age + 1

print(f"Next year, you'll be {next_year_age} years old.")



















