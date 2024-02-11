




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
        #TEST Alice Bob V2 (bob donne priorité à alice) soup
##########################################

def p1a_a(x,op):
    if op==0:# for alice
        if x.state_Alice==0:
            x.flag_Alice=1
        x.state_Alice=(x.state_Alice+1)%3
        if x.state_Alice==0:
            x.flag_Alice=0
        return x
    else:#for bob
        if x.state_Bob==0:
            x.flag_Bob=1
        x.state_Bob=(x.state_Bob+1)%3
        if x.state_Bob==0:
            x.flag_Bob=0
        return x


def descflag(x):
    x.flag_Bob=0
    x.state_Bobe=1
    return x

p1a=Piece("Alice veux",lambda x: x.state_Alice==0,lambda x: p1a_a(x,0))
p2a=Piece("Alice entre",lambda x: x.flag_Bob==0,lambda x: p1a_a(x,0))
p3a=Piece("Alice sort",lambda x: x.state_Alice==2,lambda x: p1a_a(x,0))
p1b=Piece("Bob veux",lambda x: x.state_Bob==0,lambda x: p1a_a(x,1))
p2b=Piece("Bob entre",lambda x:x.flag_Alice==0,lambda x: p1a_a(x,1))
p3b=Piece("Bob sort",lambda x: x.state_Bob==2,lambda x: p1a_a(x,1))
p4b=Piece("Bob descend flag",lambda x: x.flag_Alice==1 and x.flag_Bob==1,lambda x: descflag(x))

Lp=[p1a,p2a,p3a,p1b,p2b,p3b,p4b]
random.shuffle(Lp)

initials=[AliceBobConfV1()]
soup=SoupSpecification(initials,Lp)
soupSem=SoupSemantics(soup)
s=Semantic2RG(soupSem)
pr=ParentTraceur(s)
R=bfsSearch(pr,lambda n: not(s.getNeighbors(n)))

print("------------")
print("---- chemin BFS----")
print()

for e in R[1]:
    print(e)

# print("------------")
# print("---- Trace ----")
# print()

# # executer le parent traceur  donne une erreur quand car il ya plus de deadlock
# pr.printParentsABSoup(R[0])




##########################################