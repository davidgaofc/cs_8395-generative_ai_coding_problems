from problems.problem_19 import Graph

def test_add_edge():
    graph = Graph()
    graph.add_edge("A", "B", 4)
    graph.add_edge("B", "C", 5)
    assert len(graph.graph) == 2
    assert graph.graph["A"]["B"] == 4
    assert graph.graph["B"]["C"] == 5

def test_shortest_path():
    graph = Graph()
    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "C", 5)
    graph.add_edge("B", "D", 10)
    graph.add_edge("C", "D", 3)
    graph.add_edge("D", "E", 7)
    graph.add_edge("E", "A", 6)

    shortest_path = graph.shortest_path("A", "D")
    assert shortest_path == ["A", "C", "D"]