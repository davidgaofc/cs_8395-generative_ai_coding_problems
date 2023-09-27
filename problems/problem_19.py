#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
from collections import defaultdict

class Graph:
    def __init__(self):
        """
        Represents a weighted graph.

        This class allows users to add edges and find the shortest path.
        """
        self.graph = defaultdict(dict)

    # TODO: Implement this function
    def add_edge(self, source, destination, weight):
        """
        Adds a weighted edge to the graph.

        Args:
            source: Source vertex of the edge.
            destination: Destination vertex of the edge.
            weight: Weight of the edge.
        """
        pass

    # TODO: Implement this function
    def shortest_path(self, source, destination):
        """
        Finds the shortest path between two vertices in the graph.

        Args:
            source: Source vertex of the path.
            destination: Destination vertex of the path.

        Returns:
            List: List of vertices representing the shortest path.
        """
        pass