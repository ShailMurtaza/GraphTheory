#!/usr/bin/python

class Puzzle:
    MOVES = {
            "UP": -3,
            "DOWN": 3,
            "RIGHT": 1,
            "LEFT": -1
    }
    def __init__(self, matrix):
        self.matrix = matrix

    # Find index of space/0 in puzzle
    def get_space(self):
        for i, x in enumerate(self.matrix):
            if x == 0:
                return i
        return 0

    # Swap space with given index
    def space_swap(self, space_index, index):
        self.matrix[space_index] = self.matrix[index]
        self.matrix[index] = 0

    def move_up(self):
        space_index = self.get_space()
        index = space_index + self.MOVES["UP"]
        # Can't move up if new index is < 0
        if index < 0:
            return False
        self.space_swap(space_index, index)
        return True

    def move_down(self):
        space_index = self.get_space()
        index = space_index + self.MOVES["DOWN"]
        # Can't move down if new index is > 8
        if index > 8:
            return False
        self.space_swap(space_index, index)
        return True

    def move_right(self):
        space_index = self.get_space()
        index = space_index + self.MOVES["RIGHT"]
        # Can't move right if space index + 1 is divisible by 3
        # 0 is divisble by 3. But at index 0 we can move right. So I had to +1
        if (space_index+1) % 3 == 0:
            return False
        self.space_swap(space_index, index)
        return True

    def move_left(self):
        space_index = self.get_space()
        index = space_index + self.MOVES["LEFT"]
        # Can't move  left if space index is divisible by 3 (0, 3, 6)
        if space_index % 3 == 0:
            return False
        self.space_swap(space_index, index)
        return True


    def print(self):
        print("▁"*9)
        for i, x in enumerate(self.matrix):
            if i % 3 == 0:
                print("▏", end="")
            if x == 0:
                print("░", end=' ▏')
            else:
                print(x, end=' ▏')
            if (i+1) % 3 == 0:
                print("")
        print("▔"*9)


def BFS(start, goal):
    MOVES = ["UP", "DOWN", "RIGHT", "LEFT"]
    queue = [start]
    visited = [start]
    parent = [] # Store parent of each state to find find at the end
    path_found = False
    while queue:
        n = queue.pop(0)
        Puzzle(n).print()
        if n == goal:
            path_found = True
            break
        # Iterate over every move
        for move in MOVES:
            # Create copy of n state because if not then it will be manipulated by moves below
            puzzle = Puzzle(n.copy())
            if move == "UP":
                puzzle.move_up()
            elif move == "DOWN":
                puzzle.move_down()
            elif move == "RIGHT":
                puzzle.move_right()
            elif move == "LEFT":
                puzzle.move_left()
            if puzzle.matrix not in visited:
                queue.append(puzzle.matrix)
                visited.append(puzzle.matrix)
                # Append current state, parent of current state, move used to achieve this state
                parent.append((puzzle.matrix, n, move))
    path = []
    if path_found:
        n = goal # Start searching from goal
        found = True
        while found:
            found = False
            for i in parent:
                # If state is equal to first part of tupple then append parent of this n state, move to achieve state n.
                if i[0] == n:
                    path.append((i[0], i[2]))
                    n = i[1]
                    found = True
        # Last, initial state has None move to achieve itself
        path.append((n, None))
        path.reverse()
    return path



start = [
        1, 2, 3,
        7, 4, 5,
        0, 8, 6
        ]


start = [7, 4, 5, 8, 3, 1, 2, 0, 6]
goal = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 0
        ]

path = BFS(start, goal)
if path:
    print("_"*20, "SOLUTION FOUND", "_"*20)
    for i in path:
        Puzzle(i[0]).print()
        print(i[1])


