



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
        #TEST propriété et composition  alicebob peterson       #INCOMPLET
##########################################

# -----------------------
# test avec lhs = alicebob peterson
# -----------------------


def p1a_a(x,op):
    if op==0:# for alice
        if x.state_Alice==0:
            x.flag_Alice=1
            x.turn=1
        x.state_Alice=(x.state_Alice+1)%3
        if x.state_Alice==0:
            x.flag_Alice=0
        return x
    else:#for bob
        if x.state_Bob==0:
            x.flag_Bob=1
            x.turn=0
        x.state_Bob=(x.state_Bob+1)%3
        if x.state_Bob==0:
            x.flag_Bob=0
        return x

p1a=Piece("Alice veux",lambda x: x.state_Alice==0,lambda x: p1a_a(x,0))
p2a=Piece("Alice entre",lambda x: x.flag_Bob==0 or x.turn==0,lambda x: p1a_a(x,0))
p3a=Piece("Alice sort",lambda x: x.state_Alice==2,lambda x: p1a_a(x,0))

p1b=Piece("Bob veux",lambda x: x.state_Bob==0,lambda x: p1a_a(x,1))
p2b=Piece("Bob entre",lambda x:x.flag_Alice==0 or x.turn==1,lambda x: p1a_a(x,1))
p3b=Piece("Bob sort",lambda x: x.state_Bob==2,lambda x: p1a_a(x,1))

Lp1=[p1a,p2a,p3a,p1b,p2b,p3b]
random.shuffle(Lp1)

initials1=[AliceBobPeterson()]

#-----------------------

# propriété de bucchi rhs:

class PropBucchi:
    def __init__(self):
        self.state=0 # x=0, y=1

    def __str__(self):
        return "bucchi state: "+str(self.state)


def buchi_action(x):
    if x.state==1:
        x.state=0
    return x

#a corriger: garde bucchi prend 2 paramtre (input,configBucchi) où input=(source,action,target) de lhs
pb1=Piece("bucchi piece",lambda y,x: not(y[2].state_Alice==2 or y[2].state_Bob==2),lambda y,x: buchi_action(x))    
pb2=Piece("bucchi piece",lambda y,x: not(y[2].state_Alice==2 or y[2].state_Bob==2),lambda y,x: x)    
pb3=Piece("bucchi piece",lambda y,x: (y[2].state_Alice==2 or y[2].state_Bob==2),lambda y,x: x)    
Lp2=[pb1,pb2,pb3]
initials2=[PropBucchi()]

#-----------------------

#lhs=model(alice et bob)
#rhs=propriété(bucchi)
#car propriete depend du model et rhs depend de lhs
lhsspe=SoupSpecification(initials1,Lp1)
lhs=SoupSemantics(lhsspe)
rhs_soup=SoupSpecification(initials2,Lp2)
rhs=DependantSoupSemantics(rhs_soup)
dss=StepSynchComposition(lhs,rhs)
s=Semantic2RG(dss)
pr=ParentTraceur(s)
# R=bfsSearch(pr,lambda n:not(s.getNeighbors(n)))
# R=bfsSearch(pr,lambda n:n)
R=bfsSearch(pr,lambda n:n[1].state==1)


# for e in R[1]:
#     print(e[0])
#     print(e[1])



##########################################