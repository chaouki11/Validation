

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
        #TEST detection de tagged cycles        #INCOMPLET: code incorrect
##########################################


class Myconf(SoupConfiguration):
    def __init__(self):
        self.state=0 #0,1,2
        
    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other):
        return self.state==other.state

    def __str__(self):
        return "state"+str(self.state)


def restate(x,v):
    x.state=v
    return x
    

pb1=Piece("movement",lambda x:x.state==0,lambda x: restate(x,1))    
pb2=Piece("movement",lambda x:x.state==1,lambda x: restate(x,2))   
pb3=Piece("movement",lambda x:x.state==2,lambda x: restate(x,0))   
pb4=Piece("movement",lambda x:x.state==2,lambda x: restate(x,2))#on crée une boucle

Lp=[pb1,pb2,pb3,pb4]
initials=[Myconf()]
soup=SoupSpecification(initials,Lp)
soupSem=SoupSemantics(soup)
s=Semantic2RG(soupSem)
pr=ParentTraceur(s)

R=bfsSearch(pr,lambda n:n in pr.getNeighbors(n))
#le noeud solution est un noeud qui appartient à une boucle

print(R[0])



# ##########################################

#pour détecter un cyle:
cycledetect(pr)


R=bfsSearch(pr,lambda n:n in bfsSearch(pr,lambda n:n)[1])

