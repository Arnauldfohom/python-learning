# Stacks, Queues & Recursion

# I- Stack : data structure that follows LIFO(Last in First Out)

# 1- push   stack.append(a) add 'a' to the top of the stack 

# 2- Pop  stack.pop() : remove the top element

# 3- Peek : lookat the top element without removing it. 

# 4- Check if empty :

# if len(stack) == 0 :
#     print("stack is empty") 

# if not stack:
#     print("stack is empty")

# II- Queue : data structure that follows FIFO (First in First Out)
# from collections import deque

# queue = deque()

# queue.append("A")

# queue.append("B")

# queue.append("C")

# queue.popleft() #remove A leave B -> C

# Why queues matter in AI : can be use for BFS (Breath-first search)

# III- Recursion: means a function calling itself

# every good recursive function needs a condition that tells it to Stop! and that's call a base case.

# without that condition that function will keep calling itself indefinetely.
# def countdown(n):
# if n == 0 :
#     return

# print (n)
# countdown(n-1)

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

stack.pop()
stack.append(40)
stack.pop()

print(stack)