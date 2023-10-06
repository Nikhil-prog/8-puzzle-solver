from abc import ABC, abstractmethod


class BaseAlgo(ABC):
    @abstractmethod
    def run(self):
        pass
