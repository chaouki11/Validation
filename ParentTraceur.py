

from IRootedGraph import RootedGraph


class ParentTraceur(RootedGraph):
    def __init__(self,rg,parents=None):
        self.rg = rg    #operand
        self.parents =  {}
        #self.fparents =  []
        

    def getRoots(self):
        uroots=self.rg.getRoots()

        #return uroots
        for n in uroots:
            self.parents[n] = []
        return uroots
    
    def getNeighbors(self, n):

        uneighbors = self.rg.getNeighbors(n)

        # self.fparents.push(n,[n.towers])
        # if n not in self.fparents:
        #     if n in self.fparents.getNeighbors():
        #         self.fparents= self.fparents + [n.towers]

        # return uneighbors

        for node in uneighbors:
            if self.parents.get(node) is None:
                self.parents[node] = [n]
        return uneighbors
    
    def printParents(self,last):
        lap=last
        value=self.parents[last]

        while value is not None and len(value) is not 0:
            print(f"{lap.towers}: {value[0].towers}")

            lap=value[0]
            value=self.parents[lap]