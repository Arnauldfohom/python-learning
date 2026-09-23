
# TREES & GRAPHS

# 1- A tree is a data structure used to represent hierachical relationships.

    #     A root & parent of B & C
    #    / \
    #   B   C leaf is a node with no children
    #  / \
    # D   E


# 2- A graph is a data structure made of : Nodes(objects) & Edges9connections between objects 

# A -------- B.   nodes = [A,B,C,D]
# |          |    edges = [A-B , A-C, B-D, C-D]
# |          |
# C -------- D

# a tree doesn't have cycles while a graph do (A-B-D-C-A is a cycle.)


#3- Representing Graphs in Python

# graph = {
#     "A": ["B", "C"], #this Means A is connected to B and C 
#     "B": ["A", "D"],
#     "C": ["A", "D"],
#     "D": ["B", "C"]
# }

# 4- Trees, Graphs & AI search

# BFS -> Queue explores level by level : A->B->C->D->E FIFO
# First node discovered -> first node explored

#DFS ->Stack / Recursion LIFO

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}
def dfs(graph, node, visited):
    visited.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
visited = []

dfs(graph, "A", visited)

print(visited)

#BFS gives the shortest path in an unweighted graph

# BFS & DFS Complexity

# BFS -> O(V+E)
# DFS-> O(V+E)
