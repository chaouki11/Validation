from abc import ABC, abstractmethod


class RootedGraph(ABC):
    def __init__(self):
        self.graph = dict()
        self.roots = []

    @abstractmethod
    def getRoots(self):
        pass
    
    @abstractmethod
    def getNeighbors(self, n):
        pass
    