# 8-puzzle-solver

## 8-puzzle game, a sliding puzzle where players try to rearrange 8 tiles into numerical order. The program uses following algorithms to  find the solution from any given 'initial state' to 'final state' of the puzzle.
    - A* search (A star search)
    - BFS (Breadth first search)
    - DFS (Depth first search)
    - DLS (Depth limited Search)
    - GREEDY (Greedy search)
    - IDS (Iterative deepening depth-first search)
    - UCS (Uniform cost search)

## 👨‍💻 Problem Statement
In this project, our goal is to develop an agent that can solve a modified version of the classic 8-puzzle problem, called the Expense 8 puzzle problem. Similar to the original problem, the task involves rearranging 8 tiles on a 3x3 grid, where only one tile can be moved at a time to an adjacent blank location. **However, in this modified version, each tile is assigned a cost that represents the expense of moving that particular tile**. 
<br/> <br/> For instance, moving the tile marked with 6 would cost 6. Our objective is to determine the optimal order of moves that would result in the desired configuration of the puzzle while minimizing the total expense incurred.

## ✨ Given Inputs Format
    start.txt - contains the initial state of the board
    goal.txt - contains the goal state of the board

## ⭐️ Sample Inputs
    Start orientation:
        2 4 3
        1 0 6
        7 5 8

    Goal orientation:
        1 2 3
        4 5 6
        7 8 0

## ⚡ Sample Output
    Algorithm: A* Search
    Time taken: 2.025 ms

    Nodes Explored:  20
    Solution Found at depth 6 with cost of 24.
    Steps: 
        Move 4 Down
        Move 2 Right
        Move 1 Up
        Move 4 Left
        Move 5 Up
        Move 8 Left

## 👇 Requirements
- Install Python 3.x version or greater

## 🛠️ How to Run (step by step)
Open Terminal and follow the steps below:

1. Clone the repository
    > git clone https://github.com/Nikhil-prog/8-puzzle-solver.git

2. Change to repository folder
    > cd 8-puzzle-solver

3. Run Driver function
    >python expense_8_puzzle.py