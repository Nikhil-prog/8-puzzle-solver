from .algo import BaseAlgo
from queue import PriorityQueue

class UCS(BaseAlgo):
    def __init__(self, **kwargs) -> None:
        if kwargs.get("puzzle") is None:
            raise Exception("Puzzle object is not passed")
        self.puzzle = kwargs.get("puzzle")
        
    def run(self):
        visited = []
        nodes_explored = 1
        priority_queue = PriorityQueue()
        
        # Add initial board to the priority queue
        # as each instance in the form of (cost, depth, board state, steps)
        priority_queue.put((0, 0,  self.puzzle.initial_board, []))
        
        while not priority_queue.empty():
            cost, depth, currBoard, step = priority_queue.get()

            # Solution found
            if currBoard == self.puzzle.goal_board:
                self.puzzle.solution.nodes_explored = nodes_explored
                self.puzzle.solution.depth_found = depth
                self.puzzle.solution.total_cost = cost
                self.puzzle.solution.steps = step
                return True            
            
            # checks if curr state is already visited
            if currBoard in visited:
                continue

            # visisting the curr state
            visited.append(currBoard)

            # adjacent boards
            empty_i, empty_j = self.puzzle.__get_empty_slot__(currBoard)
            neighbhours = self.puzzle.__get_neighbour_board__(currBoard)
            
            for child in neighbhours:
                nodes_explored += 1
                # child's features
                _child_cost = cost + child[empty_i][empty_j]
                _child_depth = depth + 1
                _child_step = self.puzzle.__get_step__(
                    step, child, empty_i, empty_j
                )
                
                priority_queue.put((_child_cost, _child_depth, child, _child_step))
                
        return False