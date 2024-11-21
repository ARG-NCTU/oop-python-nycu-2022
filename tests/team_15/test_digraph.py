import pytest
from lecture3_graph import *

class TestDigraph:
    def setup_method(self):
        self.graph = Digraph()
        self.node1 = Node('1')
        self.node2 = Node('2')
        self.node3 = Node('3')
        self.edge1 = Edge(self.node1, self.node2)
        self.edge2 = Edge(self.node2, self.node3)

    def test_add_node(self):
        self.graph.add_node(self.node1)
        assert self.graph.has_node(self.node1)
        assert not self.graph.has_node(self.node2)

    @pytest.mark.xfail(raises=ValueError)
    def test_add_edge(self):
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.graph.add_edge(self.edge1)
        assert self.node2 in self.graph.children_of(self.node1)
        self.graph.add_edge(Edge(self.node2, Node('4')))
        self.graph.add_edge(Edge(Node('5'), Node('6')))

    @pytest.mark.xfail(raises=ValueError)
    def test_children_of(self):
        self.graph.add_node(self.node1)
        self.graph.add_node(self.node2)
        self.graph.add_edge(self.edge1)
        self.graph.add_edge(self.edge2)
        assert self.graph.children_of(self.node1) == [self.node2]
        assert self.graph.children_of(self.node2) == [self.node3]

    def test_has_node(self):
        self.graph.add_node(self.node1)
        assert self.graph.has_node(self.node1)
        assert not self.graph.has_node(Node('4'))

    def test_get_node(self):
        self.graph.add_node(self.node1)
        assert self.graph.get_node('1') == self.node1

def test_build_city_graph():
    
    g = Digraph()

    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'):  # Create 7 nodes
        g.add_node(Node(name))

    g.add_edge(Edge(g.get_node('Boston'), g.get_node('Providence')))
    g.add_edge(Edge(g.get_node('Boston'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('Boston')))
    g.add_edge(Edge(g.get_node('Providence'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('New York'), g.get_node('Chicago')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Denver')))
    g.add_edge(Edge(g.get_node('Chicago'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('Phoenix')))
    g.add_edge(Edge(g.get_node('Denver'), g.get_node('New York')))
    g.add_edge(Edge(g.get_node('Los Angeles'), g.get_node('Boston')))

    print(g)
    assert len(g.edges) == 7 
    assert g.get_node('Boston').get_name() == 'Boston'
