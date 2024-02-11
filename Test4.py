
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

# ##########################################
#         #TEST Soup langage AlicebobV0 avec soup #fonctionnel
# ##########################################

def p1a_a(x,op):
    if op==0:# for alice
        x.state_Alice=(x.state_Alice+1)%3
        return x
    else:#for bob
        x.state_Bob=(x.state_Bob+1)%3
        return x
    

p1a=Piece("Alice veux",lambda x: True,lambda x: p1a_a(x,0))
p2a=Piece("Alice entre",lambda x: True,lambda x: p1a_a(x,0))
p3a=Piece("Alice sort",lambda x: True,lambda x: p1a_a(x,0))
p1b=Piece("Bob veux",lambda x: True,lambda x: p1a_a(x,1))
p2b=Piece("Bob entre",lambda x:True,lambda x: p1a_a(x,1))
p3b=Piece("Bob sort",lambda x: True,lambda x: p1a_a(x,1))
Lp=[p1a,p2a,p3a,p1b,p2b,p3b]
random.shuffle(Lp)

initials=[AliceBobConf()]
soup=SoupSpecification(initials,Lp)
soupSem=SoupSemantics(soup)
s=Semantic2RG(soupSem)
pr=ParentTraceur(s)
R=bfsSearch(pr,lambda n: n.state_Bob==2)

print("------------")
print("---- chemin BFS----")
print()

for e in R[1]:
    print(e)

print("------------")
print("---- Trace ----")
print()
pr.printParentsABSoup(R[0])

# ##########################################
