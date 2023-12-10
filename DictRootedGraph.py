from collections import deque

from IRootedGraph import RootedGraph

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


g = DictRootedGraph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

# Set roots as a list containing the single root node 0
g.roots = [0]

print(bfsSearch(g,lambda n: n>9))
