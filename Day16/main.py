#FILENAME = "sample2.txt"
#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
from collections import deque

NORTH = (-1, 0)
EAST = (0, 1)
SOUTH = (1, 0)
WEST = (0, -1)

start_place = (0, -1)
start_direction = EAST

def main():
    start = time.time()

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
    print(f"Data Parse Execution Time: {1000*(parse_time - start)} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time)} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time)} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start)} ms")
    print("---------------------------------------------------")


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()
    data = [list(line.strip()) for line in data]
    return data


def print_map(data, visited):
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (y,x) in visited:
                print("#", end="")
            else:
                print(data[y][x], end="")
        print()
    print()
    

def part1(data):
    length = len(data)
    width = len(data[0])
    visited_with_direction = set()
    visited = set()
    stack = deque()
    stack.append((start_place, start_direction))
    while stack:
        # print(stack)
        (y,x), direction = stack.popleft()
        visited_with_direction.add(((y,x), direction))
        next_position = (y+direction[0], x+direction[1])
        # print(next_position, direction)
        if 0 <= next_position[0] < length and 0 <= next_position[1] < width and (next_position, direction) not in visited_with_direction:
            if next_position not in visited:
                visited.add(next_position)
            if data[next_position[0]][next_position[1]] == ".":
                stack.append((next_position, direction))
            elif data[next_position[0]][next_position[1]] == "\\":
                if direction == EAST:
                    stack.append((next_position, SOUTH))
                elif direction == SOUTH:
                    stack.append((next_position, EAST))
                elif direction == NORTH:
                    stack.append((next_position, WEST))
                elif direction == WEST:
                    stack.append((next_position, NORTH))
            elif data[next_position[0]][next_position[1]] == "/":
                if direction == EAST:
                    stack.append((next_position, NORTH))
                elif direction == SOUTH:
                    stack.append((next_position, WEST))
                elif direction == NORTH:
                    stack.append((next_position, EAST))
                elif direction == WEST:
                    stack.append((next_position, SOUTH))
            elif data[next_position[0]][next_position[1]] == "|":
                if direction == EAST or direction == WEST:
                    stack.append((next_position, SOUTH))
                    stack.append((next_position, NORTH))
                elif direction == SOUTH or direction == NORTH:
                    stack.append((next_position, direction))
            elif data[next_position[0]][next_position[1]] == "-":
                if direction == SOUTH or direction == NORTH:
                    stack.append((next_position, WEST))
                    stack.append((next_position, EAST))
                elif direction == EAST or direction == WEST:
                    stack.append((next_position, direction))
        # print_map(data,visited)

    print_map(data, visited)
    cells = len(visited)
    return cells


def part2(data):
    return None


if __name__ == "__main__":
    main()