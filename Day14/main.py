#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
from copy import deepcopy

cycle_detection_start = 119

def main():
    start = time.time()

    data, length, width = parse_data()
    parse_time = time.time()

    original_data = deepcopy(data)

    answer1 = part1(data, length, width)
    part1_time = time.time()
    answer2 = part2(original_data, length, width)
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
    data = [line.strip() for line in data]
    length = len(data)
    width = len(data[0])
    map = []
    for y in range(length):
        new_row=[]
        for x in range(width):
            new_row.append(data[y][x])
        map.append(new_row)
    return map, length, width

def print_map(map):
    for row in map:
        for column in row:
            print(column, end="")
        print()

def north(data, length, width):
    for y in range(1, length):
        for x in range(width):
            if data[y][x] == "O":
                move = False
                new_y = y-1
                while new_y>=0:
                    if data[new_y][x] == ".":
                        move = True
                    if data[new_y][x] == "#" or data[new_y][x] == "O":
                        if move:
                            data[new_y+1][x] = "O"
                            data[y][x] = "."
                        break
                    if new_y == 0:
                        if move:
                            data[new_y][x] = "O"
                            data[y][x] = "."
                        break
                    new_y -= 1

def south(data, length, width):
    for y in range(length-2, -1, -1):
        for x in range(width):
            if data[y][x] == "O":
                move = False
                new_y = y+1
                while new_y<length:
                    if data[new_y][x] == ".":
                        move = True
                    if data[new_y][x] == "#" or data[new_y][x] == "O":
                        if move:
                            data[new_y-1][x] = "O"
                            data[y][x] = "."
                        break
                    if new_y == length-1:
                        if move:
                            data[new_y][x] = "O"
                            data[y][x] = "."
                        break
                    new_y += 1
    
def east(data, length, width):
    for x in range(width-2, -1, -1):
        for y in range(length):
            if data[y][x] == "O":
                move = False
                new_x = x+1
                while new_x<width:
                    if data[y][new_x] == ".":
                        move = True
                    if data[y][new_x] == "#" or data[y][new_x] == "O":
                        if move:
                            data[y][new_x-1] = "O"
                            data[y][x] = "."
                        break
                    if new_x == width-1:
                        if move:
                            data[y][new_x] = "O"
                            data[y][x] = "."
                        break
                    new_x += 1
    
def west(data, length, width):
    for x in range(1, width):
        for y in range(length):
            if data[y][x] == "O":
                move = False
                new_x = x-1
                while new_x>=0:
                    if data[y][new_x] == ".":
                        move = True
                    if data[y][new_x] == "#" or data[y][new_x] == "O":
                        if move:
                            data[y][new_x+1] = "O"
                            data[y][x] = "."
                        break
                    if new_x == 0:
                        if move:
                            data[y][new_x] = "O"
                            data[y][x] = "."
                        break
                    new_x -= 1

def cycle(data, length, width):
    north(data, length, width)
    west(data, length, width)
    south(data, length, width)
    east(data, length, width)

def get_score(data, length, width):
    score = 0
    for y in range(0, length):
        for x in range(width):
            if data[y][x] == "O":
                score += (length-y)
    return score


def part1(data, length, width):
    north(data, length, width)
    score = get_score(data, length, width)
    return score


def part2(data, length, width):
    for z in range(1000):
        cycle(data, length, width)
        if z == cycle_detection_start:
            detector = deepcopy(data)
        if z > cycle_detection_start:
            if data == detector:
                repeat = z-cycle_detection_start
                break
    
    no_of_cycles = int((1000000000-(z+1))/repeat)
    last_repeat = z + 1 + no_of_cycles*repeat
    cycles_left = 1000000000-last_repeat
    for _ in range(cycles_left):
        cycle(data, length, width)

    score = get_score(data, length, width)
    
    return score


if __name__ == "__main__":
    main()