# SIS_INTEL_PRACTICA_3
Practica 3 de Sistemas Inteligentes A Star.

Alvaro Bryan Cori Sanchez <br>
Omar Christian Arias Chavez


Description Of Problem
==========================

The 8 puzzle is a game invented in 1874 by Noyes Palmer Chapmen base in a table of 3x3 cells equals in size with 8 pieces and a free space. The objective of the game is moving the pieces in the free space (at the left, at the up, at the right and at the down) for get an order that form a sequence of number or more popularity the numbers are replaced for an imagen.
The complexity also can have a minor or mayor size if we take a table of 2x2 or a table of 4x4 with 3 pieces and 15 pieces in that sequence, the movements that are required can be of a singular number of attempts until a centesimal number of attempts.
The initial state can derive in more states that have other states of transition. If we don’t get states that we already took the space of states is finite and we can approximate at many solutions without go at a deep sequency but we need to take an algorithm.


Description Of Solution
==========================

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
Beans . - We will implement a heuristic function that we call diference of pieces, the function sum the absolute differences between the current state boxes and the target state boxes. For example abs(currentS(1,1) - goalS(1,1))+abs(currentS(2,1) - goalS(2,1))+...+abs(currentS(n,n) - goalS(n,n)).
Python
We use the language Python because this language have a large collection of util libraries, In this exercise a clarity preference in order to use Python is the pass of parameters for Functions because we are pass the heuristic function like a variable.
Python also is a language applicable and recommendable for the Intelligence Artificial because the syntax helps much in the development.


Experiments And Results
==========================

To the experiments, we took pages on the web to generate ramdon initial states

Experiments with 3-Puzzle
-------------------
The 3-Puzzle is easy to implement, we only see 2 cases because we can see the 
Experiment N° 1 

Initial state = [2,3],[1,0]
Goal state = [1,2],[3,0]

With Table difference: h1

Estado N°1: [[2, 3], [1, 0]] , Estado N°2: [[2, 0], [1, 3]] , Estado N°3: [[0, 2], [1, 3]] , Estado N°4: [[1, 2], [0, 3]] , Estado N°5: [[1, 2], [3, 0]]

It expanded 6 States.
Execution time: 0.01 seg. <br>

With Manhattan distances

Estado N°1: [[2, 3], [1, 0]] , Estado N°2: [[2, 0], [1, 3]] , Estado N°3: [[0, 2], [1, 3]] , Estado N°4: [[1, 2], [0, 3]] , Estado N°5: [[1, 2], [3, 0]]

It expanded 5 States.
Execution time: 0.0 seg.

With Inverse matrix

Estado N°1: [[2, 3], [1, 0]] , Estado N°2: [[2, 0], [1, 3]] , Estado N°3: [[0, 2], [1, 3]] , Estado N°4: [[1, 2], [0, 3]] , Estado N°5: [[1, 2], [3, 0]]

It expanded 8 States.
Execution time: 0.01 seg.


Experiment  N° 2

Initial state = [1,3],[2,0]
Goal state = [1,2],[3,0]

With Table difference: h1

Estado N°1: [[1, 3], [2, 0]] , Estado N°2: [[1, 0], [2, 3]] , Estado N°3: [[0, 1], [2, 3]] , Estado N°4: [[2, 1], [0, 3]] <br>
Estado N°5: [[2, 1], [3, 0]] , Estado N°6: [[2, 0], [3, 1]] , Estado N°7: [[0, 2], [3, 1]]

It expanded 13 States.
Execution time: 0.02 seg.

With Manhattan distances

Estado N°1: [[1, 3], [2, 0]] , Estado N°2: [[1, 0], [2, 3]] , Estado N°3: [[0, 1], [2, 3]] , Estado N°4: [[2, 1], [0, 3]] <br>
Estado N°5: [[2, 1], [3, 0]] , Estado N°6: [[2, 0], [3, 1]] , Estado N°7: [[0, 2], [3, 1]] 

It expanded 13 States.
Execution time: 0.01 seg.

With Inverse matrix:

Estado N°1: [[1, 3], [2, 0]] , Estado N°2: [[1, 0], [2, 3]] , Estado N°3: [[0, 1], [2, 3]] , Estado N°4: [[2, 1], [0, 3]] <br>
Estado N°5: [[2, 1], [3, 0]] , Estado N°6: [[2, 0], [3, 1]] , Estado N°7: [[0, 2], [3, 1]] , Estado N°8: [[3, 2], [0, 1]]

It expanded 13 States.
Execution time: 0.01 seg.


Experiments with 8-Puzzle
-------------------

Experiment N° 1 

Initial state = [3,2,5],[4,8,1],[0,7,6]
Goal state = [1,2,3],[4,5,6],[7,8,0]

With Table difference: h1

