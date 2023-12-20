
from IRootedGraph import RootedGraph

class Semantic2RG(RootedGraph):

    def __init__(self, semantic):
        self.semantic = semantic

    def getRoots(self):
        roots=self.semantic.initial()
        return roots
    
    def getNeighbors(self, v):
        actions = self.semantic.actions(v)
        neighbours=[]
        for a in actions:
            targets=self.semantic.execute(a,v)
            neighbours.extend(targets)
        return neighbours