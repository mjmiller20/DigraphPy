# digraph.py
# Author: Michael Miller 11005764@live.mercer.edu
# Digraph class for the network simulator

class node:
    def __init__(self, name, location, speed):
        self.name = name
        self.location = location
        self.speed = speed
    
    def __str__(self) -> str:
        return (self.name + "\nLocation: " + self.location + "\nTransceiver Speed: " + str(self.speed) + "Gbps")


class edge:
    def __init__(self, node1, node2, distance, latency, error_rate, speed):
        self.node1 = node1
        self.node2 = node2
        self.distance = distance
        self.latency = latency
        self.error_rate = error_rate
        self.speed = speed
    
    def __str__(self) -> str:
        return (str(self.node1) + " -> " + str(self.node2) + "\nDistance: " + str(self.distance) + "Km\nLatency: " + str(self.latency) + "ms\nError Rate: " + str(self.error_rate) + "%\nSpeed: " + str(self.speed) + "Gbps")

class valueError(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)

class dgraph:
    def __init__(self):
        self.nodes = []
        self.graph = []

    def add_node(self, name, location, speed):
        if name in [n.name for n in self.nodes]:
            raise valueError("Node already exists")
        self.nodes.append(node(name, location, speed))
    
    def __locate_node(self, name):
        for n in self.nodes:
            if n.name == name:
                return n
        return None

    def add_edge(self, node1, node2, distance, latency, error_rate):
        n1 = self.__locate_node(node1)
        n2 = self.__locate_node(node2)
        if(n1 == None or n2 == None):
            raise valueError("Node not found")
        self.graph.append(edge(n1, n2, distance, latency, error_rate, n1.speed if n1.speed < n2.speed else n2.speed))

    def get_edges_on_node(self, name):
        edges = []
        for e in self.graph:
            if e.node1.name == name or e.node2.name == name:
                edges.append(e)
        return edges
    
    def print_nodes(self):
        for n in self.nodes:
            print(n)
    
    def print_edges(self):
        for e in self.graph:
            print(e)
    
    def __str__(self) -> str:
        s = ""
        for e in self.graph:
            s += str(e) + "\n"
        return s
    
    def change_node_speed(self, name, speed):
        if name in [n.name for n in self.nodes]:
            n = self.__locate_node(name)
            n.speed = speed
        else:
            raise valueError("Node does not exist") 

    def change_edge_latency(self, node1, node2, latency):
        for e in self.graph:
            if (e.node1.name == node1 and e.node2.name == node2) or (e.node1.name == node2 and e.node2.name == node1):
                e.latency = latency
                return
        raise valueError("Edge not found")
    
    def change_edge_error_rate(self, node1, node2, error_rate):
        for e in self.graph:
            if (e.node1.name == node1 and e.node2.name == node2) or (e.node1.name == node2 and e.node2.name == node1):
                e.error_rate = error_rate
                return
        raise valueError("Edge not found")

    def change_edge_distance(self, node1, node2, distance):
        for e in self.graph:
            if (e.node1.name == node1 and e.node2.name == node2) or (e.node1.name == node2 and e.node2.name == node1):
                e.distance = distance
                return
        raise valueError("Edge not found")

class graph(dgraph):
    map = dgraph()
    def __init__(self):
        if self.map == None:
            self.map = dgraph()

    def add_node(self, name, location, speed):
        try:
            if type(name) != str or type(location) != str or type(speed) != int:
                raise valueError("Invalid type")
            if name in [n.name for n in self.map.nodes]:
                raise valueError("Node already exists")
            if speed <= 0:
                raise valueError("Speed must be a positive value")
            if name == "" or location == "":
                raise valueError("Name and location must not be empty")
            self.map.add_node(name, location, speed)
        except valueError as e:
            print(e.message)

    def add_edge(self, node1, node2, distance, latency, error_rate):
        try:
            if type(distance) != int or type(latency) != int or type(error_rate) != float:
                raise valueError("Invalid type")
            if distance <= 0 or latency <= 0 or error_rate < 0 or error_rate > 1:
                raise valueError("Numeric values must be nonzero positive values and error rate must be between 0 and 1")
            self.map.add_edge(node1, node2, distance, latency, error_rate)
        except valueError as e:
            print(e.message)
    
    def print_nodes(self):
        self.map.print_nodes()
    
    def print_edges(self):
        self.map.print_edges()
    
    def get_edges(self):
        return self.map.graph
    
    def get_nodes(self):
        return self.map.nodes
    
    def __str__(self) -> str:
        return str(self.map)
    
    def change_node_speed(self, name, speed):
        try:
            if type(speed) != int:
                raise valueError("Invalid type")
            if speed <= 0:
                raise valueError("Speed must be a positive value")
            self.map.change_node_speed(name, speed)
        except valueError as e:
            print(e.message)
    
    def change_edge_latency(self, node1, node2, latency):
        try:
            if type(latency) != int:
                raise valueError("Invalid type")
            if latency <= 0:
                raise valueError("Latency must be a positive value")
            self.map.change_edge_latency(node1, node2, latency)
        except valueError as e:
            print(e.message)

    def change_edge_error_rate(self, node1, node2, error_rate):
        try:
            if type(error_rate) != float:
                raise valueError("Invalid type")
            if error_rate < 0 or error_rate > 1:
                raise valueError("Error rate must be between 0 and 1")
            self.map.change_edge_error_rate(node1, node2, error_rate)
        except valueError as e:
            print(e.message)

    def change_edge_distance(self, node1, node2, distance):
        try:
            if type(distance) != int:
                raise valueError("Invalid type")
            if distance <= 0:
                raise valueError("Distance must be a positive value")
            self.map.change_edge_distance(node1, node2, distance)
        except valueError as e:
            print(e.message)
    
    def get_edges_on_node(self, name):
        try:
            if type(name) != str:
                raise valueError("Invalid type")
            return self.map.get_edges_on_node(name)
        except valueError as e:
            print(e.message)