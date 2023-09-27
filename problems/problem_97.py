#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
from collections import defaultdict

class Graph:
    """
    A class to represent an undirected graph using adjacency lists.
    """

    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Adds an edge between two vertices in the graph.

        Args:
            u: First vertex of the edge.
            v: Second vertex of the edge.
        """
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start_vertex):
        """
        Performs Breadth-First Search (BFS) traversal of the graph starting from a given vertex.

        Args:
            start_vertex: The vertex to start BFS traversal from.

        Returns:
            list: The BFS traversal order.
        """
        pass