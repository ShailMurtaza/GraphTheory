#!/usr/bin/python
from graph import Graph

def dfs(find, v, graph):
    stack = []
    visited = []

    stack.append(v)
    visited.append(v)

    while stack:
        v = stack.pop()
        print(v)
        if v == find:
            return True
        for i in graph[v]:
            if not (i in visited):
                stack.append(i)
                visited.append(i)
    return False


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

start = 1
find = 8
if dfs(find, start, g.graph):
    print("[+] Found", find)
else:
    print("[-] Not Found", find)

#
#       1___
#      / \  \
#     2---3  8
#    /     \  \
#   4       5  9
#  /         \
# 6           7


