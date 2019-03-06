class State:
    def __init__(self, state, parent, depth, cost, GoalStates=[0], heuristic=False):
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.heuristic = 0 if not heuristic else self.countHeuristic(GoalStates)
    
    def getMatrix(self):
        return [self.state[i:i+3] for i in range(0, len(self.state), 3)]

    def countHeuristic(self, GoalStates):
        heuristic = 0
        data = self.getMatrix()

        for i in range(0,3):
            for j in range(0,3):
                index = GoalStates.index(data[i][j])
                index = (int(index/3), int(index%3))
                heuristic += abs(index[0] - i) + abs(index[1] - j)

        return heuristic
    
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)