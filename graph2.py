class AdjacentNode:
	def __init__(self, vertex):
		self.vertex = vertex
		self.next = None

class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = [None] * self.vertices
		
	# Function for adding undirected edge 
	def add_edge(self, src, dest):
		node = AdjacentNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		node = AdjacentNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node
		
n = 15
dest = 14

# Create a graph
graph = Graph(n)
graph.add_edge(0, 4)
graph.add_edge(1, 4)
graph.add_edge(2, 5)
graph.add_edge(3, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 6)
graph.add_edge(6, 7)
graph.add_edge(7, 8)
graph.add_edge(8, 9)
graph.add_edge(8, 10)
graph.add_edge(9, 11)
graph.add_edge(9, 12)
graph.add_edge(10, 13)
graph.add_edge(10, 14)

g = graph.graph

for i in range(len(g)):
    print(i, end="->")
    n = g[i]
    while n:
        print(n.vertex, end="->")
        n = n.next
    print(n)
    print("-"*10)

exit()
while True:
    print(g[0].vertex)
    input()
