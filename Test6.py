




import random
from ParentTraceur import ParentTraceur
from hanoiNode import isFinal
from myhanoiGraph import HanoiRG
from Semantic2RG import Semantic2RG
from OneBitClock import OneBitClock
from AliceEtBob import AliceAndBob0
from AliceAndBobV1 import AliceAndBobV1
from SoupLangage import Piece, SoupConfiguration, SoupSemantics, SoupSpecification
from AliceBobSoupConfig import AliceBobConf
from AliceBobSOupConfigV1 import AliceBobConfV1
from HanoiSoupConfig import HanoiSoupConfig
from DependantSemantics import DependantSoupSemantics
from StepSyncComposition import StepSynchComposition
from AliceBobPetersonConfig import AliceBobPeterson
from utilities import bfsSearch, cycledetect, print_visited_nodes_hanoi


##########################################
        #TEST Soup Hanoi    #fonctionnel
##########################################

def hpa(x,source,destination):
    return x.move_disk(source, destination)

def hgarde(x,source,destination):
    if source != destination and x.can_move(source, destination):
        return True
    return False

gardes=[(lambda x,i=i,j=j:hgarde(x,i,j)) for i in range(3) for j in range(3) if i!=j]
actions=[(lambda x,i=i,j=j:hpa(x,i,j)) for i in range(3) for j in range(3) if i!=j]

initials=[HanoiSoupConfig(3)]
#print(hpa(HanoiSoupConfig(3),0,1))
Lp=[Piece("deplacement disque: ",gardes[k],actions[k]) for k in range(len(actions))]

soup=SoupSpecification(initials,Lp)
soupSem=SoupSemantics(soup)
s=Semantic2RG(soupSem)
pr=ParentTraceur(s)
R=bfsSearch(pr,lambda n:isFinal(n))



print("------------")
print("---- chemin BFS----")
print()

for e in R[1]:
    print(e)


print("------------")
print("---- Trace ----")
print()
pr.printParentsHanoi(R[0])


##########################################