State N°1: [[3, 2, 5], [4, 8, 1], [0, 7, 6]] , State N°2: [[3, 2, 5], [4, 8, 1], [7, 0, 6]] , State N°3: [[3, 2, 5], [4, 0, 1], [7, 8, 6]] <br>
State N°4: [[3, 0, 5], [4, 2, 1], [7, 8, 6]] , State N°5: [[0, 3, 5], [4, 2, 1], [7, 8, 6]] , State N°6: [[4, 3, 5], [0, 2, 1], [7, 8, 6]] <br>
State N°7: [[4, 3, 5], [2, 0, 1], [7, 8, 6]] , State N°8: [[4, 3, 5], [2, 1, 0], [7, 8, 6]] , State N°9: [[4, 3, 0], [2, 1, 5], [7, 8, 6]] <br>
State N°10: [[4, 0, 3], [2, 1, 5], [7, 8, 6]] , State N°11: [[4, 1, 3], [2, 0, 5], [7, 8, 6]] , State N°12: [[4, 1, 3], [0, 2, 5], [7, 8, 6]] <br>
State N°13: [[0, 1, 3], [4, 2, 5], [7, 8, 6]] , State N°14: [[1, 0, 3], [4, 2, 5], [7, 8, 6]] , State N°15: [[1, 2, 3], [4, 0, 5], [7, 8, 6]] <br>
State N°16: [[1, 2, 3], [4, 5, 0], [7, 8, 6]] , State N°17: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 554 States.
Execution time: 1.53 seg.

With Manhattan distances

State N°1: [[3, 2, 5], [4, 8, 1], [0, 7, 6]] , State N°2: [[3, 2, 5], [4, 8, 1], [7, 0, 6]] , State N°3: [[3, 2, 5], [4, 0, 1], [7, 8, 6]] <br>
State N°4: [[3, 0, 5], [4, 2, 1], [7, 8, 6]] , State N°5: [[0, 3, 5], [4, 2, 1], [7, 8, 6]] , State N°6: [[4, 3, 5], [0, 2, 1], [7, 8, 6]] <br>
State N°7: [[4, 3, 5], [2, 0, 1], [7, 8, 6]] , State N°8: [[4, 3, 5], [2, 1, 0], [7, 8, 6]] , State N°9: [[4, 3, 0], [2, 1, 5], [7, 8, 6]] <br>
State N°10: [[4, 0, 3], [2, 1, 5], [7, 8, 6]] , State N°11: [[4, 1, 3], [2, 0, 5], [7, 8, 6]] , State N°12: [[4, 1, 3], [0, 2, 5], [7, 8, 6]] <br>
State N°13: [[0, 1, 3], [4, 2, 5], [7, 8, 6]] , State N°14: [[1, 0, 3], [4, 2, 5], [7, 8, 6]] , State N°15: [[1, 2, 3], [4, 0, 5], [7, 8, 6]] <br>
State N°16: [[1, 2, 3], [4, 5, 0], [7, 8, 6]] , State N°17: [[1, 2, 3], [4, 5, 6], [7, 8, 0]] <br>

It expanded 180 States.
Execution time: 0.47 seg.

With Inverse matrix

State N°1: [[3, 2, 5], [4, 8, 1], [0, 7, 6]] , State N°2: [[3, 2, 5], [4, 8, 1], [7, 0, 6]] , State N°3: [[3, 2, 5], [4, 0, 1], [7, 8, 6]] <br>
State N°4: [[3, 0, 5], [4, 2, 1], [7, 8, 6]] , State N°5: [[0, 3, 5], [4, 2, 1], [7, 8, 6]] , State N°6: [[4, 3, 5], [0, 2, 1], [7, 8, 6]] <br>
State N°7: [[4, 3, 5], [2, 0, 1], [7, 8, 6]] , State N°8: [[4, 3, 5], [2, 1, 0], [7, 8, 6]] , State N°9: [[4, 3, 0], [2, 1, 5], [7, 8, 6]] <br>
State N°10: [[4, 0, 3], [2, 1, 5], [7, 8, 6]] , State N°11: [[4, 1, 3], [2, 0, 5], [7, 8, 6]] , State N°12: [[4, 1, 3], [0, 2, 5], [7, 8, 6]] <br>
State N°13: [[0, 1, 3], [4, 2, 5], [7, 8, 6]] , State N°14: [[1, 0, 3], [4, 2, 5], [7, 8, 6]] , State N°15: [[1, 2, 3], [4, 0, 5], [7, 8, 6]] <br>
State N°16: [[1, 2, 3], [4, 5, 0], [7, 8, 6]] , State N°17: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 429 States.
Execution time: 1.24 seg.


Experiment  N° 2

Initial state = [4,1,3],[8,0,5],[2,7,6]
Goal state = [1,2,3],[4,5,6],[7,8,0]

With Table difference: h1

