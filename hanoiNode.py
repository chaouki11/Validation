

import copy


class HanoiConfig:

    def __init__(self,n):
        self.towers=[list(range(n, 0, -1)),list(),list()]

    def can_move(self, source, destination):
        source_tower = self.towers[source]
        destination_tower = self.towers[destination]

        if not source_tower:
            return False

        if not destination_tower or source_tower[-1] < destination_tower[-1]:
            return True

        return False
    
    def move_disk(self, source, destination):
        anext= copy.deepcopy(self)
        anext.towers[destination].append(anext.towers[source].pop())   
        return anext

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return self.towers == other.towers


def isFinal(node):
    if len(node.towers[0])==0 and len(node.towers[1])==0 and all(node.towers[2][i] > node.towers[2][i+1] for i in range(len(node.towers[2])-1)):
        return True
    return False
#x=list(range(0, 7, 1))
#x.append(10)
#print(x)