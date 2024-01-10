

#define a hanoiGraph
from ParentTraceur import ParentTraceur
from hanoiNode import isFinal
from myhanoiGraph import HanoiRG
from Semantic2RG import Semantic2RG
from OneBitClock import OneBitClock
from AliceEtBob import AliceAndBob0
from AliceAndBobV1 import AliceAndBobV1
from utilities import bfsSearch, print_visited_nodes_hanoi

##########################################
        #TEST PARENT TRACEUR#   #fonctionnel
##########################################

# gr=HanoiRG()
# pr=ParentTraceur(gr)
# R=bfsSearch(pr,isFinal)
# print_visited_nodes_hanoi(R)
# print("-----------------")
# print("-----------------")
# print("-----------------")
# pr.printParentsHanoi(R[0])

##########################################



##########################################
        #TEST OneBitClock#      #fonctionnel
##########################################

# OneBitClockInstance=OneBitClock()

# semantic2RGInstance=Semantic2RG(OneBitClockInstance)

# pr=ParentTraceur(semantic2RGInstance)

# R=bfsSearch(pr,lambda n: n==3)

# for e in R[1]:
#     print(e)
##########################################




##########################################
        #TEST Alice et Bob v0#  #fonctionnel
##########################################

# aliceAndBobInstance=AliceAndBob0()

# semantic2RGInstance=Semantic2RG(aliceAndBobInstance)

# pr=ParentTraceur(semantic2RGInstance)

# R=bfsSearch(pr,lambda n: n[0]=="EnSectionCritiqueAlice" and n[1]=="EnSectionCritiqueBob")

# for e in R[1]:
#     print(e)

# print("------------")
# print("------------")
# print()
# pr.printParentsABV1(R[0])


##########################################





##########################################
        #TEST Alice et Bob v1#  #a completer
##########################################

aliceAndBobInstance=AliceAndBobV1()

semantic2RGInstance=Semantic2RG(aliceAndBobInstance)

pr=ParentTraceur(semantic2RGInstance)

R=bfsSearch(pr,lambda n: n[0]=="attendAlice" and n[1]=="attendBob")     #la query ne permet pas vraiment de detecter un deadlock how to avec seulement le noeud en parametre, Mais puisqu'on connais deja le couple d'etat ou on a deadlock, on specifie ce couple de facon explicite

for e in R[1]:
    print(e)

print("------------")
print("------------")
print()
pr.printParentsABV1(R[0])


##########################################