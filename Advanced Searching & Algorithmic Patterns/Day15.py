
# 2- Pattern #1 -- Frequency Counting
# numbers = [1, 2, 2, 3, 3, 3, 4]


# def count_frequency(numbers):
#     frequency = {}

#     for number in numbers:
#         if number in frequency:
#             frequency[number] +=1
#         else:
#             frequency[number] = 1
#     return frequency

# print(count_frequency(numbers))


# Finding the most frequent

# def most_frequent_number(numbers):
#     frequency = {}
#     for number in numbers:
#         if number in frequency:
#             frequency[number] += 1
#         else:
#             frequency[number] = 1 
#     most_frequent = None 
#     highest_count = 0
#     for number , count in frequency.items():
#         if count > highest_count:
#             highest_count = count
#             most_frequent = number
#     return most_frequent 

# print(most_frequent_number([4, 4, 2, 7, 2, 4]))


# Find the first duplicate
# numbers = [6, 3, 8, 2, 3, 9, 6]
# def first_duplicate(numbers): # With a dictionnary
#     seen = {}
#     for number in numbers:
#         if number not in seen:
#             seen[number] = number
#         elif number in seen :
#             return number
#     return None

# print(first_duplicate(numbers))

# numbers = [6, 3, 8, 2, 3, 9, 6]

# def first_duplicate(numbers): # with a set
#     seen = set()

#     for number in numbers:
#         if number not in seen:
#             seen.add(number)
#         else:
#             return number

#     return None

# print(first_duplicate(numbers))


# Patternn3: two pointers

# numbers = [2, 3, 5, 7, 9, 12]
# target = 10

# def two_sum_sorted(numbers, target):
#     left = 0
#     right = len(numbers)-1

#     while left< right:
#         total = numbers[left] + numbers[right]
#         if total == target:
#             return numbers[left], numbers[right]
#         elif total<target:
#             left +=1
#         else:
#             right -=1
#     return None

# print(two_sum_sorted(numbers, 15))

# Pattern 4: sliding window

# def max_window_sum(numbers, k):
#     window_sum = sum(numbers[:k])
#     max_sum = window_sum

#     for i in range(k, len(numbers)):
#         window_sum += numbers[i]
#         window_sum -= numbers[i-k]

#         max_sum = max(max_sum, window_sum)
#     return max_sum

# numbers = [5, 8, 3, 10, 6, 4, 9]
# print(max_window_sum(numbers, 3))

#Pattern 5: Prefix Sum

# sum(L, R) = prefix[R] - prefix[L-1]. if L>0 Sum(0, R) = prefix[R] if L=0 

# requests = [4, 7, 2, 9, 5, 8, 3, 6]
# prefix_sum = [4, 11, 13, 22, 27, 35, 38, 44]

# numbers = [4, 7, 2, 9, 5]
# def build_prefix_sum(numbers):
#     prefix = []
#     running_total =0
#     for number in numbers:
#        running_total += number
#        prefix.append(running_total)
#     return prefix
# print(build_prefix_sum(numbers))

#Pattern 6: Binary Search for Boundaries

# numbers = [1, 2, 2, 2, 3, 4, 5]

# def first_occurence(numbers, target):
#     left = 0 
#     right = len(numbers) - 1
#     answer = -1

#     while left <=right:
#         mid = (left + right) // 2

#         if numbers[mid] == target:
#             answer = mid
#             right = mid - 1
#         elif numbers[mid] < target:
#             left = mid + 1
#         else:
#             right = mid -1 
#     return answer


# numbers = [1, 2, 2, 2, 3, 4, 5]
# target = 2

# def last_occurence(numbers, target):
#     left = 0 
#     right = len(numbers) - 1
#     answer = -1

#     while left <=right:
#         mid = (left + right) // 2

#         if numbers[mid] == target:
#             answer = mid
#             left = mid + 1
#         elif numbers[mid] > target:
#             right = mid - 1
#         else:
#             left = mid +1 
#     return answer


# Pattern7: Fast Lookup with two Hash Structures

# users = ["John", "Sarah", "Mike", "Annna"]
# logged_in = ["Sarah", "Anna"]

# logged_in_set = set(logged_in)

# for user in users:
#     if user in logged_in_set:
#         print(user)

# Sets use hashing to perform fast membership lookup : avverage complexity is O(1)
# Lists membership is O(n)


attempts = [
    "john",
    "sarah",
    "mike",
    "john",
    "anna",
    "sarah",
    "john"
]
# A. how many times each user attempted to log in. 

def user_attempts(attempts):
    logged_in = {}

    for user in attempts:
        if user in logged_in:
            logged_in[user] += 1
        else:
            logged_in[user] = 1

    return logged_in


attempts = [
    "john",
    "sarah",
    "mike",
    "john",
    "anna",
    "sarah",
    "john"
]

print(user_attempts(attempts))



















