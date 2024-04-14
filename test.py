

import pytest
import digraph
import simulation

def test_node():
    n = digraph.node("node1", "location1", 1)
    assert n.name == "node1"
    assert n.location == "location1"
    assert n.speed == 1
    assert str(n) == "node1\nLocation: location1\nTransceiver Speed: 1"

def test_edge():
    n1 = digraph.node("node1", "location1", 1)
    n2 = digraph.node("node2", "location2", 2)
    e = digraph.edge(n1, n2, 1, 2, 0.1, 1)
    assert e.node1 == n1
    assert e.node2 == n2
    assert e.distance == 1
    assert e.latency == 2
    assert e.error_rate == 0.1
    assert e.speed == 1
    assert str(e) == """node1
Location: location1
Transceiver Speed: 1 -> node2
Location: location2
Transceiver Speed: 2
Distance: 1
Latency: 2
Error Rate: 0.1
Speed: 1"""

def test_graph():
    g = digraph.graph()
    n1 = digraph.node("node1", "location1", 1)
    n2 = digraph.node("node2", "location2", 2)
    g.add_node("node1", "location1", 1)
    g.add_node("node2", "location2", 2)
    assert g.get_edges() == []
    g.add_edge("node1", "node2", 1, 2, 0.1)
    e = digraph.edge(n1, n2, 1, 2, 0.1, 1)
    assert g.print_nodes() == None
    assert g.print_edges() == None

def test_main():
    assert simulation.main() == 0

if __name__ == "__main__":
    test_node()
    test_edge()
    test_graph()
    test_main()
    print("All tests passed!")
