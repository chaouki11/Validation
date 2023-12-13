
#module containing utilty functions

from collections import deque

#function that performs BFS search 
def bfsSearch(graph,query):
    visited = set()
    queue = deque()

    for root in graph.getRoots():
        queue.append(root)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            
            if query(node):
                return visited
            
            unvisited = [n for n in graph.getNeighbors(node) if n not in visited]
            queue.extend(unvisited)

    return visited

#function that returns the trace of hanoi solution
def traceHanoi(graph, query):
    visited = set()
    queue = deque()

    for root in graph.getRoots():
        queue.append((root, []))  # Include an empty list to store the trace

    while queue:
        node, trace = queue.popleft()
        if node not in visited:
            visited.add(node)

            if query(node):
                return trace + [node.towers]  # Return the trace if the final state is reached

            unvisited = [(n, trace + [n.towers]) for n in graph.getNeighbors(node) if n not in visited]
            queue.extend(unvisited)

    return None

#helper function to print the trace of hanoi solution
def print_trace_for_direct_solution(graph, query):
    trace = traceHanoi(graph, query)

    if trace:
        for idx, towers in enumerate(trace):
            print(f"Step {idx + 1}: {towers}")
    else:
        print("No solution found.")


