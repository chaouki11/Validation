

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
        #TEST Alice et Bob v0#  #fonctionnel
##########################################

aliceAndBobInstance=AliceAndBob0()

semantic2RGInstance=Semantic2RG(aliceAndBobInstance)

pr=ParentTraceur(semantic2RGInstance)

R=bfsSearch(pr,lambda n: n[0]=="EnSectionCritiqueAlice" and n[1]=="EnSectionCritiqueBob")

for e in R[1]:
    print(e)

print("------------")
print("------------")
print()
pr.printParentsABV1(R[0])


##########################################
