from IRootedGraph import RootedGraph


class AliceAndBob(RootedGraph):
    def __init__(self):
        self.graph = dict()
        self.roots = []

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)

