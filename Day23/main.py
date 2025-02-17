#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
from collections import deque

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

    #grid based input
    data = [list(line.strip()) for line in data]

    return data

def print_node_path(data, longest_path, length, width):
    index_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
    for y in range(length):
        for x in range(width):
            if (y,x) in longest_path:
                print(f"{RED}{index_list[longest_path.index((y,x))]}{RESET}", end="")
            elif (y,x) == (31,107):
                print(f"{GREEN}N{RESET}", end="")
            else:
                print(data[y][x], end="")
        print()


def part1(data):
    length = len(data)
    width = len(data[0])

    for x in range(width):
        if data[0][x] == ".":
            start = (0,x)
            break
    
    for x in range(width):
        if data[length-1][x] == ".":
            end = (length-1,x)
            break
    
    stack = deque()
    stack.append((start, set()))
    paths = []
    while stack:
        current_position, visited = stack.popleft()

        visited.add(current_position)

        if current_position == end:
            paths.append(visited)
            continue
    
        
        if data[current_position[0]][current_position[1]] != ".":
            if data[current_position[0]][current_position[1]] == ">":
                if (current_position[0], current_position[1]+1) not in visited:
                    stack.append(((current_position[0], current_position[1]+1), visited.copy()))
            elif data[current_position[0]][current_position[1]] == "<":
                if (current_position[0], current_position[1]-1) not in visited:
                    stack.append(((current_position[0], current_position[1]-1), visited.copy()))
            elif data[current_position[0]][current_position[1]] == "^":
                if (current_position[0]-1, current_position[1]) not in visited:
                    stack.append(((current_position[0]-1, current_position[1]), visited.copy()))
            elif data[current_position[0]][current_position[1]] == "v":
                if (current_position[0]+1, current_position[1]) not in visited:
                    stack.append(((current_position[0]+1, current_position[1]), visited.copy()))
        else:
            for direction in [(1,0), (-1,0), (0,1), (0, -1)]:
                next_position = (current_position[0] + direction[0], current_position[1] + direction[1])
                if 0 <= next_position[0] < length and 0 <= next_position[1] < width and data[next_position[0]][next_position[1]] != "#":
                    if next_position not in visited:
                        stack.append((next_position, visited.copy()))

    max_length = 0
    for path in paths:
        if len(path) - 1 > max_length:
            max_length = len(path) -1


    return max_length


def part2(data):

    length = len(data)
    width = len(data[0])

    for x in range(width):
        if data[0][x] == ".":
            start = (0,x)
            break
    
    for x in range(width):
        if data[length-1][x] == ".":
            end = (length-1,x)
            break
    
    # Find all the intersections ("nodes")
    nodes = set()
    nodes.add(start)
    nodes.add(end)
    for y in range(length):
        for x in range(width):
            if data[y][x] in [".", "v", "^", ">", "<"]:
                sides = 0
                for direction in [(1,0), (-1,0), (0,1), (0, -1)]:
                    neighbor = (y + direction[0], x + direction[1])
                    if 0 <= neighbor[0] < length and 0 <= neighbor[1] < width and data[neighbor[0]][neighbor[1]] in [".", "v", "^", ">", "<"]:
                        sides += 1
                if sides >=3:
                    nodes.add((y,x))

    # Determine the distance between a node and all the nodes that it can reach (without going through another node)
    connections = {node: {} for node in nodes}  # Initialize dictionary with all nodes

    for start in nodes:
        stack = [(start, 0, start)]  # (current_position, pathlength, original_node)
        visited = set()

        while stack:
            current_position, pathlength, og_node = stack.pop()

            # Stop if we hit another node (but don't stop at the starting node itself)
            if current_position in nodes and current_position != og_node:
                connections[og_node][current_position] = pathlength
                connections[current_position][og_node] = pathlength  # Ensure bidirectional storage
                continue  # Stop this path

            # Explore all four directions
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_position = (current_position[0] + direction[0], current_position[1] + direction[1])

                if (
                    0 <= next_position[0] < length  # Stay within grid bounds
                    and 0 <= next_position[1] < width
                    and data[next_position[0]][next_position[1]] != "#"  # Avoid walls
                    and next_position not in visited  # Avoid revisiting same path
                ):
                    visited.add(next_position)
                    stack.append((next_position, pathlength + 1, og_node))  # Continue search

    # # Debugging: Print connections
    # for key, value in connections.items():
    #     print(f"{key} -> {value}")


    # Pathfinding algorithm using nodes to find the longest path between start and end
    stack = [((19,5), ((0,1),), 147)]
    max_length = 0
    longest_path = tuple()

    while stack:
        current_node, visited_nodes, pathlength = stack.pop()  # DFS for deep exploration first

        if current_node == (137,131):
            pathlength += 31
            if pathlength > max_length:
                new_visited = visited_nodes + (current_node,) + ((140,139),)
                max_length = pathlength
                longest_path = new_visited
            continue

        if current_node in visited_nodes:
            continue  # Avoid cycles

        # Create a new visited path
        new_visited = visited_nodes + (current_node,)  # Tuples are immutable, faster than copying sets

        for neighbor, distance in connections.get(current_node, {}).items():
            if neighbor not in visited_nodes:  # Only visit unvisited nodes
                stack.append((neighbor, new_visited, pathlength + distance))

    # # Prints the path one node at a time, listing the node, the distance from the last node, and the total length so far
    # total_length = 0
    # for i, node in enumerate(longest_path):
    #     if i == 0:
    #         pass
    #     else:
    #         prev_node = longest_path[i-1]
    #         for place in connections[node]:
    #             if prev_node == place:
    #                 total_length += connections[node][place]
    #                 print(node, connections[node][place], total_length)

    ## Prints the whole grid with the nodes in red and enumerated based on the order they are visited
    # print_node_path(data, longest_path, length, width)       

    return max_length


if __name__ == "__main__":

    main()