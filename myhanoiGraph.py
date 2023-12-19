
from collections import deque
from IRootedGraph import RootedGraph
from hanoiNode import HanoiConfig, isFinal
from ParentTraceur import ParentTraceur
from utilities import bfsSearch, print_visited_nodes, printParents

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

pr=ParentTraceur(gr)

#parentTraceur(gr)

R=bfsSearch(pr,isFinal,includeTrace=True)


#print the visited nodes when using the BFS search
print_visited_nodes(R)
#print the trace for finding the solutino  
#print_hanoi_trace_for_direct_solution(R)
# parent_traceur(pr)
# get_trace(R[1])

print("-----------------")
print("-----------------")
print("-----------------")
#fonction qui affiche la trace
printParents(pr,R[1])