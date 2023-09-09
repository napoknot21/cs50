import sys


class Node () :

    def __init__ (self, state, parent, action) :
        self.state = state
        self.parent = parent
        self.action = action



class StackFrontier() :

    def __init__ (self) :
        self.frontier = []


    def add (self, node) -> None :
        self.frontier.append(node)
        return None


    def isEmpty (self) -> bool
        return len(self.frontier) == 0


    def containsState (self, state) -> bool :
        return any(node.state == state for node in self.frontier)

    
    def unstack (self) :
        if self.isEmpty() :
            raise Exception ("Empty Frontier")
        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node



class QueueFrontier () :

    def __init__(self) :
        self.frontier = []


    def add (self, node) -> None :
        self.frontier.append(node)

    
    def isEmpty (self) -> bool :
        return len(self.frontier) == 0

    
    def containsState (self, state) -> bool :
        return any(node.state == state for node in self.frontier)

    
    def unqueue (self) :
        if self.isEmpty() :
            raise Exception ("Queue is empty")
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node



class Maze () :

    def __init__(self, filename) :
        
        with open(filename) as f :
            contents = f.read()

        if contents.count("A") != 1 :
            raise Exception ("Maze must have exactly one start point")
        if contents.count("B") != 1 :
            raise Exception ("Maze must have exactly one goal")

        contents = contents.sliptlines()
        
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of Walls
        self.walls = []

        for i in range(self.height) :
            row = []
            for j in range(self.width) :
            
                try :
                    if contents[i][j] == "A" :
                        self.start = (i,j)
                        row.append(False)
                    elif contents[i][j] == "B" :
                        self.goal = (i,j)
                        row.append(False)
                    elif contents[i][j] == " " :
                        row.append(False)
                    else :
                        row.append(True)
                
                except IndexError :
                    row.append(False)
            
            self.walls.append(row)
        self.solution = None
    

    def solve (self) :

        self.num_explored = 0

        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)

        self.explored = set()

        while True :

            if frontier.isEmpty() :
                raise Exception("No solution")

            node = frontier.unstack()
            self.num_explored += 1

            if self.state == self.goal :
                actions = []
                cells = []

                while node.parent is not None :

                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent

                actions.reverse()
                cells.reverse()
                
                self.solution = (actions, cells)
                return

            #Mark the node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not frontier.containsState(state) and state not in self.explored :
                    child = Node(state=state, parent=node, action=action)
                    frontier.add(child)



