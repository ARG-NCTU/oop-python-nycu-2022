import pytest
from lecture3_graph import *


git@github.com:billwang0517/oop-python-nycu.git```python
class TestDigraph:
    """
    This class is used to test the functionality of the Digraph class.
    """

    def setup_method(self):
        """
        This method is called before each test method is executed.
        It sets up the graph, nodes, and edges that will be used in the tests.
        """
        self.graph = Digraph()  # Initialize a new Digraph object
        self.node1 = Node('1')  # Initialize a new Node object with value '1'
        self.node2 = Node('2')  # Initialize a new Node object with value '2'
        self.node3 = Node('3')  # Initialize a new Node object with value '3'
        self.edge1 = Edge(self.node1, self.node2)  # Initialize a new Edge object between node1 and node2
        self.edge2 = Edge(self.node2, self.node3)  # Initialize a new Edge object between node2 and node3

 def test_add_node(self):
    """
    This method tests the 'add_node' method of the Digraph class.
    
    It first adds 'node1' to the graph and then checks if 'node1' is in the graph using the 'has_node' method.
    It also checks that 'node2' (which has not been added to the graph) is not in the graph.
    """
    self.graph.add_node(self.node1)  # Add 'node1' to the graph
    assert self.graph.has_node(self.node1)  # Check if 'node1' is in the graph
    assert not self.graph.has_node(self.node2)  # Check if 'node2' is not in the graph

 @pytest.mark.xfail(raises=ValueError)
def test_add_edge(self):
    """
    This method tests the 'add_edge' method of the Digraph class.
    
    It first adds 'node1' and 'node2' to the graph, then adds an edge between them.
    It checks if 'node2' is a child of 'node1' in the graph.
    It also tries to add edges with nodes that are not in the graph, which should raise a ValueError.
    """
    self.graph.add_node(self.node1)  # Add 'node1' to the graph
    self.graph.add_node(self.node2)  # Add 'node2' to the graph
    self.graph.add_edge(self.edge1)  # Add an edge between 'node1' and 'node2'
    assert self.node2 in self.graph.children_of(self.node1)  # Check if 'node2' is a child of 'node1'
    self.graph.add_edge(Edge(self.node2, Node('4')))  # Try to add an edge with a node not in the graph
    self.graph.add_edge(Edge(Node('5'), Node('6')))  # Try to add an edge with nodes not in the graph

@pytest.mark.xfail(raises=ValueError)
def test_children_of(self):
    """
    This method tests the 'children_of' method of the Digraph class.
    
    It first adds 'node1', 'node2', and 'node3' to the graph, then adds edges between them.
    It checks if the children of 'node1' and 'node2' in the graph are as expected.
    """
    self.graph.add_node(self.node1)  # Add 'node1' to the graph
    self.graph.add_node(self.node2)  # Add 'node2' to the graph
    self.graph.add_edge(self.edge1)  # Add an edge between 'node1' and 'node2'
    self.graph.add_edge(self.edge2)  # Add an edge between 'node2' and 'node3'
    assert self.graph.children_of(self.node1) == [self.node2]  # Check if the children of 'node1' are as expected
    assert self.graph.children_of(self.node2) == [self.node3]  # Check if the children of 'node2' are as expected

def test_has_node(self):
    """
    This method tests the 'has_node' method of the Digraph class.
    
    It first adds 'node1' to the graph, then checks if 'node1' is in the graph and if a node not in the graph is not in the graph.
    """
    self.graph.add_node(self.node1)  # Add 'node1' to the graph
    assert self.graph.has_node(self.node1)  # Check if 'node1' is in the graph
    assert not self.graph.has_node(Node('4'))  # Check if a node not in the graph is not in the graph

def test_get_node(self):
    """
    This method tests the 'get_node' method of the Digraph class.
    
    It first adds 'node1' to the graph, then checks if the node returned by 'get_node' is the same as 'node1'.
    """
    self.graph.add_node(self.node1)  # Add 'node1' to the graph
    assert self.graph.get_node('1') == self.node1  # Check if the node returned by 'get_node' is the same as 'node1'
