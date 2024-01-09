import random
from Semantic import Semantic


class AliceAndBob1(Semantic):

    def __init__(self):
        self.sA=0   #sA représente l'état actuel de Alice: 0:initial 1:attente 2:critique
        self.sB=0

    def initial(self):
        return [("initialAlice", "initialBob")]

    def actions(self, config):
        a=[]
        if random.random() < 0.5: #alice moves
            print("moma ")
            print(type(config))
            node,b=config
            print("alice moves with : "+b)
            if node == "initialAlice":
                a.append(lambda x: ("attendAlice",b))
            elif node == "attendAlice":
                a.append(lambda x: ("EnSectionCritiqueAlice",b))
            elif node == "EnSectionCritiqueAlice":
                a.append(lambda x: ("initialAlice",b))
        else:#bob moves
            al,node=config
            print("bob moves with : "+al)
            if node == "initialBob":
                a.append(lambda x: (al,"attendBob"))
            elif node == "attendBob":
                a.append(lambda x: (al,"EnSectionCritiqueBob"))
            elif node == "EnSectionCritiqueBob":
                a.append(lambda x: (al,"initialBob"))
        return a

    def execute(self, action, config):
        return action(config)
    
    

