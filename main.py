

#define a hanoiGraph
from ParentTraceur import ParentTraceur
from hanoiNode import isFinal
from myhanoiGraph import HanoiRG
from utilities import bfsSearch, print_visited_nodes


gr=HanoiRG()

pr=ParentTraceur(gr)

#parentTraceur(gr)

R=bfsSearch(pr,isFinal,includeTrace=True)


#print the visited nodes when using the BFS search
print_visited_nodes(R)
#print the trace for finding the solutino  
#print_hanoi_trace_for_direct_solution(R)
# parent_traceur(pr)
# get_trace(R[1])

print("-----------------")
print("-----------------")
print("-----------------")
#fonction qui affiche la trace
pr.printParents(R[1])