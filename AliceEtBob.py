from Semantic import Semantic


class AliceAndBob(Semantic):

    def __init__(self):
        self.sA=0   #sA représente l'état actuel: 0:initial 1:attente 2:critique
        self.sB=0

    def initial(self):
        return [(0,0)]

    def actions(self, config):
        A=[]
        if config==1:
            A.append(lambda c: [0])
        else: #config==0
            A.append(lambda c: [1])
        return A

    def execute(self, action, config):
        pass
    
    

