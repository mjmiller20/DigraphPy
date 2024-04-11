# digraph.py
# Author: Michael Miller 11005764@live.mercer.edu
# Digraph class for the network simulator

class node:
    def __init__(self, name, location, speed):
        self.name = name
        self.location = location
        self.speed = speed
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.speed = 0
    
    def __init__(self, name):
        self.name = name
        self.location = 0
        self.speed = 0
    
    def __str__(self) -> str:
        return (self.name + "\nLocation: " + self.location + "\nSpeed: " + self.speed)


class edge:
    def __init__(self, node1, node2, distance, latency, error_rate, speed):
        self.node1 = node1
        self.node2 = node2
        self.distance = distance
        self.latency = latency
        self.error_rate = error_rate
        self.speed = speed
    
    def __str__(self) -> str:
        return (self.node1 + " -> " + self.node2 + "\nDistance: " + self.distance + "\nLatency: " + self.latency + "\nError Rate: " + self.error_rate + "\nSpeed: " + self.speed)


class graph:
    def __init__(self):
        self.nodes = []
        self.graph = []

    def add_node(self, name, location, speed):
        self.nodes.append(node(name, location, speed))
    
    def add_node(self, name, location):
        self.nodes.append(node(name, location))

    def add_node(self, name):  
        self.nodes.append(node(name))
    
    def __locate_node(self, name):
        for n in self.nodes:
            if n.name == name:
                return n
        return None

    def add_edge(self, node1, node2, distance, latency, error_rate):
        n1 = self.__locate_node(node1)
        n2 = self.__locate_node(node2)
        self.graph.append(edge(n1, n2, distance, latency, error_rate, n1.speed if n1.speed < n2.speed else n2.speed))

    def get_edges_on_node(self, name):
        edges = []
        for e in self.graph:
            if e.node1.name == name:
                edges.append(e)
        return edges
    
    def get_nodes(self):
        return self.nodes
    
    def get_edges(self):
        return self.graph
    
    def __str__(self) -> str:
        s = ""
        for e in self.graph:
            s += str(e) + "\n"
        return s
    
    def change_node_speed(self, name, speed):
        n = self.__locate_node(name)
        n.speed = speed

    def change_edge_latency(self, node1, node2, latency):
        for e in self.graph:
            if e.node1.name == node1 and e.node2.name == node2:
                e.latency = latency
                return
        print("Edge not found")
    
    def change_edge_error_rate(self, node1, node2, error_rate):
        for e in self.graph:
            if e.node1.name == node1 and e.node2.name == node2:
                e.error_rate = error_rate
                return
        print("Edge not found")

    def change_edge_distance(self, node1, node2, distance):
        for e in self.graph:
            if e.node1.name == node1 and e.node2.name == node2:
                e.distance = distance
                return
        print("Edge not found")
    