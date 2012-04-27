class Vertex:
    def __init__(self, data):
        self.data = data
        self.in_edges = []
        self.out_edges = []


class Edge:
    def __init__(self, data, v1, v2):
        self.data = data
        self.v1 = v1
        self.v2 = v2


class Graph:
    pass
