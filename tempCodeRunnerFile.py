gr=HanoiRG()
pr=ParentTraceur(gr)
R=bfsSearch(pr,isFinal)
print_visited_nodes_hanoi(R)
print("-----------------")
print("-----------------")
print("-----------------")
pr.printParents(R[1])
