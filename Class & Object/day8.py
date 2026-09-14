# Class vs Object

#Class: it's a blueprint/template that create objects.

#Object : is an actual thing created from that bblueprint

# Creating my first class

# class Student:
#     pass #means there is nothing here yet

# # Creating an object 
# student1 = Student() # it's an instance/obbject of the Student 

# # Attributes : are data that belong to objects

# student1.name = "Arnauld"
# student1.score = "100"

# print(student1.name)
# print(student1.score)

# Exercice 1
# class Car:
#     pass 

# car1 = Car()
# car1.brand = "Toyota"
# car1.model = "Corolla"
# car1.year = 2024
# print(car1.brand)
# print(car1.model)
# print(car1.year)

# The __init__() method : is a special method that runs when you create an object.it's use to create the attributes automatically.

# class Student:

#     def __init__(self, name, score):
#         self.name = name # self refers to the current student (object)
#         self.score = score

# student1 = Student("Arnauld", 100) #create student1 and initalize it with Arnauld and 98
# student2 = Student("Sara", 98)

# print(student1.name) 
# print(student2.name)

# Exercise 2

# class Student:
#     def __init__(self, name , age , score):
#         self.name = name
#         self.age = age 
#         self.score = score

# student1 = Student("Arnauld", 26, 98)
# student2 = Student("Bertol", 26, 97)

# print(student1.name)
# print(student1.score)
# print(student2.name)
# print(student2.score)

# Methods: is a function inside a class

# class Student:

#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#     def display(self):
#         print(self.name, "->", self.score)

# student1 = Student("Arnauld", 98)
# student1.display()

#Methods can perform calculations

# class Student:
#     def __init__(self, name , score):
#         self.name = name
#         self.score = score
#     def is_passed(self):
#         return self.score >= 50

# student1 = Student("Arnauld", 98)
# student2 = Student("Lea", 45)
# print(student1.is_passed())
# print(student2.is_passed())

# exercice 3

# class Student:
#     def __init__(self, name , score):
#         self.name = name
#         self.score = score
#     def display(self):
#         print(self.name, "->", self.score )
#     def is_passed(self):
#         return self.score >= 50

# student1 = Student("Arnauld", 98)
# student2 = Student("Mike", 45)

# student1.display()
# print(student1.is_passed())

# student2.display()
# print(student2.is_passed())

# Basic inheritance
# class Animal:
#     def speak(self):
#         print("Animal make a sound")

# class Dog(Animal): # The Dog class inherit the speak() method  from parent's class Animal
#     pass
# dog = Dog()
# dog.speak()

# MINI-CHALLENGE -- Bank account

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount): #self reffers to the account that's is using the method
#         if amount > self.balance:
#             print("Insufficient Balance")
#         else:
#             self.balance -= amount

#     def display_balance(self):
#         print(f"Owner: {self.owner}")
#         print(f"Balance: {self.balance}")


# account = BankAccount("Arnauld", 2500000)

# account.deposit(500000)
# account.withdraw(3000001)
# account.display_balance()
        
# -----------------------------------------------------------------------------
#Part 2: Inheritance & Encapsulation

# 1. Inheritance : allows a class (child) to reuse attributes and methods from another class(parent)

# class Animal:
#     def speak(self):
#         print ("Animal makes a sound")

# class Dog (Animal):
#     def bark(self):
#         print("Woof!")

# dog = Dog() # create dog object from class Dog. 
# dog.speak() #The Dog object inherit this method from Animal 
# dog.bark() # belongs specifically to Dog class

# Method Overriding : a child class can replace a method from its parent.
# class Animal:
#     def speak(self):
#         print ("Animal makes a sound")
# class Dog(Animal):
#     def speak(self):
#         print("Dog makes woof!") # Dog version overrides the Animal one.

# dog = Dog()
# dog.speak()      


# Encapsulation: means controlling how data inside an object are accessed or modified.
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self._balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount

#     def get_balance(self):
#         return self._balance

# account = BankAccount("Arnauld", 100000)

# account.deposit(50000)

# print(account.get_balance())


# Challenge 1 - inheritance
# class Animal:
#     def speak(self):
#         print("Animal makes a sounds.")

# class Cat(Animal):
#     def meow(self):
#         print("Meow!")

# cat = Cat()
# cat.speak()
# cat.meow()

# Challenge 2 - Method overriding

# class Animal:
#     def speak(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def speak(self):
#         print("Dog says Woof!")

# dog = Dog()
# dog.speak()

# Challenge 3 - AI-style OOP

# class AIModel:
#     def __init__(self, name):
#         self.name = name
#     def train(self):
#         print(self.name, " is training...")
#     def predict(self):
#         print(self.name, "is making a prediction...")

# aimodel = AIModel("Cancer Detection Model")
# aimodel.train()
# aimodel.predict()
# model1 = AIModel("Face recognition Model")
# model2 = AIModel("Spam detection Model")

# model1.train()
# model2.predict()

# --------------------------------------------------------------------------------------

# DAY 8 FINAL CHALLENGE — AI Model Management

class AIModel:
    def __init__(self, name, model_type, accuracy):
        self.name = name
        self.model_type = model_type
        self.accuracy = accuracy 
        self.trained = False 
    def train(self):
           self.trained = True
           print(self.name, "has been trained.")
    def predict(self):
        if not self.trained:
            print("Model must be trained first")
        else:
             print(self.name, "is making a prediction.....")
    def display_info(self):
         print("Name:", self.name)
         print("Type: ", self.model_type)
         print("Accuracy :", self.accuracy)
         print("Trained :", self.trained)

model1 = AIModel("Cancer Detector", "Computer Vision", 0.95)

model2 = AIModel("Spam Detector", "Machine Learning", 0.91)

model3 = AIModel("Chatbot", "Natural Language Processing", 0.88)

model1.predict()

model1.train()

model1.predict()

models = [model1, model2, model3]

for model in models:
    model.display_info()

def find_best_model(models):
    best = models[0]
    for model in models:
         if model.accuracy > best.accuracy:
              best = model
    return best

         