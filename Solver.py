from State import State
from PriorityQueue import PriorityQueue
from collections import deque

class solver:
    def __init__(self, StartStates, GoalStates):
        self.StartStates = self.toList(StartStates)
        self.GoalStates = GoalStates

    def toList(self,data):
        return [j for sub in data for j in sub]

    def move(self, data, dir):
        index = data.state.index(0)
        index = (int(index/3), int(index%3))
        newData = data.getMatrix()
        newIndex = (0,0)

        if(dir == 1): #up
            newIndex = (index[0] - 1, index[1])
        elif(dir == 2): #down
            newIndex = (index[0] + 1, index[1])
        elif(dir == 3): #left
            newIndex = (index[0], index[1] - 1)
        elif(dir == 4): #right
            newIndex = (index[0], index[1] + 1)
        
        if(not ((newIndex[0] >= 0 and newIndex[0] <= 2) and (newIndex[1] >= 0 and newIndex[1] <= 2))): return None
        
        temp = newData[newIndex[0]][newIndex[1]]
        newData[newIndex[0]][newIndex[1]] = newData[index[0]][index[1]]
        newData[index[0]][index[1]] = temp

        return self.toList(newData)


    def DFS(self):

        isVisited, stack = list(), list()

        stack.append(State(self.StartStates, None, 0, 0))

        while stack:
            node = stack.pop()
            isVisited.append(node.state)

            if(node.state == self.GoalStates): return node
            
            #expand
            neighbors = list()
            for i in range(1, 5):
                nextState = self.move(node, i)
                if(nextState): neighbors.append(State(nextState, node, node.depth + 1, node.cost + 1))
            
            for neighbor in neighbors:
                if(neighbor.state not in isVisited): stack.append(neighbor)
        
        return None

    def DLS(self, MaxDepth):

        isVisited, stack = list(), list()

        stack.append(State(self.StartStates, None, 0, 0))

        while stack:
            node = stack.pop()
            isVisited.append(node.state)

            if(node.state == self.GoalStates): return node
            elif(node.depth == MaxDepth): return None

            #expand
            neighbors = list()
            for i in range(1, 5):
                nextState = self.move(node, i)
                if(nextState): neighbors.append(State(nextState, node, node.depth + 1, node.cost + 1))
            
            for neighbor in neighbors:
                if(neighbor.state not in isVisited): stack.append(neighbor)
        
        return None

    def BFS(self):

        isVisited, queue = list(), deque()

        queue.append(State(self.StartStates, None, 0, 0))

        while(queue):
            node = queue.popleft()
            isVisited.append(node.state)

            if(node.state == self.GoalStates): return node

            #expand
            neighbors = list()
            for i in range(1, 5):
                nextState = self.move(node, i)
                if(nextState): neighbors.append(State(nextState, node, node.depth + 1, node.cost + 1))
            
            for neighbor in neighbors:
                if(neighbor.state not in isVisited): queue.append(neighbor)

        return None

    def Dijkstra(self):

        isVisited, queue = list(), PriorityQueue()

        queue.push(State(self.StartStates, None, 0, 0))

        while(queue):
            node = queue.pop()
            isVisited.append(node.state)

            if(node.state == self.GoalStates): return node

            #expand
            neighbors = list()
            for i in range(1, 5):
                nextState = self.move(node, i)
                if(nextState): neighbors.append(State(nextState, node, node.depth + 1, node.cost + 1))
            
            for neighbor in neighbors:
                if(neighbor.state not in isVisited): queue.push(neighbor)

        return None

    def ast(self):

        isVisited, queue = list(), PriorityQueue()

        queue.push(State(self.StartStates, None, 0, 0, GoalStates=self.GoalStates, heuristic=True))

        while(queue):
            node = queue.pop()
            isVisited.append(node.state)

            if(node.state == self.GoalStates): return node

            #expand
            neighbors = list()
            for i in range(1, 5):
                nextState = self.move(node, i)
                if(nextState): neighbors.append(State(nextState, node, node.depth + 1, node.cost + 1, GoalStates=self.GoalStates, heuristic=True))
            
            for neighbor in neighbors:
                if(neighbor.state not in isVisited): queue.push(neighbor)

        return None

    def isSolvable(self):

        inv_count = 0

        for i in range (0, 8):
            for j in range(i+1, 9):
                if (self.StartStates[j] and self.StartStates[i] and self.StartStates[i] > self.StartStates[j]): inv_count += 1

        return (inv_count%2) == 0

    def PrintSteps(self,nodes):
        
        for node in reversed(nodes):
            count = 0
            while(count <= 6):
                print(node[count], node[count+1], node[count+2])
                count += 3
            print()

    def traverse(self, node):

        res = list()

        while(node):
            res.append(node.state)
            node = node.parent
        
        self.PrintSteps(res)