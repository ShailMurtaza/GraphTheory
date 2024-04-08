# Implementation of Un-Directed graph using adjacent list
class Graph:
    def __init__(self):
        self.graph = {}

    def add(self, a, b):
        if not self.graph.get(a):
            self.graph[a] = []
        if not self.graph.get(b):
            self.graph[b] = []
        self.graph[a].append(b)
        self.graph[b].append(a)

