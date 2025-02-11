#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time

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

    start, wall, length, width = parse_data()
    parse_time = time.time()

    # answer1 = part1(start, wall, length, width)
    part1_time = time.time()
    answer2 = part2(start, wall, length, width)
    part2_time = time.time()

    print("---------------------------------------------------")
    # print(f"Part 1 Answer: {answer1}")
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

    map = []
    for line in data:
        new_line = []
        for char in line.strip():
            new_line.append(char)
        map.append(new_line)
    
    length = len(map)
    width = len(map[0])
    wall = set()
    for y in range(length):
        for x in range(width):
            if map[y][x] == "S":
                start = (y,x)
            elif map[y][x] == "#":
                wall.add((y,x))
    return start, wall, length, width


def print_reached_steps(current_positions, wall, length, width, gridsize):
    if gridsize == 1:
        range_start = 0
        range_end = length
    elif gridsize == 3:
        range_start = -length
        range_end = 2*length
    elif gridsize == 5:
        range_start = -2*length
        range_end = 3*length
    elif gridsize == 7:
        range_start = -3*length
        range_end = 4*length

    for y in range(range_start, range_end):
        for x in range(range_start, range_end):
            normalized_y = y % length
            normalized_x = x % width
            if (y,x) == (65,65):
                print(f"{RED}", end="")
            else:
                print(f"{RESET}", end="")
            if (normalized_y,normalized_x) in wall:
                print("#", end="")
            elif (y,x) in current_positions:
                print("O", end="")
            else:
                print(".", end="")
        print()
    print()

def print_reached_steps_file(current_positions, wall, length, width, gridsize, file):
    if gridsize == 1:
        range_start = 0
        range_end = length
    elif gridsize == 3:
        range_start = -length
        range_end = 2*length
    elif gridsize == 5:
        range_start = -2*length
        range_end = 3*length
    elif gridsize == 7:
        range_start = -3*length
        range_end = 4*length

    with open(file, "w") as file:
        for y in range(range_start, range_end):
            for x in range(range_start, range_end):
                normalized_y = y % length
                normalized_x = x % width
                if (normalized_y,normalized_x) in wall:
                    file.write("#")
                elif (y, x) in current_positions:
                    file.write("O")
                else:
                    file.write(".")
            file.write("\n")  
        file.write("\n") 

def print_reached_steps_html(current_positions, wall, length, width, gridsize, file):
    red = 0
    green = 0
    lower = int(gridsize/2)
    upper = lower+1
    range_start = -lower*length
    range_end = upper*length

    with open(file, "w") as file:
        file.write("<html><body><pre style='font-family: monospace;'>\n")
        for y in range(range_start, range_end):
            for x in range(range_start, range_end):
                normalized_y = y % length
                normalized_x = x % width
                if (normalized_y,normalized_x) in wall:
                    file.write("#")
                elif (y, x) in current_positions:
                    if 0 <= y < length and 0 <= x < width:
                        file.write("<span style='color: red;'>O</span>")
                        red +=1
                    else:
                        file.write("<span style='color: green;'>O</span>")
                        green+=1
                else:
                    file.write(".")
            file.write("\n")  
        file.write("</pre></body></html>") 
    print(f"{gridsize=}, {red=}, {green=}")


def part1(start, wall, length, width):
    number_steps = 65
    current_positions = set()
    current_positions.add(start)
    new_positions = set()
    for _ in range(number_steps):
        for position in current_positions:
            for direction in [(-1,0), (1,0), (0,1), (0,-1)]:
                next_position_y = position[0] + direction[0]
                next_position_x = position[1] + direction[1]
                if 0 <= next_position_y < length and 0 <= next_position_x < width and (next_position_y, next_position_x) not in wall:
                    new_positions.add((next_position_y, next_position_x))
        current_positions = new_positions
        new_positions = set()
    
    # print_reached_steps(current_positions, wall, length, width, 3)
    print_reached_steps_file(current_positions, wall, length, width, 3, file="output.txt")
    return len(current_positions)


def part2(start, wall, length, width):
    # q=5
    # z=11
    # results = {}
    # record_steps = [5, 10, 20, 25, 50, 64, 65, 66]
    # number_steps = 65 + 131*q
    # current_positions = set()
    # current_positions.add(start)
    # new_positions = set()
    # for i in range(number_steps):
    #     for position in current_positions:
    #         for direction in [(-1,0), (1,0), (0,1), (0,-1)]:
    #             next_position_y = position[0] + direction[0]
    #             next_position_x = position[1] + direction[1]
                
    #             normalized_y = next_position_y % length
    #             normalized_x = next_position_x % width

    #             if (normalized_y, normalized_x) not in wall:
    #                 new_positions.add((next_position_y, next_position_x))
    #     current_positions = new_positions
    #     new_positions = set()

        # if i+1 in record_steps:
        #     print(f"Number of steps: {i+1}, number of cells reached: {len(current_positions)}")
        #     results[i+1] = len(current_positions)
    # print_reached_steps_html(current_positions, wall, length, width, z, file="output.html")

    green = 86015
    step_up = 59810
    for q, i in enumerate(range(458, 26501366, 131)):
        if q%2 == 0:
            step_up += 29692
            green += step_up
        else:
            step_up += 29960
            green += step_up

        if q < 10:
            print(q, i, green, step_up)

    total = 7423 + green

    return total


if __name__ == "__main__":
    main()