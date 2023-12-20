

#define a hanoiGraph
from ParentTraceur import ParentTraceur
from hanoiNode import isFinal
from myhanoiGraph import HanoiRG
from Semantic2RG import Semantic2RG
from OneBitClock import OneBitClock
from AliceEtBob import AliceAndBob
from utilities import bfsSearch, print_visited_nodes_hanoi

##########################################
        #TEST PARENT TRACEUR#
##########################################

# gr=HanoiRG()
# pr=ParentTraceur(gr)
# R=bfsSearch(pr,isFinal)
# print_visited_nodes_hanoi(R)
# print("-----------------")
# print("-----------------")
# print("-----------------")
# pr.printParents(R[1])

##########################################



##########################################
        #TEST OneBitClock#
##########################################

OneBitClockInstance=OneBitClock()

semantic2RGInstance=Semantic2RG(OneBitClockInstance)

pr=ParentTraceur(semantic2RGInstance)

R=bfsSearch(pr,lambda n: n==3)

for e in R[0]:
    print(e)
##########################################




##########################################
        #TEST Alice et Bob#
##########################################

aliceAndBobInstance=AliceAndBob()

semantic2RGInstance=Semantic2RG(OneBitClockInstance)

pr=ParentTraceur(semantic2RGInstance)

R=bfsSearch(pr,isSolution)

for e in R[0]:
    print(e)
##########################################