#Graph Algorithms & Shortest paths 

# Dijkstra's Algorithm 
# Relaxation : process of asking if a node can be reach more cheaply through  the current node 

# if new_distance < distance[neighbor]:
#     distance[neighbor] = new_distance


#Dijkstra + Priority Queue


# import heapq

# distances = {
#     "A": 0,
#     "B": float("inf"),
#     "C": float("inf"),
#     "D": float("inf")
# }

# priority_queue = [(0, "A")]

# Weighted graph representation

# graph = {
#     "A": [("B", 4), ("C", 1), ("D", 10)],
#     "B": [("D", 2)],
#     "C": [("B", 1), ("D", 5)],
#     "D": []
# }

# while priority_queue:
#     current_distance, current_node = heapq.heappop(priority_queue)

#     for neighbor, weight in graph[current_node]:
#         new_distance = current_distance + weight #Get the cheapest node. 

#         if new_distance < distances[neighbor]: #Calculate a possible new route if the new distance is cheaper update it.
#             distances[neighbor] = new_distance
#             heapq.heappush(priority_queue, (new_distance, neighbor))

# NB : a priority queue can contains the same node multiple times, but we onlu want to use the best known distance. 

import heapq

def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        #Skip outdated entries
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))
    return distances


graph = {
    "A": [("B", 4), ("C", 1), ("D", 10)],
    "B": [("D", 2)],
    "C": [("B", 1), ("D", 5)],
    "D": []
}

print(dijkstra(graph, "A"))

