State N°1: [[4, 1, 3], [8, 0, 5], [2, 7, 6]] , State N°2: [[4, 1, 3], [0, 8, 5], [2, 7, 6]] , State N°3: [[4, 1, 3], [2, 8, 5], [0, 7, 6]] <br>
State N°4: [[4, 1, 3], [2, 8, 5], [7, 0, 6]] , State N°5: [[4, 1, 3], [2, 0, 5], [7, 8, 6]] , State N°6: [[4, 1, 3], [0, 2, 5], [7, 8, 6]] <br>
State N°7: [[0, 1, 3], [4, 2, 5], [7, 8, 6]] , State N°8: [[1, 0, 3], [4, 2, 5], [7, 8, 6]] , State N°9: [[1, 2, 3], [4, 0, 5], [7, 8, 6]] <br>
State N°10: [[1, 2, 3], [4, 5, 0], [7, 8, 6]] , State N°11: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 43 States.
Execution time: 0.07 seg.

With Manhattan distances

State N°1: [[4, 1, 3], [8, 0, 5], [2, 7, 6]] , State N°2: [[4, 1, 3], [0, 8, 5], [2, 7, 6]] , State N°3: [[4, 1, 3], [2, 8, 5], [0, 7, 6]] <br>
State N°4: [[4, 1, 3], [2, 8, 5], [7, 0, 6]] , State N°5: [[4, 1, 3], [2, 0, 5], [7, 8, 6]] , State N°6: [[4, 1, 3], [0, 2, 5], [7, 8, 6]] <br>
State N°7: [[0, 1, 3], [4, 2, 5], [7, 8, 6]] , State N°8: [[1, 0, 3], [4, 2, 5], [7, 8, 6]] , State N°9: [[1, 2, 3], [4, 0, 5], [7, 8, 6]] <br>
State N°10: [[1, 2, 3], [4, 5, 0], [7, 8, 6]] , State N°11: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 29 States.
Execution time: 0.05 seg.

With Inverse matrix:

State N°1: [[4, 1, 3], [8, 0, 5], [2, 7, 6]] , State N°2: [[4, 1, 3], [0, 8, 5], [2, 7, 6]] , State N°3: [[4, 1, 3], [2, 8, 5], [0, 7, 6]] <br>
State N°4: [[4, 1, 3], [2, 8, 5], [7, 0, 6]] , State N°5: [[4, 1, 3], [2, 0, 5], [7, 8, 6]] , State N°6: [[4, 1, 3], [0, 2, 5], [7, 8, 6]] <br>
State N°7: [[0, 1, 3], [4, 2, 5], [7, 8, 6]] , State N°8: [[1, 0, 3], [4, 2, 5], [7, 8, 6]] , State N°9: [[1, 2, 3], [4, 0, 5], [7, 8, 6]] <br>
State N°10: [[1, 2, 3], [4, 5, 0], [7, 8, 6]] , State N°11: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 39 States.
Execution time: 0.07 seg.


Experiment  N° 3

Initial state = [7,2,0],[5,1,4],[8,6,3]
Goal state = [1,2,3],[4,5,6],[7,8,0]

With Table difference: h1:

State N°1: [[7, 2, 0], [5, 1, 4], [8, 6, 3]] , State N°2: [[7, 0, 2], [5, 1, 4], [8, 6, 3]] , State N°3: [[7, 1, 2], [5, 0, 4], [8, 6, 3]] <br>
State N°4: [[7, 1, 2], [0, 5, 4], [8, 6, 3]] , State N°5: [[0, 1, 2], [7, 5, 4], [8, 6, 3]] , State N°6: [[1, 0, 2], [7, 5, 4], [8, 6, 3]] <br>
State N°7: [[1, 5, 2], [7, 0, 4], [8, 6, 3]] , State N°8: [[1, 5, 2], [7, 4, 0], [8, 6, 3]] , State N°9: [[1, 5, 2], [7, 4, 3], [8, 6, 0]] <br>
State N°10: [[1, 5, 2], [7, 4, 3], [8, 0, 6]] , State N°11: [[1, 5, 2], [7, 4, 3], [0, 8, 6]] , State N°12: [[1, 5, 2], [0, 4, 3], [7, 8, 6]] <br>
State N°13: [[1, 5, 2], [4, 0, 3], [7, 8, 6]] , State N°14: [[1, 0, 2], [4, 5, 3], [7, 8, 6]] , State N°15: [[1, 2, 0], [4, 5, 3], [7, 8, 6]] <br>
State N°16: [[1, 2, 3], [4, 5, 0], [7, 8, 6]] , State N°17: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 497 States.
Execution time: 1.34 seg.

With Manhattan distances:

