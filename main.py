

#define a hanoiGraph
from ParentTraceur import ParentTraceur
from hanoiNode import isFinal
from myhanoiGraph import HanoiRG
from Semantic2RG import Semantic2RG
from OneBitClock import OneBitClock
from AliceEtBob import AliceAndBob0
from AliceAndBobV1 import AliceAndBobV1
from SoupLangage import Piece, SoupSemantics, SoupSpecification
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
        #TEST Alice et Bob v1#  #fonctionnel
##########################################

# aliceAndBobInstance=AliceAndBobV1()

# semantic2RGInstance=Semantic2RG(aliceAndBobInstance)

# pr=ParentTraceur(semantic2RGInstance)

# R=bfsSearch(pr,lambda n: not (semantic2RGInstance.getNeighbors(n)))   #detecter deadlock
# for e in R[1]:
#     print(e)

# print("------------")
# print("------------")
# print()
# pr.printParentsABV1(R[0])


##########################################




##########################################
        #TEST Soup langage 
##########################################

p1=Piece("nom1",lambda x: 1!=0,lambda x: print("nom 1"))
p2=Piece("nom2",lambda x: 1!=0,lambda x: print("nom 2"))

soup=SoupSpecification()
soupSem=SoupSemantics(soup)
s=Semantic2RG(soupSem)
R=bfsSearch(s,lambda n: n)


##########################################