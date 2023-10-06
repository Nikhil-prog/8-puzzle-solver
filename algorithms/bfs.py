from .algo import BaseAlgo
from queue import Queue


class BFS(BaseAlgo):
    def __init__(self, **kwargs) -> None:
        if kwargs.get("puzzle") is None:
            raise Exception("Puzzle object is not passed")
        self.puzzle = kwargs.get("puzzle")

    def run(self):
        visited = []
        queue = Queue()
        nodes_explored = 0

        # storing each instance in the form of (cost, depth, board state, steps)
        queue.put((0, 0, self.puzzle.initial_board, []))
        visited.append(self.puzzle.initial_board)

        while not queue.empty():
            cost, depth, currBoard, step = queue.get()

            # adjacent boards
            empty_i, empty_j = self.puzzle.__get_empty_slot__(currBoard)
            neighbhours = self.puzzle.__get_neighbour_board__(currBoard)

            for child in neighbhours:
                if child not in visited:
                    visited.append(child)
                    nodes_explored += 1

                    # child's features
                    _child_cost = cost + child[empty_i][empty_j]
                    _child_depth = depth + 1
                    _child_step = self.puzzle.__get_step__(
                        step, child, empty_i, empty_j
                    )

                    queue.put((_child_cost, _child_depth, child, _child_step))

                    # solution found
                    if child == self.puzzle.goal_board:
                        self.puzzle.solution.nodes_explored = nodes_explored
                        self.puzzle.solution.depth_found = _child_depth
                        self.puzzle.solution.total_cost = _child_cost
                        self.puzzle.solution.steps = _child_step
                        return True
        return False