State N°1: [[7, 2, 0], [5, 1, 4], [8, 6, 3]] , State N°2: [[7, 0, 2], [5, 1, 4], [8, 6, 3]] , State N°3: [[7, 1, 2], [5, 0, 4], [8, 6, 3]] <br>
State N°4: [[7, 1, 2], [0, 5, 4], [8, 6, 3]] , State N°5: [[0, 1, 2], [7, 5, 4], [8, 6, 3]] , State N°6: [[1, 0, 2], [7, 5, 4], [8, 6, 3]] <br>
State N°7: [[1, 5, 2], [7, 0, 4], [8, 6, 3]] , State N°8: [[1, 5, 2], [7, 4, 0], [8, 6, 3]] , State N°9: [[1, 5, 2], [7, 4, 3], [8, 6, 0]] <br>
State N°10: [[1, 5, 2], [7, 4, 3], [8, 0, 6]] , State N°11: [[1, 5, 2], [7, 4, 3], [0, 8, 6]] , State N°12: [[1, 5, 2], [0, 4, 3], [7, 8, 6]] <br>
State N°13: [[1, 5, 2], [4, 0, 3], [7, 8, 6]] , State N°14: [[1, 0, 2], [4, 5, 3], [7, 8, 6]] , State N°15: [[1, 2, 0], [4, 5, 3], [7, 8, 6]] <br>
State N°16: [[1, 2, 3], [4, 5, 0], [7, 8, 6]] , State N°17: [[1, 2, 3], [4, 5, 6], [7, 8, 0]] 

It expanded 65 States.
Execution time: 0.15 seg.

With Inverse matrix:

State N°1: [[7, 2, 0], [5, 1, 4], [8, 6, 3]] , State N°2: [[7, 0, 2], [5, 1, 4], [8, 6, 3]] , State N°3: [[7, 1, 2], [5, 0, 4], [8, 6, 3]] <br>
State N°4: [[7, 1, 2], [5, 4, 0], [8, 6, 3]] , State N°5: [[7, 1, 2], [5, 4, 3], [8, 6, 0]] , State N°6: [[7, 1, 2], [5, 4, 3], [8, 0, 6]] <br>
State N°7: [[7, 1, 2], [5, 0, 3], [8, 4, 6]] , State N°8: [[7, 1, 2], [0, 5, 3], [8, 4, 6]] , State N°9: [[0, 1, 2], [7, 5, 3], [8, 4, 6]] <br>
State N°10: [[1, 0, 2], [7, 5, 3], [8, 4, 6]] , State N°11: [[1, 2, 0], [7, 5, 3], [8, 4, 6]] , State N°12: [[1, 2, 3], [7, 5, 0], [8, 4, 6]] <br>
State N°13: [[1, 2, 3], [7, 0, 5], [8, 4, 6]] , State N°14: [[1, 2, 3], [7, 4, 5], [8, 0, 6]] , State N°15: [[1, 2, 3], [7, 4, 5], [0, 8, 6]] <br>
State N°16: [[1, 2, 3], [0, 4, 5], [7, 8, 6]] , State N°17: [[1, 2, 3], [4, 0, 5], [7, 8, 6]] , State N°18: [[1, 2, 3], [4, 5, 0], [7, 8, 6]] <br>
State N°19: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded 615 States.
Execution time: 2.09 seg.

Experiments with 15-Puzzle
-------------------

Experiment N° 1 

Initial state = [5,1,3,4],[2,10,6,7],[9,0,12,8],[13,15,11,15]
Goal state = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]

Table difference: h1
]
State N°1: [[5, 1, 3, 4], [2, 10, 6, 7], [9, 0, 12, 8], [13, 14, 11, 15]] , State N°2: [[5, 1, 3, 4], [2, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] <br>
State N°3: [[5, 1, 3, 4], [0, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] , State N°4: [[0, 1, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] <br>
State N°5: [[1, 0, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] , State N°6: [[1, 2, 3, 4], [5, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] <br>
State N°7: [[1, 2, 3, 4], [5, 6, 0, 7], [9, 10, 12, 8], [13, 14, 11, 15]] , State N°8: [[1, 2, 3, 4], [5, 6, 7, 0], [9, 10, 12, 8], [13, 14, 11, 15]] <br>
State N°9: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 12, 0], [13, 14, 11, 15]] , State N°10: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 11, 15]] <br>
State N°11: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]] , State N°12: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]] <br>

It expanded 27 States.
Execution time: 0.06 seg.

With Manhattan distances:

State N°1: [[5, 1, 3, 4], [2, 10, 6, 7], [9, 0, 12, 8], [13, 14, 11, 15]] , State N°2: [[5, 1, 3, 4], [2, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] <br>
State N°3: [[5, 1, 3, 4], [0, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] , State N°4: [[0, 1, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] <br>
State N°5: [[1, 0, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] , State N°6: [[1, 2, 3, 4], [5, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] <br>
State N°7: [[1, 2, 3, 4], [5, 6, 0, 7], [9, 10, 12, 8], [13, 14, 11, 15]] , State N°8: [[1, 2, 3, 4], [5, 6, 7, 0], [9, 10, 12, 8], [13, 14, 11, 15]] <br>
State N°9: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 12, 0], [13, 14, 11, 15]] , State N°10: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 11, 15]] <br>
State N°11: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]] ,State N°12: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

It expanded 39 States.
Execution time: 0.11 seg.

With Inverse Matrix:

