# HASH TABLES, SETS & FAST LOOKUPS

# 1- The problem: Finding information

# students = [
#     {"name": "John", "score": 72},
#     {"name": "Sarah", "score": 91},
#     {"name": "Mike", "score": 45},
#     {"name": "Anna", "score": 84}
# ]
# #linera search to find Sarah's score:

# for student in students:
#     if student["name"] == "Sarah":
#         print(student["score"])


# 2- A Hash table is a data structure designed to store and retrieve information using a key

# 3- Average O(1) Lookup : means on average, the amount of work doesn't grow linearly with the number of stored items. 

# 4- How does a hash work ? 

# key = "Sarah"
# # a hash function convert the key to a numerical hash value. 

# # "Sarah" -> hash -> 58324 -> location
# print(hash("Sarah"))

# # 5- Dictionary = Key -> Value
# students["Sarah"] # find the value associated with the key Sarah.


# 6- Hash Collisions

# "John"  → hash → 42
# "Sarah" → hash → 17
# "Mike"  → hash → 42   ← collision!  the both ended at the same location

# 7- Chaining 
# Location 42 
#      |
# [("John", 72), ("Mike", 45)]

# scores["Mike"] becomes 45


# 7- Sets use hash table too : set main property is uniqueness. 

# numbers = {10, 20, 30, 40}
# if 30 in numbers:
#     print("Found") # membership is average  O(1) while a list is averaging O(n)


# numbers = [4, 7, 2, 9, 7, 5]

# seen = set()

# for number in numbers:
#     if number in seen:
#         print("Duplicate found:", number)
#         break

#     seen.add(number)


#Day 13 challenge 

numbers = [4, 2, 6, 7, 3, 2]
def has_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True

        seen.add(number)

    return False
       




































