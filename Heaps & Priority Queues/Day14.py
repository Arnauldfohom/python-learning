
numbers = [7, 2, 9, 1, 5]

#1- A heap is a special tree-based data structure designed to efficiently access the smallesst or largest element. 

# Min-heap: the smallest element is always at the top. Here, any parent is smaller or equal to its children

#Max-heap: The largest element is always at the top. Nb: a heap is'nt a sorted list

# The only guarantee with a heap is that the minimum or maximum is at the top. 

# Python's heapq 
import heapq

heap =[]

# heapq.heappush(heap, 7) #To add 5 in the heap
# heapq.heappush(heap, 3)
# heapq.heappush(heap, 9)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 5)

# # The smallest element is always at heap[0]

# # this is called peeking. peek -> O(1)

# heapq.heappop(heap) #remove the smallesst element an reorganize the heap

# print(heap) #heappop-> O(log n)

# if we hae a large numberof element , the height of the tree grows logarithmically 

# heappush → O(log n)
# heappop  → O(log n)
# peek     → O(1)


# 2- Priority Queues
# a priority queue is a structure where items are processed according to their priority, rather than simply according to when they arrived 

# Suppose an AI has discovered:

# State A → cost 15
# State B → cost 4
# State C → cost 9
# State D → cost 2  an algorithm may want to explore the state with the lowest cost first
#Therefore D->B->C->A

# python's heapq is naturally a min-heap
# for largest element : largest = -heap.heappop(heap)



# Mini Project: SOC Alert Priority Queue

alerts = [
    ("Suspicious Login", 7),
    ("Malware Detected", 10),
    ("Port Scan", 4),
    ("Data Exfiltration", 9),
    ("Failed Login", 2)
]



heap = []

for alert, severity in alerts:
    heapq.heappush(heap, (-severity, alert))

while heap:
    severity, alert = heapq.heappop(heap)
    print(alert, "->", -severity)