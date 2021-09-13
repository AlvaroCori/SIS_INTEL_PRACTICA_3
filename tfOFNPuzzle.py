import copy
def countDiferencesOfTables(state, goalState):
    row = len(state.table) 
    col = row
    count = 0
    for r in range(row):
        for c in range(col):
            if (state.table[r][c] != goalState.table[r][c]):
                count += 1
    return count
def countParents(state):
    count = 0
    while (state!= None):
        count += 1
        state = state.father
    return count

#Search the element n and return the position
def findElement(state,n):
    rows = len(state.table)
    columns = len(state.table[0])
    for row in range(rows):
        for col in range(columns):
            if (state.table[row][col] == n):
                return row, col
    return -1, -1

#Swap two elements of a table
def swap(state, r1, c1, r2,c2):
    aux = state.table[r1][c1]
    state.table[r1][c1] = state.table[r2][c2]
    state.table[r2][c2] = aux

#Compare all elements of 2 tables
def goalTest(state, goalState):
    rows = len(goalState.table)
    columns = len(goalState.table[0])
    for row in range(rows):
        for col in range(columns):
            if (state.table[row][col] != goalState.table[row][col]):
                return False
    return True

def functionL(state, goalState):
    return countDiferencesOfTables(state, goalState) + countParents(state)


def evaluateAction(state, action):
    row, col = findElement(state, 0)
    rows = len(state.table) -1 
    columns = len(state.table[0]) -1
    #conditions for the 4 corners
    if (row == 0 and col==0):        
        return action=="r" or action =="d"
    elif (row == 0 and col==columns):
        return action=="l" or action =="d"  
    elif (row == rows and col==0):
        return action=="u" or action =="r" 
    elif (row == rows and col==columns):
        return action=="l" or action =="u"  
    #if the empty position don't be a corner, the alghoritm see the borders
    elif (col == 0): 
        return action=="u" or action =="r" or action =="d" 
    elif (row == 0):
        return action=="l" or action =="r" or action =="d"
    elif (col == columns):
        return action=="l" or action =="u" or action =="d"
    elif (row == rows):
        return action=="l" or action =="u" or action =="r" #fin
    #if the position is inside
    return True

#the transiction function change the new state
def TF(state, action):
    #deepcopy copy a new object incluse the lists inside of a object
    newState = copy.deepcopy(state)
    row, col = findElement(state,0)
    if (action == "l"):
        swap(newState,row,col,row,col-1)
    elif (action == "u"):
        swap(newState,row,col,row-1,col)
    elif (action == "r"):
        swap(newState,row,col,row,col+1)
    elif (action == "d"):
        swap(newState,row,col,row+1,col)
    return newState

#evaluate if a father have the same state (evit the repeat states).
def evaluateRepeatState(state):
    actual = state
    walker = state.father
    while (walker != None):
        if (goalTest(actual,walker)):
            return False
        walker = walker.father
    return True
def insertSuccessors(states, newStates,goalState):
    for s in newStates:
        states.insert([functionL(s, goalState),s])