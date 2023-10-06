from .algo import BaseAlgo
from queue import PriorityQueue

class GREEDY(BaseAlgo):
    def __init__(self, **kwargs) -> None:
        if kwargs.get("puzzle") is None:
            raise Exception("Puzzle object is not passed")
        self.puzzle = kwargs.get("puzzle")

    # heuristic function
    # used misplaced tiles as heuristic function cost
    def __heuristic__(self, board):
        cost = -1
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] != self.puzzle.goal_board[i][j]:
                    cost = cost + 1
        return cost
    
    def __greedy_cost__(self, board):
        return self.__heuristic__(board)
    
    def run(self):
        visited = []
        nodes_explored = 1
        priority_queue = PriorityQueue()

        # greedy cost
        greedy_cost = self.__greedy_cost__(self.puzzle.initial_board)
        
        # Add initial board to the priority queue
        # as each instance in the form of (greedy_cost ,cost, depth, board state, steps)
        priority_queue.put((greedy_cost, 0, 0, self.puzzle.initial_board, []))
        
        while not priority_queue.empty():
            h, cost, depth, currBoard, step = priority_queue.get()

            # Solution found
            if currBoard == self.puzzle.goal_board:
                self.puzzle.solution.nodes_explored = nodes_explored
                self.puzzle.solution.depth_found = depth
                self.puzzle.solution.total_cost = cost
                self.puzzle.solution.steps = step
                return True  

            visited.append(currBoard)
            
            # adjacent boards
            empty_i, empty_j = self.puzzle.__get_empty_slot__(currBoard)
            neighbhours = self.puzzle.__get_neighbour_board__(currBoard)
            
            for child in neighbhours:
                if child not in visited:
                    nodes_explored += 1
                    # child's features
                    _child_cost = cost + child[empty_i][empty_j]
                    _child_depth = depth + 1
                    _child_step = self.puzzle.__get_step__(
                        step, child, empty_i, empty_j
                    )
                    
                    # heuristic function adjustment for child
                    _child_greedy_cost = self.__greedy_cost__(child)
                    
                    priority_queue.put((_child_greedy_cost, _child_cost, _child_depth, child, _child_step))
        
        return False