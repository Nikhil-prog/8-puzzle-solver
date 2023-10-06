from .a_star import ASTAR
from .bfs import BFS
from .dfs import DFS
from .dls import DLS
from .greedy import GREEDY
from .ids import IDS
from .ucs import UCS

class AlgoFactory() :
    @staticmethod
    def get_algo_object(type) :
        algos = {
            "a_star" : ASTAR,
            "bfs" : BFS,
            "dfs" : DFS,
            "dls"   : DLS,
            "greedy" : GREEDY,
            "ids" : IDS,
            "ucs" : UCS,
        }
        algo_names = algos.keys()
        
        assert type in algo_names, f"Pick algo from {', '.join(algo_names)}!"
        return algos[type]