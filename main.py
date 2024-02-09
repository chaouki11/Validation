

#define a hanoiGraph
import random
from ParentTraceur import ParentTraceur
from hanoiNode import isFinal
from myhanoiGraph import HanoiRG
from Semantic2RG import Semantic2RG
from OneBitClock import OneBitClock
from AliceEtBob import AliceAndBob0
from AliceAndBobV1 import AliceAndBobV1
from SoupLangage import Piece, SoupSemantics, SoupSpecification
from AliceBobSoupConfig import AliceBobConf
from AliceBobSOupConfigV1 import AliceBobConfV1
from HanoiSoupConfig import HanoiSoupConfig
from DependantSemantics import DependantSoupSemantics
from StepSyncComposition import StepSynchComposition
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




# ##########################################
#         #TEST Soup langage AlicebobV0 avec soup #fonctionnel
# ##########################################

# def p1a_a(x,op):
#     if op==0:# for alice
#         x.state_Alice=(x.state_Alice+1)%3
#         return x
#     else:#for bob
#         x.state_Bob=(x.state_Bob+1)%3
#         return x
    

# p1a=Piece("Alice veux",lambda x: True,lambda x: p1a_a(x,0))
# p2a=Piece("Alice entre",lambda x: True,lambda x: p1a_a(x,0))
# p3a=Piece("Alice sort",lambda x: True,lambda x: p1a_a(x,0))
# p1b=Piece("Bob veux",lambda x: True,lambda x: p1a_a(x,1))
# p2b=Piece("Bob entre",lambda x:True,lambda x: p1a_a(x,1))
# p3b=Piece("Bob sort",lambda x: True,lambda x: p1a_a(x,1))
# Lp=[p1a,p2a,p3a,p1b,p2b,p3b]
# random.shuffle(Lp)

# initials=[AliceBobConf()]
# soup=SoupSpecification(initials,Lp)
# soupSem=SoupSemantics(soup)
# s=Semantic2RG(soupSem)
# pr=ParentTraceur(s)
# R=bfsSearch(pr,lambda n: n.state_Bob==2)

# print("------------")
# print("---- chemin BFS----")
# print()

# for e in R[1]:
#     print(e)

# print("------------")
# print("---- Trace ----")
# print()
# pr.printParentsABSoup(R[0])

# ##########################################





##########################################
        #TEST Soup langage AlicebobV1 avec soup #fonctionnel
##########################################

# def p1a_a(x,op):
#     if op==0:# for alice
#         if x.state_Alice==0:
#             x.flag_Alice=1
#         x.state_Alice=(x.state_Alice+1)%3
#         if x.state_Alice==0:
#             x.flag_Alice=0
#         return x
#     else:#for bob
#         if x.state_Bob==0:
#             x.flag_Bob=1
#         x.state_Bob=(x.state_Bob+1)%3
#         if x.state_Bob==0:
#             x.flag_Bob=0
#         return x
    

# p1a=Piece("Alice veux",lambda x: x.state_Alice==0,lambda x: p1a_a(x,0))
# p2a=Piece("Alice entre",lambda x: x.flag_Bob==0,lambda x: p1a_a(x,0))
# p3a=Piece("Alice sort",lambda x: x.state_Alice==2,lambda x: p1a_a(x,0))
# p1b=Piece("Bob veux",lambda x: x.state_Bob==0,lambda x: p1a_a(x,1))
# p2b=Piece("Bob entre",lambda x:x.flag_Alice==0,lambda x: p1a_a(x,1))
# p3b=Piece("Bob sort",lambda x: x.state_Bob==2,lambda x: p1a_a(x,1))
# Lp=[p1a,p2a,p3a,p1b,p2b,p3b]
# random.shuffle(Lp)

# initials=[AliceBobConfV1()]
# soup=SoupSpecification(initials,Lp)
# soupSem=SoupSemantics(soup)
# s=Semantic2RG(soupSem)
# pr=ParentTraceur(s)
# R=bfsSearch(pr,lambda n: not(s.getNeighbors(n)))

# print("------------")
# print("---- chemin BFS----")
# print()

# for e in R[1]:
#     print(e)

# print("------------")
# print("---- Trace ----")
# print()

# pr.printParentsABSoup(R[0])

##########################################




##########################################
        #TEST Soup Hanoi    #fonctionnel
##########################################

# def hpa(x,source,destination):
#     return x.move_disk(source, destination)

# def hgarde(x,source,destination):
#     if source != destination and x.can_move(source, destination):
#         return True
#     return False

# gardes=[(lambda x,i=i,j=j:hgarde(x,i,j)) for i in range(3) for j in range(3) if i!=j]
# actions=[(lambda x,i=i,j=j:hpa(x,i,j)) for i in range(3) for j in range(3) if i!=j]

# initials=[HanoiSoupConfig(3)]
# #print(hpa(HanoiSoupConfig(3),0,1))
# Lp=[Piece("deplacement disque: ",gardes[k],actions[k]) for k in range(len(actions))]

# soup=SoupSpecification(initials,Lp)
# soupSem=SoupSemantics(soup)
# s=Semantic2RG(soupSem)
# pr=ParentTraceur(s)
# R=bfsSearch(pr,lambda n:isFinal(n))



# print("------------")
# print("---- chemin BFS----")
# print()

# for e in R[1]:
#     print(e)


# print("------------")
# print("---- Trace ----")
# print()
# pr.printParentsHanoi(R[0])


##########################################




##########################################
        #TEST propriété et composition    #à compléter
##########################################


#lhs=model(alice et bob)
#rhs=propriété(bucchi)
#car propriete depend du model et rhs depend de lhs
lhs=SoupSpecification(initials1,Lp1)
rhs_soup=SoupSpecification(initials2,Lp2)
rhs=DependantSoupSemantics(rhs_soup)
dss=StepSynchComposition(lhs,rhs)
s=Semantic2RG(dss)
pr=ParentTraceur(s)
R=bfsSearch(pr,lambda n:n)






##########################################





##########################################
        #TEST detection de tagged cycles    #a faire
##########################################










##########################################