State N°1: [[5, 1, 3, 4], [2, 10, 6, 7], [9, 0, 12, 8], [13, 14, 11, 15]] , State N°2: [[5, 1, 3, 4], [2, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] <br>
State N°3: [[5, 1, 3, 4], [0, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] , State N°4: [[0, 1, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] <br>
State N°5: [[1, 0, 3, 4], [5, 2, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] , State N°6: [[1, 2, 3, 4], [5, 0, 6, 7], [9, 10, 12, 8], [13, 14, 11, 15]] <br>
State N°7: [[1, 2, 3, 4], [5, 6, 0, 7], [9, 10, 12, 8], [13, 14, 11, 15]] , State N°8: [[1, 2, 3, 4], [5, 6, 7, 0], [9, 10, 12, 8], [13, 14, 11, 15]] <br>
State N°9: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 12, 0], [13, 14, 11, 15]] , State N°10: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 11, 15]] <br>
State N°11: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]] , State N°12: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

It expanded  86 States.
Execution time: 0.31 seg.


Experiment N° 2

Initial state = [5,1,3,4],[2,10,6,7],[9,0,12,8],[13,15,11,15]
Goal state = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]

For this case, the algorithm keeps working more than 30 minutes, so we don't have a precise control.


Experiment N° 3

Initial state = [5,1,3,4],[2,10,6,7],[9,0,12,8],[13,15,11,15]
Goal state = [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]

For this case, the algorithm keeps working more than 30 minutes too, so we don't have a precise control.

We can see more cases of 15-puzzle tests.
We also discovered cases where the 15 puzzle took more time to find the way depending the algorithm.

Experiment N° 4

With Table difference: h1:
Estado N°1: [[5, 0, 6, 3], [2, 1, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] , Estado N°2: [[5, 1, 6, 3], [2, 0, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] <br>
Estado N°3: [[5, 1, 6, 3], [0, 2, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] , Estado N°4: [[0, 1, 6, 3], [5, 2, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] <br>
Estado N°5: [[1, 0, 6, 3], [5, 2, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] , Estado N°6: [[1, 2, 6, 3], [5, 0, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] <br>
Estado N°7: [[1, 2, 6, 3], [5, 10, 4, 8], [9, 0, 7, 12], [13, 14, 11, 15]] , Estado N°8: [[1, 2, 6, 3], [5, 10, 4, 8], [9, 7, 0, 12], [13, 14, 11, 15]] <br>
Estado N°9: [[1, 2, 6, 3], [5, 10, 4, 8], [9, 7, 12, 0], [13, 14, 11, 15]] , Estado N°10: [[1, 2, 6, 3], [5, 10, 4, 0], [9, 7, 12, 8], [13, 14, 11, 15]] <br>
Estado N°11: [[1, 2, 6, 3], [5, 10, 0, 4], [9, 7, 12, 8], [13, 14, 11, 15]] , Estado N°12: [[1, 2, 0, 3], [5, 10, 6, 4], [9, 7, 12, 8], [13, 14, 11, 15]] <br>
Estado N°13: [[1, 2, 3, 0], [5, 10, 6, 4], [9, 7, 12, 8], [13, 14, 11, 15]] , Estado N°14: [[1, 2, 3, 4], [5, 10, 6, 0], [9, 7, 12, 8], [13, 14, 11, 15]] <br>
Estado N°15: [[1, 2, 3, 4], [5, 10, 6, 8], [9, 7, 12, 0], [13, 14, 11, 15]] , Estado N°16: [[1, 2, 3, 4], [5, 10, 6, 8], [9, 7, 0, 12], [13, 14, 11, 15]] <br>
Estado N°17: [[1, 2, 3, 4], [5, 10, 6, 8], [9, 0, 7, 12], [13, 14, 11, 15]] , Estado N°18: [[1, 2, 3, 4], [5, 0, 6, 8], [9, 10, 7, 12], [13, 14, 11, 15]] <br>
Estado N°19: [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 12], [13, 14, 11, 15]] , Estado N°20: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 11, 15]] <br>
Estado N°21: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]] , Estado N°22: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]] <br>
It expanded  7413 States.
Execution time: 62.23 seg.

