#return the solution only with no talking keeping in mind that it will be directly inputted into a python file
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        # Implement this function
        pass

    def add_edge(self, start_vertex, end_vertex):
        # Implement this function
        pass

    def depth_first_search(self, start_vertex):
        # Implement this function
        pass


class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, neighbor):
        # Implement this function
        pass

    def __str__(self):
        return str(self.key)