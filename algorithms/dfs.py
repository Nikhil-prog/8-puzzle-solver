from .algo import BaseAlgo

class DFS(BaseAlgo):
    def __init__(self, **kwargs) -> None:
        if kwargs.get("puzzle") is None:
            raise Exception("Puzzle object is not passed")
        self.puzzle = kwargs.get("puzzle")
        
        self.nodes_explored = 0
        
    def __dfs__(self, visited, cost, depth, currBoard, step):
        self.nodes_explored += 1
        visited.append(currBoard)
        
        # Base case : Solution found
        if currBoard == self.puzzle.goal_board:
            self.puzzle.solution.nodes_explored = self.nodes_explored
            self.puzzle.solution.depth_found = depth
            self.puzzle.solution.total_cost = cost
            self.puzzle.solution.steps = step
            return True
        
        # Recursive case
        empty_i, empty_j = self.puzzle.__get_empty_slot__(currBoard)
        neighbhours = self.puzzle.__get_neighbour_board__(currBoard)
        
        for child in neighbhours:
                if child not in visited:
                    # child's features
                    _child_cost = cost + child[empty_i][empty_j]
                    _child_depth = depth + 1
                    _child_step = self.puzzle.__get_step__(
                        step, child, empty_i, empty_j
                    )
                    
                    # Recursive call
                    is_found = self.__dfs__(visited, _child_cost, _child_depth, child, _child_step)
                    if is_found:
                        return True
        
        return False
    
    def run(self):
        visited = []
        cost = 0
        depth = 0
        step = []
        
        return self.__dfs__(visited, cost, depth, self.puzzle.initial_board, step)
        