With Manhattan distances:
Estado N°1: [[5, 0, 6, 3], [2, 1, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] , Estado N°2: [[5, 1, 6, 3], [2, 0, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] <br>
Estado N°3: [[5, 1, 6, 3], [0, 2, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] , Estado N°4: [[0, 1, 6, 3], [5, 2, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] <br>
Estado N°5: [[1, 0, 6, 3], [5, 2, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] , Estado N°6: [[1, 2, 6, 3], [5, 0, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] <br>
Estado N°7: [[1, 2, 6, 3], [5, 10, 4, 8], [9, 0, 7, 12], [13, 14, 11, 15]] , Estado N°8: [[1, 2, 6, 3], [5, 10, 4, 8], [9, 7, 0, 12], [13, 14, 11, 15]] <br>
Estado N°9: [[1, 2, 6, 3], [5, 10, 4, 8], [9, 7, 12, 0], [13, 14, 11, 15]] , Estado N°10: [[1, 2, 6, 3], [5, 10, 4, 0], [9, 7, 12, 8], [13, 14, 11, 15]] <br>
Estado N°11: [[1, 2, 6, 3], [5, 10, 0, 4], [9, 7, 12, 8], [13, 14, 11, 15]] , Estado N°12: [[1, 2, 0, 3], [5, 10, 6, 4], [9, 7, 12, 8], [13, 14, 11, 15]] <br>
Estado N°13: [[1, 2, 3, 0], [5, 10, 6, 4], [9, 7, 12, 8], [13, 14, 11, 15]] , Estado N°14: [[1, 2, 3, 4], [5, 10, 6, 0], [9, 7, 12, 8], [13, 14, 11, 15]] <br>
Estado N°15: [[1, 2, 3, 4], [5, 10, 6, 8], [9, 7, 12, 0], [13, 14, 11, 15]] , Estado N°16: [[1, 2, 3, 4], [5, 10, 6, 8], [9, 7, 0, 12], [13, 14, 11, 15]] <br>
Estado N°17: [[1, 2, 3, 4], [5, 10, 6, 8], [9, 0, 7, 12], [13, 14, 11, 15]] , Estado N°18: [[1, 2, 3, 4], [5, 0, 6, 8], [9, 10, 7, 12], [13, 14, 11, 15]] <br>
Estado N°19: [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 12], [13, 14, 11, 15]] , Estado N°20: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 12], [13, 14, 11, 15]] <br>
Estado N°21: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]] , Estado N°22: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]] <br>
It expanded  2054 States.
Execution time: 4.76 seg.

With Inverse matrix:
Estado N°1: [[5, 0, 6, 3], [2, 1, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] , Estado N°2: [[5, 1, 6, 3], [2, 0, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] <br>
Estado N°3: [[5, 1, 6, 3], [0, 2, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] , Estado N°4: [[0, 1, 6, 3], [5, 2, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] <br>
Estado N°5: [[1, 0, 6, 3], [5, 2, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] , Estado N°6: [[1, 2, 6, 3], [5, 0, 4, 8], [9, 10, 7, 12], [13, 14, 11, 15]] <br>
Estado N°7: [[1, 2, 6, 3], [5, 10, 4, 8], [9, 0, 7, 12], [13, 14, 11, 15]] , Estado N°8: [[1, 2, 6, 3], [5, 10, 4, 8], [9, 7, 0, 12], [13, 14, 11, 15]] <br>
Estado N°9: [[1, 2, 6, 3], [5, 10, 4, 8], [9, 7, 11, 12], [13, 14, 0, 15]] , Estado N°10: [[1, 2, 6, 3], [5, 10, 4, 8], [9, 7, 11, 12], [13, 14, 15, 0]] <br>
Estado N°11: [[1, 2, 6, 3], [5, 10, 4, 8], [9, 7, 11, 0], [13, 14, 15, 12]] , Estado N°12: [[1, 2, 6, 3], [5, 10, 4, 0], [9, 7, 11, 8], [13, 14, 15, 12]] <br>
Estado N°13: [[1, 2, 6, 3], [5, 10, 0, 4], [9, 7, 11, 8], [13, 14, 15, 12]] , Estado N°14: [[1, 2, 0, 3], [5, 10, 6, 4], [9, 7, 11, 8], [13, 14, 15, 12]] <br>
Estado N°15: [[1, 2, 3, 0], [5, 10, 6, 4], [9, 7, 11, 8], [13, 14, 15, 12]] , Estado N°16: [[1, 2, 3, 4], [5, 10, 6, 0], [9, 7, 11, 8], [13, 14, 15, 12]] <br>
Estado N°17: [[1, 2, 3, 4], [5, 10, 6, 8], [9, 7, 11, 0], [13, 14, 15, 12]] , Estado N°18: [[1, 2, 3, 4], [5, 10, 6, 8], [9, 7, 0, 11], [13, 14, 15, 12]] <br>
Estado N°19: [[1, 2, 3, 4], [5, 10, 6, 8], [9, 0, 7, 11], [13, 14, 15, 12]] , Estado N°20: [[1, 2, 3, 4], [5, 0, 6, 8], [9, 10, 7, 11], [13, 14, 15, 12]] <br>
Estado N°21: [[1, 2, 3, 4], [5, 6, 0, 8], [9, 10, 7, 11], [13, 14, 15, 12]] , Estado N°22: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 0, 11], [13, 14, 15, 12]] <br>
Estado N°23: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 0], [13, 14, 15, 12]] , Estado N°24: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]] <br>
It expanded  7358 States.
Execution time: 54,67 seg.

Experiments with the new heucaristic
-------------------

Experiment N°1

