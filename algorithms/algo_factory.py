from .bfs import BFS

class AlgoFactory() :
    @staticmethod
    def get_algo_object(type) :
        algos = {"bfs" : BFS}
        algo_names = algos.keys()
        
        assert type in algo_names, f"Pick algo from {', '.join(algo_names)}!"
        
        return algos[type]