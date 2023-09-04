def test_add_vertex(graph_cls, vertex_cls):
    graph = graph_cls()
    graph.add_vertex(vertex_cls('A'))
    assert len(graph.vertices) == 1

    graph.add_vertex(vertex_cls('B'))
    graph.add_vertex(vertex_cls('C'))
    assert len(graph.vertices) == 3

    assert graph.vertices['A'].key == 'A'
    assert graph.vertices['B'].key == 'B'
    assert graph.vertices['C'].key == 'C'

def test_add_edge(graph_cls, vertex_cls):
    graph = graph_cls()
    vertex_a = vertex_cls('A')
    vertex_b = vertex_cls('B')
    vertex_c = vertex_cls('C')

    graph.add_vertex(vertex_a)
    graph.add_vertex(vertex_b)
    graph.add_vertex(vertex_c)

    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_b, vertex_c)
    graph.add_edge(vertex_c, vertex_a)

    assert len(vertex_a.neighbors) == 1
    assert len(vertex_b.neighbors) == 1
    assert len(vertex_c.neighbors) == 1

    assert vertex_a.neighbors[0] == vertex_b
    assert vertex_b.neighbors[0] == vertex_c
    assert vertex_c.neighbors[0] == vertex_a

def test_add_neighbor(vertex_cls):
    vertex_a = vertex_cls('A')
    vertex_b = vertex_cls('B')

    vertex_a.add_neighbor(vertex_b)
    assert len(vertex_a.neighbors) == 1
    assert vertex_a.neighbors[0] == vertex_b

def test_depth_first_search(graph_cls, vertex_cls):
    graph = graph_cls()
    vertex_a = vertex_cls('A')
    vertex_b = vertex_cls('B')
    vertex_c = vertex_cls('C')

    graph.add_vertex(vertex_a)
    graph.add_vertex(vertex_b)
    graph.add_vertex(vertex_c)

    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_b, vertex_c)
    graph.add_edge(vertex_c, vertex_a)

    result = graph.depth_first_search(vertex_a)
    assert result == ['A', 'B', 'C']