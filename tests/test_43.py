from problems.problem_43 import Graph

def test_add_edge():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)

    assert graph.dfs(1) == [1, 2, 3, 5, 4]
    assert graph.dfs(3) == [3, 5, 4, 2, 1]

def test_dfs():
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(4, 5)

    assert graph.dfs(1) == [1, 2, 3, 5, 4]
    assert graph.dfs(3) == [3, 5, 4, 2, 1]