Estado N°1: [[4, 1, 3], [8, 0, 5], [2, 7, 6]] , Estado N°2: [[4, 1, 3], [0, 8, 5], [2, 7, 6]] , Estado N°3: [[4, 1, 3], [2, 8, 5], [0, 7, 6]] <br>
Estado N°4: [[4, 1, 3], [2, 8, 5], [7, 0, 6]] , Estado N°5: [[4, 1, 3], [2, 0, 5], [7, 8, 6]] , Estado N°6: [[4, 1, 3], [0, 2, 5], [7, 8, 6]] <br>
Estado N°7: [[0, 1, 3], [4, 2, 5], [7, 8, 6]] , Estado N°8: [[1, 0, 3], [4, 2, 5], [7, 8, 6]] , Estado N°9: [[1, 2, 3], [4, 0, 5], [7, 8, 6]] <br>
Estado N°10: [[1, 2, 3], [4, 5, 0], [7, 8, 6]] , Estado N°11: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded  18 States.
Execution time: 0.03 seg.

Experiment n

Estado N°1: [[4, 1, 3], [8, 0, 5], [2, 7, 6]] , Estado N°2: [[4, 1, 3], [0, 8, 5], [2, 7, 6]] , Estado N°3: [[4, 1, 3], [2, 8, 5], [0, 7, 6]] <br>
Estado N°4: [[4, 1, 3], [2, 8, 5], [7, 0, 6]] , Estado N°5: [[4, 1, 3], [2, 0, 5], [7, 8, 6]] , Estado N°6: [[4, 1, 3], [0, 2, 5], [7, 8, 6]] <br>
Estado N°7: [[0, 1, 3], [4, 2, 5], [7, 8, 6]] , Estado N°8: [[1, 0, 3], [4, 2, 5], [7, 8, 6]] , Estado N°9: [[1, 2, 3], [4, 0, 5], [7, 8, 6]] <br>
Estado N°10: [[1, 2, 3], [4, 5, 0], [7, 8, 6]] , Estado N°11: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded  18 States.
Execution time: 0.05 seg.

Estado N°1: [[7, 2, 0], [5, 1, 4], [8, 6, 3]] , Estado N°2: [[7, 0, 2], [5, 1, 4], [8, 6, 3]] , Estado N°3: [[7, 1, 2], [5, 0, 4], [8, 6, 3]] <br>
Estado N°4: [[7, 1, 2], [0, 5, 4], [8, 6, 3]] , Estado N°5: [[0, 1, 2], [7, 5, 4], [8, 6, 3]] , Estado N°6: [[1, 0, 2], [7, 5, 4], [8, 6, 3]] <br>
Estado N°7: [[1, 2, 0], [7, 5, 4], [8, 6, 3]] , Estado N°8: [[1, 2, 4], [7, 5, 0], [8, 6, 3]] , Estado N°9: [[1, 2, 4], [7, 5, 3], [8, 6, 0]] <br>
Estado N°10: [[1, 2, 4], [7, 5, 3], [8, 0, 6]] , Estado N°11: [[1, 2, 4], [7, 5, 3], [0, 8, 6]] , Estado N°12: [[1, 2, 4], [0, 5, 3], [7, 8, 6]] <br>
Estado N°13: [[0, 2, 4], [1, 5, 3], [7, 8, 6]] , Estado N°14: [[2, 0, 4], [1, 5, 3], [7, 8, 6]] , Estado N°15: [[2, 4, 0], [1, 5, 3], [7, 8, 6]] <br>
Estado N°16: [[2, 4, 3], [1, 5, 0], [7, 8, 6]] , Estado N°17: [[2, 4, 3], [1, 0, 5], [7, 8, 6]] , Estado N°18: [[2, 0, 3], [1, 4, 5], [7, 8, 6]] <br>
Estado N°19: [[0, 2, 3], [1, 4, 5], [7, 8, 6]] , Estado N°20: [[1, 2, 3], [0, 4, 5], [7, 8, 6]] , Estado N°21: [[1, 2, 3], [4, 0, 5], [7, 8, 6]] <br>
Estado N°22: [[1, 2, 3], [4, 5, 0], [7, 8, 6]] , Estado N°23: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

It expanded  992 States.
Execution time: 7.46 seg.

Tables of results
-------------------

<!------- Tabla prototipo
|8-Puzzle <td colspan=2>Table Diference <td colspan=2>  Manhattan Distance<td colspan=2> Inverse matrix |
| -------- | ----------------- | ------------------- | ------------------- |
|          |States | Time [seg]| States | Time [seg] | States | Time [seg] |
|  N° 1    |  554  |   1.53    |   180  |    0.47    |   429  |    1.24    |
|  N° 2    |   43  |   0.07    |    29  |    0.05    |    39  |    0.07    |
|  N° 3    |  497  |   1.34    |    65  |    0.15    |   615  |    2.09    |
|  TOTAL   | 1094  |   2.95    |   274  |    0.67    |  1083  |    3.40    |
--------->

|2-Puzzle  |Table Diference    | Manhattan Distance  |   Inverse matrix    |
| :------: | :---------------: | :-----------------: | :-----------------: |
|          |States , Time [seg]| States , Time [seg] | States , Time [seg] |
|  N° 1    |    6  ,   0.01    |     5  ,    0.00    |     8  ,    0.01    |
|  N° 2    |   13  ,   0.02    |    13  ,    0.01    |    13  ,    0.01    |
|  TOTAL   |   19  ,   0.03    |    18  ,    0.01    |    21  ,    0.02    |
       
