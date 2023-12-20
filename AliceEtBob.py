from Semantic import Semantic


class AliceAndBob1(Semantic):

    def __init__(self):
        self.sA=0   #sA représente l'état actuel: 0:initial 1:attente 2:critique
        self.sB=0

    def initial(self):
        return [0]

    def actions(self, config):
        A=[]
        
        return A

    def execute(self, action, config):
        pass
    
    

