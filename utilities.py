
#module containing utilty functions

from collections import deque

#traversal BFS
def bfsSearch(graph, query,includeTrace=False):
    visited = set()
    queue = deque()

    for root in graph.getRoots():
        queue.append(root)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)

            if query(node):
                return visited,node

            unvisited = [n for n in graph.getNeighbors(node) if n not in visited]
            queue.extend(unvisited)
    return visited,node

#function to print the visited nodes
def print_visited_nodes(searchResult):
    print("BFS search visited nodes: \n\n")
    for e in searchResult[0]:
            print(e.towers)
