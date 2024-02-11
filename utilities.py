
#module containing utilty functions

from collections import deque

#traversal BFS
def bfsSearch(graph, query):
    visited = set()
    queue = deque()

    for root in graph.getRoots():
        queue.append(root)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)

            if query(node):
                return node,visited

            unvisited = [n for n in graph.getNeighbors(node) if n not in visited]
            queue.extend(unvisited)
    return None,visited

#function to print the visited nodes
def print_visited_nodes_hanoi(searchResult):
    print("BFS search visited nodes: \n\n")
    for e in searchResult[1]:
            print(e.towers)

#fonction pour détecter les boucles
def cycledetect(pr):
        cyleElem=[]
        R=bfsSearch(pr,lambda n:n in pr.getNeighbors(n))
        while R[0] is not None:
                cyleElem.append(R[0])
                R=bfsSearch(pr,lambda n:n in pr.getNeighbors(n) and n not in cyleElem)

        for x in cyleElem:
                print(x)