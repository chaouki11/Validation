
#module containing utilty functions

from collections import deque



# def add_trace(func):
#     def wrapper(graph, query,includeTrace):
#         if includeTrace==True:  # Check if the decorated function is traceHanoi

#             visited = set()
#             queue = deque()

#             for root in graph.getRoots():
#                 queue.append((root, []))  # Include an empty list to store the trace

#             while queue:
#                 node, trace = queue.popleft()
#                 if node not in visited:
#                     visited.add(node)

#                     if query(node):
#                         return visited,trace + [node.towers]  # Return the trace if the final state is reached

#                     unvisited = [(n, trace + [n.towers]) for n in graph.getNeighbors(node) if n not in visited]
#                     queue.extend(unvisited)

#             return None,None

#         else:  # For other functions, return only the visited array
#             return func(graph, query)
#     return wrapper

# def parent_traceur(pr):
#     print("start")
#     for x in pr.parents:
#         print(x.towers)
    

# Original bfsSearch function
# @add_trace
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




#function to print the nodes visited by the BFS search
# def print_visited_nodes(searchResult):
#     print("BFS search visited nodes: \n\n")
#     result = searchResult[0] if isinstance(searchResult, tuple) else searchResult 
#     for e in result:
#             print(e.towers)

def print_visited_nodes(searchResult):
    print("BFS search visited nodes: \n\n")
    for e in searchResult[0]:
            print(e.towers)


#function to print the trace of the solution
def print_hanoi_trace_for_direct_solution(searchResult):
    trace = searchResult[1] if isinstance(searchResult, tuple) else "pass"
    if trace!="pass": 
        print("\n\nTrace : \n\n")
        if trace:
            for idx, towers in enumerate(trace):
                print(f"Step {idx + 1}: {towers}")
        else:
            print("No solution found.")
    



def get_trace(self, node):
        trace = []
        current = node
        while current is not None:
            trace.append(current)
            current = self.parents.get(current)
        return trace[::-1]


# def get_trace(searchResult):
#      for x in len(searchResult.parents):
#           print()
     

#fonction qui affiche trace
# def printParents(gr,last):
#         lap=last
#         value=gr.parents[last]

#         while value is not None and len(value) is not 0:
#             print(f"{lap.towers}: {value[0].towers}")

#             lap=value[0]
#             value=gr.parents[lap]
