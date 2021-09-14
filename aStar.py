from tfOFNPuzzle import *
from State import State
from queue import PriorityQueue

#Flatten the table
def flatten(t):
    return [item for sublist in t for item in sublist]

#Return the cost of transiction for levels
def cost():
    return 1

#H1: count the pieces out of place from state to goalstate
def piecesOutOfPlace(state, goalState):
    row = len(state.table) 
    col = row
    count = 0
    for r in range(row):
        for c in range(col):
            if (state.table[r][c] != goalState.table[r][c]):
                count += 1
    return count

#H2: count all mahattan distance of every state pieces
def manhattanDistance(state , goalState):
    limitRow = len(state.table)
    limitColumn = len(state.table[0])
    distance = 0
    for row in range(limitRow):
        for col in range(limitColumn):
            r,c = findElement(goalState, state.table[row][col])
            distance += abs(row-r)+abs(col-c)
    return distance

#H3: Count every inverse permutation of state pieces
def inversePermutation(state, goalstate):
    weight = 0
    index = 0
    elements = flatten(state.table)
    limit = len(elements)
    for element in elements:
        position = index + 1
        numberWeight = 0
        #Compare and count if the piece is mayor at the rest
        while (position < limit - 1):
            if (element > elements[position]):
                numberWeight += 1
            position = position + 1
        weight += numberWeight
        index = index + 1
    return weight
'''
The algoritm AStar
initialState: is the first state
goalState: is the final state searched
actions: are the movements that we can realize in the puzzles
functionH: is the heuristic function passed by parameters 
'''
def AStar(initialState, goalState, actions,functionH):
    open = PriorityQueue()
    initialState.f = 0
    open.put(initialState)
    closed = []
    counter = 0
    while(open.qsize()!=0):
        state = open.get()

        counter += 1
        closed.append(state.table)
        if (goalTest(state, goalState)):
            return True, state, counter
        for action in actions:
            if (evaluateAction(state, action) == False):
                continue
            succesor = TF(state, action)
            if (succesor.table in closed):
                continue
            succesor.h = functionH(succesor,goalState)
            succesor.g = state.g + cost()
            succesor.f = succesor.h + succesor.g
            succesor.father = state
            tables = list(map(lambda x: x.table ,open.queue))
            if (succesor.table in tables):
                index = tables.index(succesor.table)
                if (succesor.g >= open.queue[index].g):
                    continue
            open.put(succesor)
    return False, state,counter




    








table1 = [[5,1,3,4],[2,10,6,7],[9,0,12,8],[13,14,11,15]]
table2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
initialState = State(table1)
goalState = State(table2)
request = False
state = None
counter = 0
actions = ["l","u","r","d"]

