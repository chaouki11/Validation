from IRootedGraph import abstractmethod
from projets.validationGithub.Semantic import Semantic2RG


class Semantic():
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def initial(self):
        pass

    @abstractmethod
    def actions(self, config):
        pass

    @abstractmethod
    def execute(self,action, config):
        pass
    
    