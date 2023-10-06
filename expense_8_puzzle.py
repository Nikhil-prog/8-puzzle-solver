import os
import copy
import time
from algorithms import AlgoFactory


class Solution:
    def __init__(self) -> None:
        self.nodes_explored = None
        self.depth_found = None
        self.total_cost = None
        self.steps = None

    def print(self):
        print("Nodes Explored: ", self.nodes_explored)
        print(f'Solution Found at depth {self.depth_found} with cost of {self.total_cost}.')
        print('Steps: ')
        for step in self.steps:
            print(f'\t{step}')


class Puzzle:
    # ------------- Private functions -------------
    def __init__(self, type, board_size) -> None:
        self.type = type
        self.initial_board = None
        self.goal_board = None
        self.board_size = board_size
        self.solution = Solution()

    def __load_board__(self, filename):
        if filename is None:
            raise Exception("Filename is not passed")
        elif filename == "":
            raise Exception("Filename is empty")
        elif not os.path.exists(filename):
            raise Exception("File does not exist")
        elif not filename.endswith(".txt"):
            raise Exception("Filename is not a text file")

        board = []
        for line in open(filename, "r").readlines():
            board.append([int(x) for x in line.split()])
            if len(board[-1]) != self.board_size:
                raise Exception("Board size is not correct")

        if len(board) != self.board_size:
            raise Exception("Board size is not correct")

        return board

    # return the indexes of empty slot in a particular board
    def __get_empty_slot__(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    return i, j
        return -1, -1

    # getting possible neighbour of empty slot
    def __get_neighbour_board__(self, board):
        neighbours = []
        n, m = len(board), len(board[0])
        i, j = self.__get_empty_slot__(board)

        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        for k in range(len(dx)):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x and x < n and 0 <= y and y < m:
                neighbour_board = copy.deepcopy(board)
                neighbour_board[i][j], neighbour_board[x][y] = (
                    neighbour_board[x][y],
                    neighbour_board[i][j],
                )
                neighbours.append(neighbour_board)

        return neighbours

    def __get_step__(self, stepx, board, i, j):
        n, m = len(board), len(board[0])

        step = copy.deepcopy(stepx)
        curr_step = "Move {0} ".format(board[i][j])
        if 0 <= i - 1 and board[i - 1][j] == 0:
            curr_step = curr_step + "Down"
        elif 0 <= j - 1 and board[i][j - 1] == 0:
            curr_step = curr_step + "Right"
        elif i + 1 < n and board[i + 1][j] == 0:
            curr_step = curr_step + "Up"
        elif j + 1 < m and board[i][j + 1] == 0:
            curr_step = curr_step + "Left"
        step.append(curr_step)
        return step

    # print the board
    def __print_board__(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                print(board[i][j], end=" ")
            print()
        print()

    # ------------- Public functions -------------
    def solve(self, start_file, goal_file, algo_name, depth_limit=15):
        self.initial_board = self.__load_board__(start_file)
        self.goal_board = self.__load_board__(goal_file)
        
        algo = AlgoFactory.get_algo_object(self.type)(**{"puzzle": self, "depth_limit": depth_limit})
        
        # run the algorithm
        start = time.time()
        algo.run()
        end = time.time()
        
        print('\n\n----------------------- Solution -----------------------')
        print(f'Algorithm: {algo_name}')
        print(f'Time taken: {(end-start) * 1000:.03f} ms\n')
        self.solution.print()
        print('--------------------------------------------------------')


if __name__ == "__main__":
    start_file = "start.txt"
    goal_file = "goal.txt"
    board_size = 3
    
    allowed_algos = ['a_star', 'bfs', 'dfs', 'dls', 'greedy', 'ids', 'ucs']
    algo_names = ['A* Search', 'Breadth First Search', 'Depth First Search', 'Depth Limited Search', 'Greedy Best First Search', 'Iterative Deepening depth-first Search', 'Uniform Cost Search']
    
    # simulate the puzzle
    while True:
        print('\n-------------------- 8 Puzzle Solver --------------------\n')
        print("Choose algorithm:")
        for i, algo in enumerate(algo_names):
            print(f"{i+1}. {algo}")
        
        print(": (or q to quit) ", end="")
        option = input().strip()
        if option == 'q':
            break
        elif not option.isdigit():
            print("Invalid option")
            continue
        elif int(option) < 1 or int(option) > len(allowed_algos):
            print("Invalid option")
            continue
        
        type = allowed_algos[int(option)-1]
        
        
        puzzle = Puzzle(type, board_size)
        puzzle.solve(start_file, goal_file, algo_names[int(option)-1])
