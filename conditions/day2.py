# #if statement

# # age =18
# # if age>=18:
# #     print("You are an adult.")
# # else:
# #     print("You're a minor.")

# # age = 26
# # print(age> 18)
# # print(age < 18)
# # print(age == 26)
# # print(age !=30)



# #And: here the 2 conditions have to be true.  true and false = false. true or false = true. not False = true



# # age = 16
# # has_ticket = False
# # is_vip = True

# # if has_ticket or is_vip:
# #     print("You can enter.")


# #condition with input() 

# age = int(input("what's your age?"))

# if age >= 18:
#     print("You're an adult.")
# else:
#     print("You're a minor.")


#Many criteria

# age = int(input("Age: "))
# country = input("Country: ")

# if age >= 18 and country == "Cameroon":
#     print("You're an adult from Cameroon.")
# else:
#     print("condition not satisfied.")


#condition imbriquees

# age = int(input("Age: "))

# if age >= 18:

#     has_id = input("Do you have an Id?")
#     if has_id == "yes":
#         print("access granted")
#     else:
#         print("access denied!")
# else:
#     print("access denied!")

# score = float(input("Enter your score:"))

# if score >= 90:
#     print("Excellent")
# elif score >= 80:
#     print("Very good")
# elif score >= 70:
#     print("Good")
# elif score >= 60:
#    print("Pass")
# else:
#     print("Fail")




# DAY 2 PROJECT — PASSWORD STRENGTH CHECKER

password = input("Enter your password:")
password_length = len(password)

if password_length  < 6:
    print("Weak password")
elif password_length  <= 9:
    print("Medium password")
else:
    print("Strong password")