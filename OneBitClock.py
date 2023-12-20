

from Semantic import Semantic


class OneBitClock(Semantic):

    def __init__(self):
        pass

    def initial(self):
        return [0,1]

    def actions(self, config):
        A=[]
        if config==1:
            A.append(lambda c: [0])
        else: #config==0
            A.append(lambda c: [1])
        return A

    def execute(self, action, config):
        return action(config)
    
    