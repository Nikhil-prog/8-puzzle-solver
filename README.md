# 8-puzzle-solver

## 8-puzzle game, a sliding puzzle where players try to rearrange 8 tiles into numerical order. The program uses following algorithms to  find the solution from any given 'initial state' to 'final state' of the puzzle.
    - A* search (A star search)
    - BFS (Breadth first search)
    - DFS (Depth first search)
    - DLS (Depth limited Search)
    - UCS (Uniform cost search)
    - IDS (Iterative deepening search)
    - GREEDY (Greedy search)

## 👨‍💻 Problem Statement
In this project, our goal is to develop an agent that can solve a modified version of the classic 8-puzzle problem, called the Expense 8 puzzle problem. Similar to the original problem, the task involves rearranging 8 tiles on a 3x3 grid, where only one tile can be moved at a time to an adjacent blank location. **However, in this modified version, each tile is assigned a cost that represents the expense of moving that particular tile**. 
<br/> <br/> For instance, moving the tile marked with 6 would cost 6. Our objective is to determine the optimal order of moves that would result in the desired configuration of the puzzle while minimizing the total expense incurred.

## ⭐️ Given inputs
    start.txt - contains the initial state of the board
    goal.txt - contains the goal state of the board

## ⚡ Sample Output
    Nodes Popped: 97 
    Nodes Expanded: 64
    Nodes Generated: 173
    Max Fringe Size: 77
    Solution Found at depth 12 with cost of 63.
    Steps:
        Move 7 Left
        Move 5 Up
        Move 8 Right
        Move 7 Down
        Move 5 Left
        Move 6 Down
        Move 3 Right
        Move 2 Right
        Move 1 Up
        Move 4 Up
        Move 7 Left
        Move 8 Left 

## 👇 Requirements
- Python 3.x (for python version)
- Java (for java verison)

## 🛠️ How to Run (step by step)
Open Terminal and follow the steps below:

1. Clone the repository
    > git clone https://github.com/Nikhil-prog/8-puzzle-solver.git

2. Change to repository folder
    > cd 8-puzzle-solver

3. Change to folder 
    - For python version:
    > cd python\ version
    - For java vesion:
    > cd java\ version

4. xx