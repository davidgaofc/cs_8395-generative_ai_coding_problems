from problems.problem_97 import Graph

def test_bfs():
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    assert graph.bfs(2) == [2, 0, 3, 1]