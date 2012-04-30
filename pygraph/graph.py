class Vertex:
    def __init__(self, data):
        self.data = data
        self.in_edges = []
        self.out_edges = []


class Edge:
    def __init__(self, data, v1, v2):
        """
        creates an edge from v1->v2
        """
        self.data = data
        self.v1 = v1
        self.v2 = v2


class Graph:
    def __init__(self):
        self.vertices = dict()

    def adjacent(self, x, y):
        """
        tests whether there is an edge from vertex x to vertex y.
        """
        pass

    def neighbors(self, x):
        """
        lists all nodes y such that there is an edge from x to y.
        """
        pass

    def add(self, x, y):
        """
        adds to G the edge from x to y, if it is not there.
        """
        pass

    def delete(self, x, y):
        """
        removes the edge from x to y, if it is there.
        """
        pass

"""
    def get_node_value(self, x): returns the value associated with the node x.
    set_node_value(G, x, a): sets the value associated with the node x to a.

Structures that associate values to the edges usually also provide:

    get_edge_value(G, x, y): returns the value associated to the edge (x,y).
    set_edge_value(G, x, y, v): sets the value associated to the edge (x,y) to v.
"""
