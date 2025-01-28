#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
# from PIL import Image
import sys


sys.setrecursionlimit(1000000)



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

R = (0, 1)
L = (0, -1)
U = (-1, 0)
D = (1, 0)


def main():
    position = time.time()

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
    print(f"Data Parse Execution Time: {1000*(parse_time - position)} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time)} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time)} ms")
    print(f"Total Execution Time:      {1000*(part2_time - position)} ms")
    print("---------------------------------------------------")


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()
    data = [line.split() for line in data]
    return data

def flood_fill(data, position, total_length, total_width):
    if data[position[0]][position[1]] == "#":
        return
    
    data[position[0]][position[1]] = "#"

    for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_position = (position[0]+direction[0], position[1]+direction[1])

        if 0 <= new_position[0] < total_length and 0 <= new_position[1] < total_width:
            flood_fill(data, new_position, total_length, total_width)
    
    return data


def part1(data):
    trench = set()
    position = (0,0)
    minleft = 0
    maxright = 0
    minup = 0
    maxdown = 0
    for (direction, distance, _) in data:
        distance = int(distance)
        match direction:
            case "D":
                direction = D
            case "U":
                direction = U
            case "R":
                direction = R
            case "L":
                direction = L
        for _ in range(distance):
            position = (position[0]+direction[0], position[1]+direction[1])
            trench.add(position)
            if position[0] < minup:
                minup = position[0]
            if position[0] > maxdown:
                maxdown = position[0]
            if position[1] > maxright:
                maxright = position[1]
            if position[1] < minleft:
                minleft = position[1]

    normalized_trench = set()
    for hole in trench:
        normalized_trench.add((hole[0] - minup, hole[1] - minleft))

    total_width = maxright - minleft + 1
    total_length = maxdown - minup + 1

    # Create a new image with a white background
    # img = Image.new("RGB", (total_width, total_length), "white")
    # pixels = img.load()

    # # Iterate through all (y, x) positions
    # for y in range(total_length):
    #     for x in range(total_width):
    #         if (y, x) in normalized_trench:
    #             pixels[x, y] = (0, 0, 0)  # Black for positions in the set
    #         else:
    #             pixels[x, y] = (255, 255, 255)  # White for positions not in the set

    # # Save the image
    # img.save("trench.bmp")
    # print(f"Image saved as trench.bmp")

    filled_trench = [["." for _ in range(total_width)] for _ in range(total_length)]
    for hole in normalized_trench:
        filled_trench[hole[0]][hole[1]] = "#"
    

    # note to self: position (60, 300) was not found programmatically, but rather I kept changing
    # these values and looking at the filled_trench.bmp image until I had correctly chosen
    # a starting point that was within the enclosed area.
    data = flood_fill(filled_trench, (60, 300), total_length, total_width)

    #Create a new image with a white background
    # img = Image.new("RGB", (total_width, total_length), "white")
    # pixels = img.load()

    # # Iterate through all (y, x) positions
    # for y in range(total_length):
    #     for x in range(total_width):
    #         if data[y][x] == "#":
    #             pixels[x, y] = (0, 0, 0)  # Black for positions in the set
    #         else:
    #             pixels[x, y] = (255, 255, 255)  # White for positions not in the set

    # # Save the image
    # img.save("filled_trench.bmp")
    # print(f"Image saved as filled_trench.bmp")

    total = 0
    for y in range(total_length):
        for x in range(total_width):
            if data[y][x] == "#":
                total += 1
    
    return total


def part2(data):
    return None


if __name__ == "__main__":
    main()