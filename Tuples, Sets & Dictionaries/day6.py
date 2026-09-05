#TUPLES, SETS & DICTIONARIES

# 1 - Tuples #use to represent immutable set of data.

# students_records = ("Arnauld", 26, 'computer science') #tuples are writen with parentheses while lists are written with brackets

# print(students_records[0]) # Tuples are immutable(you can't modify it once you create it)
# print (students_records[1])
# print(students_records[2])
# Exercice 1


# 2 - SETS : is a collection of unique values
# numbers = {1,2,3,4} #written with braces and dupplicates values disappear
# countries = ["Cameroon", "France", "USA", "France"]
# unique_country = set(countries)
# unique_country.remove("France")
# unique_country.add("Spain")
# print(unique_country)
# if "Cameroon" in countries:
#     print("found")

# 3 - Dictionnaries : store informations as a key : value. use in JSON connection.
# car = { # Dictionnaries are mutable.
#     "brand": "Toyota",
#     "model": "Corola",
#     "color": "black"
# } # we access dictionnaries using keys
# # print(car["brand"])
# # print(car["model"])
# car ["brand"] = "Mercedes"
# car ["model"] = "Gle"
# car ["year"] = 2026

# #delete data 
# # del car["color"]
# # car.pop("year")
# print(car)
# if "brand" in car:
#     print("brand exist")

# #Dictionnary methods:
# print(car.values()) #print all car's values
# print(car.keys())  #print all car's keys
# print(car.items()) #Give key-value pairs.

#Exercice 4
# person = {
#     "name": "Job",
#     "age": 26,
#     "city": "Buea",
#     "job": "Developer"
# }
# for key, values in person.items():
#     print(key, ":", values)

#Dictionnaries + Functions:
# def display_student(student):
#     student ={ "name": "kamdem",
#               "age" : 34,
#               "ocupation": "entrepreneur"

#     }
#     return student

# print(display_student("student"))

#nested dictionnaries:

# students = {
#     "student1" : { #student1 is the first key of students
#         "name": "paul",
#         "age": 26
#     },
#     "student2" : { #student2 is the second key of students 
#         "name": "tyler",
#         "age": 32
#     }
# }
# print(students["student2"]["age"]) #use to access student2 age
# print(students["student1"]["name"])#usse to access student1 name

# Algorithmic thinking:
# numbers = [1, 2, 3, 4, 5, 2, 4, 5]

# unique_numbers = []
# for number in numbers:
    
#     if number not in unique_numbers:
       
#          unique_numbers.append(number)
    
       
        
# print(unique_numbers)

#MINI PROJECT — STUDENT DATABASE

students = [
    {"name": "John", "score": 72},
    {"name": "Sarah", "score": 91},
    {"name": "Mike", "score": 45},
    {"name": "Anna", "score": 84}
]

def display_students(students):
    print("Students : ")
    for student in students:
        print(student["name"], "->", student["score"])
    
def calculate_average(students):
    total = 0
    for student in students:
        total += student["score"]
    average = total / len(students)
    return average    
    
def find_top_student(students):
  current_best = students[0]

  for student in students:
      if student["score"] > current_best["score"]:
          current_best = student  
  return current_best

def count_passed(students):
    count = 0
    for student in students:
      if student["score"] > 50:
          count += 1
    return count

display_students(students)
print(calculate_average(students))
print(find_top_student(students))
print(f"Passed: {count_passed(students)}")