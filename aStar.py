from os import close, stat
from tfOFNPuzzle import *
from State import State
from collections import deque 
import queue
import time
def flatten(t):
    return [item for sublist in t for item in sublist]
def cost():
    return 1
def manhattanDistance(state , goalState):
    limitRow = len(state.table)
    limitColumn = len(state.table[0])
    distance = 0
    for row in range(limitRow):
        for col in range(limitColumn):
            r,c = findElement(goalState, state.table[row][col])
            distance += abs(row-r)+abs(col-c)
    return distance
def inverseState(state, goalstate):
    weight = 0
    index = 0
    elements = flatten(state.table)
    limit = len(elements)
    for element in elements:
        position = index + 1
        numberWeight = 0
        while (position < limit - 1):
            if (element > elements[position]):
                numberWeight += 1
            position = position + 1
        weight += numberWeight
        index = index + 1
    return weight


def AStar(initialState, goalState, actions,functionH):
    open = queue.PriorityQueue()
    initialState.f = 0
    open.put(initialState)
    closed = []
    counter = 0
    while(open.qsize()!=0):
        state = open.get()
        counter += 1
        closed.append(state)
        if (goalTest(state, goalState)):
            return True, state, counter
        for action in actions:
            if (evaluateAction(state, action) == False):
                continue
            succesor = TF(state, action)
            if (succesor in closed):
                continue
            succesor.h = functionH(succesor,goalState)
            succesor.g = state.g + cost()
            succesor.f = succesor.h + succesor.g
            succesor.father = state
            if (succesor in open.queue):
                if (succesor.g >= state in open.queue):
                    continue
            open.put(succesor)
    return False, state,counter

#res, state = AStar(State([[2,3],[1,0]]),State([[1,2],[3,0]]),["l","u","r","d"],inverseState)
def printSequency(state):
    while (state != None):
        states.append(state.table)
        state = state.father
    for i in range(1,len(states)+1):
        print(f"Estado N°{i}:")
        print(states.pop(-1))
    
res, state,counter = AStar(State([[5,1,3,4],[2,10,6,7],[9,0,12,8],[13,14,11,15]]),State([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]),["l","u","r","d"],inverseState)
states = []
printSequency(state)

print(f"Se expandio {counter} estados.")


# hea
# https://docs.python.org/es/3/library/heapq.html
#def __lt__ 
# https://www.daleseo.com/python-lt-not-supported/z


#6058
#171
#27
table1 = [[5,1,3,4],[2,10,6,7],[9,0,12,8],[13,14,11,15]]
table2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
initialState = State(table1)
goalState = State(table2)
request = False
state = None
counter = 0
actions = ["l","u","r","d"]
def menu():
    incise = -1
    while (incise != 0):
        print("MENU DE A STAR")
        print("-------------------------------------")
        print("1. Ingresar documento de texto y cargar.")
        print("2. Resolver con diferencia de tablas.")
        print("3. Resolver con distancia Manhattan.")
        print("4. Resolver con matriz inversa.")
        print("0. Salir.")
        incise = int(input())
        if (incise == 1):
            continue
        elif(incise == 2):
            request, state,counter = AStar(initialState,goalState,actions, countDiferencesOfTables)
        elif(incise == 3):
            request, state,counter = AStar(initialState,goalState,actions, manhattanDistance)
        elif(incise == 4):
            request, state,counter = AStar(initialState,goalState,actions, inverseState)
        if (incise >= 2 and incise <= 4):
            print("RESULTADOS:")
            printSequency(state)
            print(("no " if request else "") + "se hallo la ruta al objetivo.")
            print(f"Se expandio {counter} estados.")

