
from collections import deque
from IRootedGraph import RootedGraph
from hanoiNode import HanoiConfig, isFinal
from traceHanoi import print_trace_for_direct_solution

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
    


def bfsSearch(graph,query):
    visited = set()
    queue = deque()

    for root in graph.getRoots():
        queue.append(root)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            
            if query(node):
                return visited
            
            unvisited = [n for n in graph.getNeighbors(node) if n not in visited]
            queue.extend(unvisited)

    return visited


gr=HanoiRG()
#print(bfsSearch(gr,isFinal))
print("BFS search: \n\n")
for e in bfsSearch(gr,isFinal):
    print(e.towers)
print("\n\nTrace : \n\n")
print_trace_for_direct_solution(gr,isFinal)