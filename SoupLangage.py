from abc import ABC

from Semantic import Semantic

class SoupConfiguration(ABC):
    def __hash__(self):
        pass
    
    def __eq__(self, other):
        pass

    def __str__(self):
        pass


class Piece(SoupConfiguration):
    def __init__(self, nom, garde, action):
        self.nom = nom
        self.garde = garde
        self.action = action

    def enabled(self,c):
        return self.garde(c)

    def execute(self,c):
        return [self.action(c)]


class SoupSpecification:

    def __init__(self, pieces,initials):
        self.initials=initials #list de SoupConfiguration
        self.pieces_list = pieces #liste de pieces

    def initial(self): #list de SoupConfiguration
        return self.initials
    
    def pieces(self): #liste de pieces
        return self.pieces_list
    
    def enabledPieces(self,c):
        filtered_pieces = list(filter(lambda p: p.enabled(c), self.pieces))
        return filtered_pieces


class SoupSemantics(Semantic):
    def _init_(self, spec):
        self.spec = spec

    def initial(self):
        return self.spec.initial()

    def actions(self, config):
        return self.spec.enabledPieces(config)
    
    def execute(self,piece, config):
        return piece.action(config)
    
