# SIS_INTEL_PRACTICA_3
Practica 3 de Sistemas Inteligentes A Star.

Description Of Problem
The 8 puzzle is a game invented in 1874 by Noyes Palmer Chapmen base in a table of 3x3 cells equals in size with 8 pieces and a free space. The objective of the game is moving the pieces in the free space (at the left, at the up, at the right and at the down) for get an order that form a sequence of number or more popularity the numbers are replaced for an imagen.
The complexity also can have a minor or mayor size if we take a table of 2x2 or a table of 4x4 with 3 pieces and 15 pieces in that sequence, the movements that are required can be of a singular number of attempts until a centesimal number of attempts.
The initial state can derive in more states that have other states of transition. If we don’t get states that we already took the space of states is finite and we can approximate at many solutions without go at a deep sequency but we need to take an algorithm.
Description Of Solution
The solution of the algorithm is various previously we implemented the Breadth First Search BFS and the iterative deepening (ID) in this practice we will resolve with the algorithm Star A that belong at the conjunct of informed search algorithm, the Star A use heuristic functions to take a path toward the goal.
Heuristic Function
A heuristic function is a function of estimation that determine what node the program should take. The function evaluates a state in order to the less or greater weight be a candidate to take the next step.
Star A (*A)
This algorithm is well knowledge in artificial intelligence, the algorithm uses two heuristics function to take the next state. The heuristic function that takes the algorithm is h(m) the minimal path of the actual state with the goal state and the g(m) the minimal path to the actual state with the initial state. Both functions are unknown and we need to estimate an approximate of  this minimal paths.
The algorithm also uses a priority queue so that the minimal weight of states can be order in ascending order so we can take the first in the queue that have the minimal weight of all possibilities.
Remember also that a heuristic function is admissible with “n” (state or node) if satisfice 3 conditions:
•	Each state n has a finite number of successors (if any).
•	The cost c of going from one state n to another m, has to be c > e, for e > 0.
•	For all states n belonging to state space, hˆ(n) <= h(n).
If hˆ(n) > h(n) is a overestimate function. 
If hˆ(n) > h(n) is a underestimate function.
If hˆ(n) is permissible, then the algorithm A that uses it is optimal.

We will implement 3 different heuristics functions:
hˆ 1(n). - Number of pieces out of place relative to the target state, count the difference in the pieces of a state and the goal state.
hˆ 2(n). – Sum the Manhattan distance. For every piece count the vertical and horizontal distance comparing the initial state and the goal state.
hˆ 3(n). – Sum of the inverse permutations. Consist in applanate the matrix or table to a vector, and for every piece compare and count the smaller numbers to which we leave, only we can use this function if the goal state has an order.
Python
We use the language Python because this language have a large collection of util libraries, In this exercise a clarity preference in order to use Python is the pass of parameters for Functions because we are pass the heuristic function like a variable.
Python also is a language applicable and recommendable for the Intelligence Artificial because the syntax helps much in the development.
Experiments And Results
Experiments with 8-Puzzle

Experiment N° 1 
Initial state = [3,2,5],[4,8,1],[0,7,6]
Goal state = [1,2,3],[4,5,6],[7,8,0]

