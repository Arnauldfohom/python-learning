# Lists []  are mutable collection of multiple vvalues stored in a single variable

#Creating lists:
# students = ["Arnauld", "Bertol", "steve"] 
# person = ["Arnauld", 26, 185, "darkskin"]
# matrix = [[1, 2, 3], [4, 5, 6]] #a list inside another list.

# #Indexing:
# #For students , Arnauld -> 0 , Bertol-> 1 Steve -> 2
# print(students[0]) # give Arnauld

# #Negative indexes:
# print(person[-1]) #-> darksin
# print(person[-3]) #-> 26

# last_student = students[-1]

# #Changing list elements
# # lists are mutable which means you can change their elements   
# fruits = ["apple", "banana", "orange"]

# fruits[1] = "mango" #this replace the value of fruits index 1 with "mango"

# print(fruits)

# #List Length
# len()
# print(len(person)) #gives 4

# #ADDING ELEMENTS: append()
# students.append("Jennifer") #add Jennifer after the last index of the list  logging.critical('students: %s', repr(students))

# #insert() : use to add an element at a specific position. 
# students.insert(2, "William") #add student william at the index 2 and student steve is now at index 3

# #REMOVING ELEMENTS: remove()
# #To remove a specific value in the list:
# students.remove("Jennifer")

# #pop(): removes an element using index
# students.pop(1) #"bertol" will be removved from the list.
# #Nb: students.pop(): automatically remove the last element.
# del students[2] #delete the element of students index 2

#Important distinction
# Method	    What it does
# append(x)	    Add x at the end
# insert(i, x)	Add x at index i
# remove(x)	    Remove value x
# pop(i)	    Remove element at index i
# pop()	        Remove last element
# del	        Delete an element

#LOOPING THROUGH LISTS
# for student in students:
#     print(student)

# scores = [45, 67, 89, 32, 90, 76]
# for score in scores:
#   print(score)
# for score in scores:
#   if score >= 50:
#     print(score) 

#in operator
# fruits = ["apple", "banana", "orange"]
# # print("pinaple" in fruits) # Check if an element exists in a list 
# if "orange" in fruits:
#     print("orange found!")

#Sorting Lists with sort():
# friends = ["syndie", "awa", "jennifer", "brenda"]
# friends.sort() #sort array element in aphabetical order.
# print(friends)
# friends.sort(reverse=True) #sort friends in descending order
# print(friends)

# Min , Max and Sum:
# numbers = [23, 54, 12, 10, 45, 87]

# print(max(numbers))
# print(min(numbers))
# print(sum(numbers)) print the sum of all elements of numbbers[]
# average = sum(numbers) / len(numbers)
# print(average) 

#. List slicing 
# numbers = [0, 1, 2, 3, 4, 5, 6]
# print(numbers[1:3]) #last index is excluded.
# print(numbers[:3]) #print first 3 indexes. 
# print(numbers[3:]) #print all elements from 3. 
# print(numbers[:]) #entire list. 
# Exercice : STUDENT ANALYZER

# scores = [72, 45, 89, 63, 91, 38, 76]

# def number_of_students():
#     num_of_students = len(scores)
#     return num_of_students
# def highest_score():
#     high_score = max(scores)
#     return high_score
# def lowest_score():
#     low_score = min(scores)
#     return low_score
# def average_score():
#     average = sum(scores)/number_of_students()
#     return average
# def students_who_passed():
#     count = 0 
#     for score in scores:
#         if score >= 50:
#             count +=1
#     return count
# def students_who_failed():
#     count = 0
#     for score in scores:
#         if score < 50:
#           count +=1 
#     return count

# def percentage():
#     percentage_who_passed = (students_who_passed()/number_of_students()) * 100
#     return percentage_who_passed


# def display_result(num_of_students, high_score, low_score, average, passed_count, failed_count, percentage_who_passed):
#     print(f"Number of students: {num_of_students}")
#     print(f"Highest score: {high_score}")
#     print(f"Lowest score: {low_score}")
#     print(f"Average: {average:.1f}")
#     print(f"Passed: {passed_count}")
#     print(f"Failed: {failed_count}")
#     print(f"Pass rate: {percentage_who_passed:.1f}%")

# def main():
#     num_of_students= number_of_students()
#     high_score= highest_score()
#     low_score = lowest_score()
#     average = average_score()
#     passed_count = students_who_passed()
#     failed_count = students_who_failed()
#     percentage_who_passed = percentage()
#     display_result(num_of_students, high_score, low_score, average, passed_count, failed_count, percentage_who_passed)

# main()
numbers = [3, 8, 12, 5, 19, 2, 10]

def find_max(numbers):

    largest = numbers[0]

    for number in numbers:

        if number > largest:
            largest = number

    return largest

result = find_max(numbers)
print(result)