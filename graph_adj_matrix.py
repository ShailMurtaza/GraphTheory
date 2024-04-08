#       0
#      / \
#     1   2
#    /   / \
#    5__4   3

def DFS(matrix, start):
    stack = [start]
    visited = [start]
    while stack:
        n = stack.pop()
        neighbors = []
        for i, x in enumerate(matrix[n]):
            # If (x == 1) -> n is neighbor of i
            if x and i not in visited:
                stack.append(i)
                visited.append(i)
            if x:
                neighbors.append(i)
        print(n, "=>", neighbors)



class Graph:
    def __init__(self, n):
        self.matrix = []
        self.n = n
        # Create n by n martix
        for _ in range(n):
            self.matrix.append([0] * 6)

    def print(self):
        x = 0
        print("   ", end='')
        for i in range(len(self.matrix)):
            print(i, end='  ')
        print("")
        for i in self.matrix:
            print(x, i)
            x += 1
    # Add new node to graph
    def add(self, a, b):
        self.matrix[a][b] = 1
        self.matrix[b][a] = 1


g = Graph(6)

g.add(0, 1)
g.add(0, 2)
g.add(2, 3)
g.add(2, 4)
g.add(4, 5)
g.add(1, 5)

DFS(g.matrix, 3)
