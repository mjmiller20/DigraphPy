# simulation.py
# Author: Michael Miller 11005764@live.mercer.edu
# Simulation script for the network simulator using digraph class

from digraph import graph
import json

def main():
    with open("network.json", "r") as file:
        data = json.load(file)
        g = graph()
        for node in data["nodes"]:
            g.add_node(node["name"], node["location"], node["speed"])
        for edge in data["edges"]:
            g.add_edge(edge["node1"], edge["node2"], edge["distance"], edge["latency"], edge["error"])
        g.print_nodes()
        g.print_edges()
    return 0

if __name__ == "__main__":
    main()
