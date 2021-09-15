#This is the principal program
import os
import time

from aStar import *
from State import *

#load two tables of a text file using a path and a file
def loadTxt(path, file):
    numbers = []
    lineaNumeros = []
    elements = 0
    #open the file
    try:
        with open(f"{path}/{file}","r") as archivo:
            for linea in archivo:
                #erases the jumps ("\n"), split into space and convert in numbers
                lineaNumeros = list(map(lambda n : int(n) , linea.replace("\n","").split(" ")))
                numbers.append(lineaNumeros)
        elements = len(numbers)
        #return initial and final states
        return [numbers[i] for i in range(0,int(elements/2))], [numbers[i] for i in range(int(elements/2),elements)]
    except:
        print("Archivo no encontrado.")
    return [],[]

def printSequency(state):
    states = []
    while (state != None):
        states.append(state.table)
        state = state.father
    for i in range(1,len(states)+1):
        print(f"Estado N°{i}:")
        print(states.pop(-1))

def menu():
    actions = ["l","u","r","d"]
    nameTxt = "15_pieces/case7.txt"
    initialTable, goalTable = loadTxt(os.path.abspath(os.getcwd()), nameTxt)
    initialState = State(initialTable)
    goalState = State(goalTable)
    incise = -1
    functionH = lambda x,y: 1
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
            nameTxt = input()
            initialTable, goalTable = loadTxt(os.path.abspath(os.getcwd()), nameTxt)
            initialState = State(initialTable)
            goalState = State(goalTable)
        elif(incise == 2):
            functionH = piecesOutOfPlace
        elif(incise == 3):
            functionH = manhattanDistance
        elif(incise == 4):
            functionH = inversePermutation
        if (incise >= 2 and incise <= 4):
            init = time.time()
            request, state,counter = AStar(initialState,goalState,actions, functionH)
            end = time.time()
            print("RESULTADOS:")
            printSequency(state)
            print(("" if request else "no ") + "se hallo la ruta al objetivo.")
            print(f"Se expandio {counter} estados.")
            print(f"tiempo de ejecucion f{round(end-init,2)} seg.")
        input("presione enter para continuar.")

menu()

'''
case 4
'''