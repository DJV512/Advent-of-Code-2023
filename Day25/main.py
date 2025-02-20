#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import networkx as nx
import matplotlib.pyplot as plt

RESET = "\033[0m"         # Resets all styles
BLACK = "\033[30;1m"      # Black text
RED = "\033[31;1m"        # Red text
GREEN = "\033[32;1m"      # Green text
YELLOW = "\033[33;1m"     # Yellow text
BLUE = "\033[34;1m"       # Blue text
MAGENTGA = "\033[35;1m"   # Magenta text
CYAN = "\033[36;1m"       # Cyan text
WHITE = "\033[37;1m"      # White text

BOLD = "\033[1m"          # Bold text
UNDERLINE = "\033[4m"     # Underlined text

def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1 = part1(data)
    part1_time = time.time()
    answer2 = part2(data)
    part2_time = time.time()

    print("---------------------------------------------------")
    print(f"Part 1 Answer: {answer1}")
    print()
    print(f"Part 2 Answer: {answer2}")
    print()
    print(f"Data Parse Execution Time: {1000*(parse_time - start_time)} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time)} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time)} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start_time)} ms")
    print("---------------------------------------------------")


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()

    G = nx.Graph()
    for line in data:
        wire, other_wires = line.strip().split(": ")
        wires = other_wires.split(" ")
        for item in wires:
            G.add_edge(wire, item)

    return G


def part1(G):
    # First look at graph, to see which wires need to be disconnected
    # plt.figure(figsize=(8,6))
    # nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=10)
    # plt.show()

    G.remove_edge("vgf", "jpn")
    G.remove_edge("fdb", "txm")
    G.remove_edge("nmz", "mnl")

    # Redraw the figure after cutting the wires to make sure I cut the right ones
    # plt.figure(figsize=(8,6))
    # nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=700, font_size=10)
    # plt.show()

    # Determine the size of the two clusters and return their product
    components = list(nx.connected_components(G))  # List of sets of nodes
    cluster_sizes = [len(comp) for comp in components]

    return cluster_sizes[0]*cluster_sizes[1]


def part2(data):
    return None


if __name__ == "__main__":
    main()