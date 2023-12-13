from collections import deque

from IRootedGraph import RootedGraph
from utilities import bfsSearch

#implementation of dictionnary based graph - not different from the abstract class
class DictRootedGraph(RootedGraph):
    def __init__(self):
        self.graph = dict()
        self.roots = []

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)

    def getRoots(self):
        return self.roots
    
    def getNeighbors(self, n):
        return self.graph.get(n, [])
    
    def __hash__(self):
        return 1

    def __eq__(self, other):
        return isinstance(other, DictRootedGraph) and \
               self.graph == other.graph and \
               self.roots == other.roots


#define a graph structure - just a test
g = DictRootedGraph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

# Set roots as a list containing the single root node 0
g.roots = [0]

#perform the bfs search
print(bfsSearch(g,lambda n: n>9))
