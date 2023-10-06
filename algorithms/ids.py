import copy
from .dls import DLS
from .algo import BaseAlgo

class IDS(BaseAlgo):
    def __init__(self, **kwargs) -> None:
        if kwargs.get("puzzle") is None:
            raise Exception("Puzzle object is not passed")
        self.puzzle = kwargs.get("puzzle")
        
        if kwargs.get("depth_limit") is None:
            raise Exception("Depth limit is not passed")
        self.max_depth_limit = kwargs.get("depth_limit")
        
    def run(self):
        nodes_explored = 0
        
        # Run DLS for each depth till max_depth_limit
        for depth in range(0, 1 + self.max_depth_limit, 1):
            puzzle = copy.deepcopy(self.puzzle)
            algo = DLS(**{"puzzle": puzzle, "depth_limit": depth})
            is_found = algo.run()
            nodes_explored += algo.nodes_explored
            
            if is_found:
                self.puzzle.solution  = algo.puzzle.solution
                self.puzzle.solution.nodes_explored = nodes_explored
                return True
        
        return False
                