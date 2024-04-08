#!/usr/bin/python
from graph import Graph


# Check for intersection
def intersection(a, b):
    for i in a:
        # if element of visited1 is found in visited2 then that node has been visited by both. Return that node
        if i in b:
            return i
    return -1


# Take data as reference and update it
def bfs(graph, queue, visited, parent):
    n = queue.pop(0) # Pop first element of queue
    for neighbor in graph[n]: # get all child/neighbors of that node from graph
        if neighbor not in visited: # if this perticular neighbor has not been visited then
            # add it to queue
            queue.append(neighbor)
            # mark it as visisted
            visited.append(neighbor)
            # save parent node of node 'n'. It will be used to get path from point of intersection to node
            parent[neighbor] = n


def bi_dir(graph, start, goal):
    queue1 = [start] # Forwad queue
    queue2 = [goal] # Backward queue
    visited1 = [start] # Visited nodes of forward search
    visited2 = [goal] # Visited nodes of backward search
    parent1 = dict() # parent of every node in forward. It will be used to get full path from start to goal
    parent2 = dict() # parent of every node in backward. It will be used to get full path from start to goal
    intersect = -1 # -1 means not intersected

    while queue1 and queue2:
        bfs(graph, queue1, visited1, parent1)
        bfs(graph, queue2, visited2, parent2)

        intersect = intersection(visited1, visited2)
        # If intersection of nodes occur then no need to continue
        if intersect != -1:
            break

    path = [] # Empty path
    if intersect != -1:
        # Generate path from intersection node to start
        node = intersect
        while node != None:
            path.insert(0, node)
            node = parent1.get(node)

        # Generate path from intersection node to goal
        node = parent2.get(intersect) # No need to include intersected  node as it is already included
        while node != None:
            path.append(node)
            node = parent2.get(node)
    return path

        
g = Graph()
g.add(1, 2)
g.add(1, 3)
g.add(2, 3)
g.add(2, 4)
g.add(3, 5)
g.add(4, 6)
g.add(5, 7)
g.add(1, 8)
g.add(8, 9)
g.add(5, 0)
start = 9
goal = 0

path = bi_dir(g.graph, start, goal)
if not path:
    print("[-] Path Not Found")
else:
    print("[+] ", path)
#
#       1___
#      / \  \
#     2---3  8
#    /     \  \
#   4       5  9
#  /       / \
# 6       0   7

