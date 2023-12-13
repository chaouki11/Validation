
from collections import deque
from IRootedGraph import RootedGraph
from hanoiNode import HanoiConfig, isFinal
from utilities import bfsSearch, print_trace_for_direct_solution

#graph implementation with nodes as hanoi configuration
class HanoiRG(RootedGraph):
    def __init__(self):
        self.graph = dict()
        self.roots =  [HanoiConfig(3)]

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)

    def getRoots(self):
        return self.roots
    
    def getNeighbors(self, n):
        neighbors = []

        # Move a single disk to another tower
        for source in range(3):
            for destination in range(3):
                if source != destination and n.can_move(source, destination):
                    new_config = n.move_disk(source, destination)
                    neighbors.append(new_config)

        return neighbors
    

#define a hanoiGraph
gr=HanoiRG()

#print the visited nodes when using the BFS search
print("BFS search: \n\n")
for e in bfsSearch(gr,isFinal):
    print(e.towers)

#print the trace for finding the solutino  
print("\n\nTrace : \n\n")
print_trace_for_direct_solution(gr,isFinal)