|8-Puzzle  |Table Diference    | Manhattan Distance  |   Inverse matrix    |
| :------: | :---------------: | :-----------------: | :-----------------: |
|          |States , Time [seg]| States , Time [seg] | States , Time [seg] |
|  N° 1    |  554  ,   1.53    |   180  ,    0.47    |   429  ,    1.24    |
|  N° 2    |   43  ,   0.07    |    29  ,    0.05    |    39  ,    0.07    |
|  N° 3    |  497  ,   1.34    |    65  ,    0.15    |   615  ,    2.09    |
|  TOTAL   | 1094  ,   2.95    |   274  ,    0.67    |  1083  ,    3.40    |

|15-Puzzle  |Table Diference    | Manhattan Distance  |   Inverse matrix    |
| :------: | :---------------: | :-----------------: | :-----------------: |
|          |States , Time [seg]| States , Time [seg] | States , Time [seg] |
|  N° 1    |   27  ,   0.06    |    39  ,    0.11    |    86  ,    0.31    |
|  N° 2    |   --  ,  +1800    |    --  ,   +1800    |    --  ,   +1800    |
|  N° 3    |   --  ,  +1800    |    --  ,   +1800    |    --  ,   +1800    |
|  N° 4    |   387  ,  0.47    |    461  ,   0.53    |    2620  ,   7.33    |
|  N° 5    |   156  ,  0.11    |    100  ,   0.09    |    211  ,   0.19    |
|  N° 6    |   115  ,  0.08    |    210  ,   0.21    |    306  ,   0.35    |
|  N° 7    |   7358  ,  54.67    |    2054  ,   4.76    |    7413  ,   62.23    |
|  TOTAL   |   8043  ,    55.39     |    2864  ,    5.7      |    10630  ,    70.41      |


(We only sum the knowed cases in the table of 15-puzzle)
## Beans
With the new heucaristic
-------------------
The new algorithm that we implemented realized the next results:
### 8-Puzzle

|  Case    |States    | Time [seg] | States for path   |
| :------: | :------: | :--------: | :------------:    |
|  N° 1    |    18    |   0.03     |        17         |
|  N° 2    |    18    |   0.05     |        11         | 
|  N° 3    |   992    |   1.37     |        23         | 
|  TOTAL   |  1028    |   1.45     |        51         | 


### 15-Puzzle                  

| Case        |  States  | Time [seg] | States for path |
| :------:    | :------: | :--------: | :------------:  |
|  N° 1       |   25     |    0.04    |       12        |
|  N° 2       |   --     |   ----     |       --        |
|  N° 3       |   --     |   ----     |       --        |
|  N° 4       |   250    |   0.35     |       22        | 
|  N° 5       |  31      |   0.05     |       18        | 
|  N° 6       |  331     |   7.49     |       16        | 
|  N° 7       |  1931    |   4.56     |       24        | 
|  TOTAL      |  2568    |   12.49    |       92        | 

(We only sum the knowed cases in the table of 15-puzzle)

Conclusions
==========================

In the 3-puzzle, the algorithm is very effective in time, the second heucharist is better in time and memory, then the first heucharist is better than the third heucharist in memory, but the third heucharist is better that the first in time. We only use two cases because is a early test of the program behavior.

In the 8-puzzle, with the table of results, the h2(Manhattan Distance) looks like the better heucharist, with the best time and the best in memory.
Then the third heucharist (Inverse matrix) is better than the first heucharist (Table Diference), but the first heucharist takes up less memory than the third heucharist, just like with the experiments with the 3-puzzle.

In the 15-puzzle, the algorithms work irregularly, with a basic initial state it works even better than a 8-puzzle, but with a initial state more complex, the algorithms work for a long time. We wait for 2 hours and it keeps working, so we decided just control it like more than 30 minutes, because it was the time we made the other tests.

Despite the long search time, if we add the cases we know their results we can compare that as well as the total states as the total time, the most effective heuristic is the distance Manhattan followed by the differences of pieces being the worst the inverse matrix.

The experiments with the new heucaristic, looks better for the first and the second case, but looks worse for the thrid case. So it can be a better solution for simple cases, but it's not so good for complex cases. 

Concluding, the A* with the tested heucaristics is not always optimum for get the shortest way, for example, the thrid heucaristic takes up a lot of memory, but the first heucaristic show good results in time but the better heucaristic, is the second. However, when the states are very complex, the algorithms are slow and it doesn't always find the answer.

Beans .- With the new heucaristic, look a little better for simple cases, but it take a long time for complex cases example case 2 and 3 of 15-puzzle, the algoritmh is better than the inverse permutations and the number of pieces out of place but is lower than the Manhattan distance, the algorithm is moderately better to be implemented. 


Bibliography
==========================
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

Solver and generator for 15-puzzle:
https://www.jaapsch.net/puzzles/javascript/fifteenj.htm