With Table difference: h1
State N°1: [[3, 2, 5], [4, 8, 1], [0, 7, 6]]
State N°2: [[3, 2, 5], [4, 8, 1], [7, 0, 6]]
State N°3: [[3, 2, 5], [4, 0, 1], [7, 8, 6]]
State N°4: [[3, 0, 5], [4, 2, 1], [7, 8, 6]]
State N°5: [[0, 3, 5], [4, 2, 1], [7, 8, 6]]
State N°6: [[4, 3, 5], [0, 2, 1], [7, 8, 6]]
State N°7: [[4, 3, 5], [2, 0, 1], [7, 8, 6]]
State N°8: [[4, 3, 5], [2, 1, 0], [7, 8, 6]]
State N°9: [[4, 3, 0], [2, 1, 5], [7, 8, 6]]
State N°10: [[4, 0, 3], [2, 1, 5], [7, 8, 6]]
State N°11: [[4, 1, 3], [2, 0, 5], [7, 8, 6]]
State N°12: [[4, 1, 3], [0, 2, 5], [7, 8, 6]]
State N°13: [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
State N°14: [[1, 0, 3], [4, 2, 5], [7, 8, 6]]
State N°15: [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
State N°16: [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
State N°17: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 554 States.
Execution time: 1.53 seg.

With Manhattan distances
State N°1: [[3, 2, 5], [4, 8, 1], [0, 7, 6]]
State N°2: [[3, 2, 5], [4, 8, 1], [7, 0, 6]]
State N°3: [[3, 2, 5], [4, 0, 1], [7, 8, 6]]
State N°4: [[3, 0, 5], [4, 2, 1], [7, 8, 6]]
State N°5: [[0, 3, 5], [4, 2, 1], [7, 8, 6]]
State N°6: [[4, 3, 5], [0, 2, 1], [7, 8, 6]]
State N°7: [[4, 3, 5], [2, 0, 1], [7, 8, 6]]
State N°8: [[4, 3, 5], [2, 1, 0], [7, 8, 6]]
State N°9: [[4, 3, 0], [2, 1, 5], [7, 8, 6]]
State N°10: [[4, 0, 3], [2, 1, 5], [7, 8, 6]]
State N°11: [[4, 1, 3], [2, 0, 5], [7, 8, 6]]
State N°12: [[4, 1, 3], [0, 2, 5], [7, 8, 6]]
State N°13: [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
State N°14: [[1, 0, 3], [4, 2, 5], [7, 8, 6]]
State N°15: [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
State N°16: [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
State N°17: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 180 States.
Execution time: 0.47 seg.

With Inverse matrix
State N°1: [[3, 2, 5], [4, 8, 1], [0, 7, 6]]
State N°2: [[3, 2, 5], [4, 8, 1], [7, 0, 6]]
State N°3: [[3, 2, 5], [4, 0, 1], [7, 8, 6]]
State N°4: [[3, 0, 5], [4, 2, 1], [7, 8, 6]]
State N°5: [[0, 3, 5], [4, 2, 1], [7, 8, 6]]
State N°6: [[4, 3, 5], [0, 2, 1], [7, 8, 6]]
State N°7: [[4, 3, 5], [2, 0, 1], [7, 8, 6]]
State N°8: [[4, 3, 5], [2, 1, 0], [7, 8, 6]]
State N°9: [[4, 3, 0], [2, 1, 5], [7, 8, 6]]
State N°10: [[4, 0, 3], [2, 1, 5], [7, 8, 6]]
State N°11: [[4, 1, 3], [2, 0, 5], [7, 8, 6]]
State N°12: [[4, 1, 3], [0, 2, 5], [7, 8, 6]]
State N°13: [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
State N°14: [[1, 0, 3], [4, 2, 5], [7, 8, 6]]
State N°15: [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
State N°16: [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
State N°17: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 429 States.
Execution time: 1.24 seg.

Experiment  N° 2
Initial state = [4,1,3],[8,0,5],[2,7,6]
Goal state = [1,2,3],[4,5,6],[7,8,0]
With Table difference: h1
State N°1: [[4, 1, 3], [8, 0, 5], [2, 7, 6]]
State N°2: [[4, 1, 3], [0, 8, 5], [2, 7, 6]]
State N°3: [[4, 1, 3], [2, 8, 5], [0, 7, 6]]
State N°4: [[4, 1, 3], [2, 8, 5], [7, 0, 6]]
State N°5: [[4, 1, 3], [2, 0, 5], [7, 8, 6]]
State N°6: [[4, 1, 3], [0, 2, 5], [7, 8, 6]]
State N°7: [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
State N°8: [[1, 0, 3], [4, 2, 5], [7, 8, 6]]
State N°9: [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
State N°10: [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
State N°11: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 43 States.
Execution time: 0.07 seg.

With Manhattan distances
State N°1: [[4, 1, 3], [8, 0, 5], [2, 7, 6]]
State N°2: [[4, 1, 3], [0, 8, 5], [2, 7, 6]]
State N°3: [[4, 1, 3], [2, 8, 5], [0, 7, 6]]
State N°4: [[4, 1, 3], [2, 8, 5], [7, 0, 6]]
State N°5: [[4, 1, 3], [2, 0, 5], [7, 8, 6]]
State N°6: [[4, 1, 3], [0, 2, 5], [7, 8, 6]]
State N°7: [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
State N°8: [[1, 0, 3], [4, 2, 5], [7, 8, 6]]
State N°9: [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
State N°10: [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
State N°11: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 29 States.
Execution time: 0.05 seg.

With Inverse matrix:
State N°1: [[4, 1, 3], [8, 0, 5], [2, 7, 6]]
State N°2: [[4, 1, 3], [0, 8, 5], [2, 7, 6]]
State N°3: [[4, 1, 3], [2, 8, 5], [0, 7, 6]]
State N°4: [[4, 1, 3], [2, 8, 5], [7, 0, 6]]
State N°5: [[4, 1, 3], [2, 0, 5], [7, 8, 6]]
State N°6: [[4, 1, 3], [0, 2, 5], [7, 8, 6]]
State N°7: [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
State N°8: [[1, 0, 3], [4, 2, 5], [7, 8, 6]]
State N°9: [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
State N°10: [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
State N°11: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 39 States.
Execution time: 0.07 seg.

Experiment  N° 3
Initial state = [7,2,0],[5,1,4],[8,6,3]
Goal state = [1,2,3],[4,5,6],[7,8,0]

With Table difference: h1:
State N°1: [[7, 2, 0], [5, 1, 4], [8, 6, 3]]
State N°2: [[7, 0, 2], [5, 1, 4], [8, 6, 3]]
State N°3: [[7, 1, 2], [5, 0, 4], [8, 6, 3]]
State N°4: [[7, 1, 2], [0, 5, 4], [8, 6, 3]]
State N°5: [[0, 1, 2], [7, 5, 4], [8, 6, 3]]
State N°6: [[1, 0, 2], [7, 5, 4], [8, 6, 3]]
State N°7: [[1, 5, 2], [7, 0, 4], [8, 6, 3]]
State N°8: [[1, 5, 2], [7, 4, 0], [8, 6, 3]]
State N°9: [[1, 5, 2], [7, 4, 3], [8, 6, 0]]
State N°10: [[1, 5, 2], [7, 4, 3], [8, 0, 6]]
State N°11: [[1, 5, 2], [7, 4, 3], [0, 8, 6]]
State N°12: [[1, 5, 2], [0, 4, 3], [7, 8, 6]]
State N°13: [[1, 5, 2], [4, 0, 3], [7, 8, 6]]
State N°14: [[1, 0, 2], [4, 5, 3], [7, 8, 6]]
State N°15: [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
State N°16: [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
State N°17: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 497 States.
Execution time: 1.34 seg.

With Manhattan distances:
State N°1: [[7, 2, 0], [5, 1, 4], [8, 6, 3]]
State N°2: [[7, 0, 2], [5, 1, 4], [8, 6, 3]]
State N°3: [[7, 1, 2], [5, 0, 4], [8, 6, 3]]
State N°4: [[7, 1, 2], [0, 5, 4], [8, 6, 3]]
State N°5: [[0, 1, 2], [7, 5, 4], [8, 6, 3]]
State N°6: [[1, 0, 2], [7, 5, 4], [8, 6, 3]]
State N°7: [[1, 5, 2], [7, 0, 4], [8, 6, 3]]
State N°8: [[1, 5, 2], [7, 4, 0], [8, 6, 3]]
State N°9: [[1, 5, 2], [7, 4, 3], [8, 6, 0]]
State N°10: [[1, 5, 2], [7, 4, 3], [8, 0, 6]]
State N°11: [[1, 5, 2], [7, 4, 3], [0, 8, 6]]
State N°12: [[1, 5, 2], [0, 4, 3], [7, 8, 6]]
State N°13: [[1, 5, 2], [4, 0, 3], [7, 8, 6]]
State N°14: [[1, 0, 2], [4, 5, 3], [7, 8, 6]]
State N°15: [[1, 2, 0], [4, 5, 3], [7, 8, 6]]
State N°16: [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
State N°17: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 65 States.
Execution time: 0.15 seg.

With Inverse matrix:
State N°1: [[7, 2, 0], [5, 1, 4], [8, 6, 3]]
State N°2: [[7, 0, 2], [5, 1, 4], [8, 6, 3]]
State N°3: [[7, 1, 2], [5, 0, 4], [8, 6, 3]]
State N°4: [[7, 1, 2], [5, 4, 0], [8, 6, 3]]
State N°5: [[7, 1, 2], [5, 4, 3], [8, 6, 0]]
State N°6: [[7, 1, 2], [5, 4, 3], [8, 0, 6]]
State N°7: [[7, 1, 2], [5, 0, 3], [8, 4, 6]]
State N°8: [[7, 1, 2], [0, 5, 3], [8, 4, 6]]
State N°9: [[0, 1, 2], [7, 5, 3], [8, 4, 6]]
State N°10: [[1, 0, 2], [7, 5, 3], [8, 4, 6]]
State N°11: [[1, 2, 0], [7, 5, 3], [8, 4, 6]]
State N°12: [[1, 2, 3], [7, 5, 0], [8, 4, 6]]
State N°13: [[1, 2, 3], [7, 0, 5], [8, 4, 6]]
State N°14: [[1, 2, 3], [7, 4, 5], [8, 0, 6]]
State N°15: [[1, 2, 3], [7, 4, 5], [0, 8, 6]]
State N°16: [[1, 2, 3], [0, 4, 5], [7, 8, 6]]
State N°17: [[1, 2, 3], [4, 0, 5], [7, 8, 6]]
State N°18: [[1, 2, 3], [4, 5, 0], [7, 8, 6]]
State N°19: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 615 States.
Execution time: 2.09 seg.


Experiments with 15-Puzzle

Experiment N° 1 
Initial state = [5,1,3,4],[2,10,6,7],[9,0,12,8],[13,15,11,15]
Goal state = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]
Table difference: h1
RESULTADOS:
State N°1: [[5, 1, 3, 4], [2, 10, 6, 7], [9, 0, 12, 8], [13, 14, 11, 15]]
State N°2: [[5, 1, 3, 4], [2, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°3: [[5, 1, 3, 4], [0, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°4: [[0, 1, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°5: [[1, 0, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°6: [[1, 2, 3, 4], [5, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°7: [[1, 2, 3, 4], [5, 6, 0, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°8: [[1, 2, 3, 4], [5, 6, 7, 0], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°9: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 12, 0], [13, 14, 11, 15]]
State N°10: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 11, 15]]
State N°11: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
State N°12: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
It expanded 27 States.
Execution time: 0.06 seg.
With Manhattan distances:
State N°1: [[5, 1, 3, 4], [2, 10, 6, 7], [9, 0, 12, 8], [13, 14, 11, 15]]
State N°2: [[5, 1, 3, 4], [2, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°3: [[5, 1, 3, 4], [0, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°4: [[0, 1, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°5: [[1, 0, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°6: [[1, 2, 3, 4], [5, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°7: [[1, 2, 3, 4], [5, 6, 0, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°8: [[1, 2, 3, 4], [5, 6, 7, 0], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°9: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 12, 0], [13, 14, 11, 15]]
State N°10: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 11, 15]]
State N°11: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
State N°12: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
It expanded 39 States.
Execution time: 0.11 seg.
With Inverse Matrix:
State N°1: [[5, 1, 3, 4], [2, 10, 6, 7], [9, 0, 12, 8], [13, 14, 11, 15]]
State N°2: [[5, 1, 3, 4], [2, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°3: [[5, 1, 3, 4], [0, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°4: [[0, 1, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°5: [[1, 0, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°6: [[1, 2, 3, 4], [5, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°7: [[1, 2, 3, 4], [5, 6, 0, 7], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°8: [[1, 2, 3, 4], [5, 6, 7, 0], [9, 10, 12, 8], [13, 14, 11, 15]]
State N°9: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 12, 0], [13, 14, 11, 15]]
State N°10: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 11, 15]]
State N°11: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
State N°12: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
It expanded  86 States.
Execution time: 0.31 seg.


Experiment N° 2
Initial state = [5,1,3,4],[2,10,6,7],[9,0,12,8],[13,15,11,15]
Goal state = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]
Table difference: h1

Manhattan distances

Inverse Matrix


Experiment N° 3
Initial state = [5,1,3,4],[2,10,6,7],[9,0,12,8],[13,15,11,15]
Goal state = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]
Table difference: h1

Manhattan distances

Inverse Matrix

Conclusions
Bibliography
       Queue (priorityQueue)
https://docs.python.org/3/library/queue.html

Function (__lt__) use for priorityQueue:
https://www.daleseo.com/python-lt-not-supported/z

Copy objects: (import copy):
https://pymotw.com/2/copy/

Obtain the actual path: (import os):
https://www.delftstack.com/es/howto/python/python-get-path/

Open input from file txt: 
https://decodigo.com/python-leer-un-archivo-de-texto
Visual and solver tree for 8-puzzle:
https://deniz.co/8-puzzle-solver/



1.	Descripción del problema: se describe qué problema se está queriendo resolver a nivel general.
2.	Descripción de la solución: se describe qué algoritmo se está utilizando, se justifica su elección y se detalla cómo se utiliza dicho algoritmo para resolver el problema.
3.	Experimentos y resultados: los experimentos que tienen que ser hechos estarán descritos en el documento del laboratorio; pero cualquier experimento adicional que el estudiante realice será bien recibido. Los resultados tienen que ser argumentados. 
4.	Conclusiones: basándose en las evidencias obtenidas de los resultados, el estudiante debe llegar a una conclusión.
5.	Bibliografía: todo material externo (enlaces de internet, tutoriales, libros, videos de YouTube, etc.) a la clase que se utilice para responder con el laboratorio tendrá que ser citado. Toda referencia sin citación será considerada plagio y el laboratorio será anulado. 
