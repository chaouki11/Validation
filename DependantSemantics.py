

import copy


class DependantSemantics:
    def initial(self):
        pass

    def actions(self, input,configuration):
        pass
    
    def execute(self,action, input,configuration):
        pass



class DependantSoupSemantics(DependantSemantics):
    def __init__(self,soup):
        self.soup=soup

    def initial(self):
        return self.soup.initial()
    
    def actions(self, input,source):#garde() ne prend qu'un parametre dans sa signature-solution a trouver
        return filter(lambda p:p.garde(input,source),self.soup.pieces())
    
    def execute(self,piece, input,source):#input=step
        src=copy.deepcopy(source)
        inp=copy.deepcopy(input)
        return piece.action(inp,src)
    

