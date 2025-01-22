#FILENAME = "sample2.txt"
#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
from copy import deepcopy

def main():
    start = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, answers = part1(data)
    part1_time = time.time()
    answer2 = part2(data, answers)
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
        data = f.read()
    data = data.split("\n\n")
    return data

def find_mirror(grid, past_answer):
    grid_height = len(grid)
    grid_width = len(grid[0])

    for y in range(1, grid_height):
        offset = 1
        mirror = True
        while y+offset-1<=grid_height-1 and y-offset>=0:
            if grid[y+offset-1] == grid[y-offset]:
                offset += 1
            else:
                mirror = False
                break
        if mirror and 100*y != past_answer:
            return 100*y
    
    for x in range(1, grid_width):
        mirror = True
        for row in grid:
            offset = 1
            while x+offset-1<=grid_width-1 and x-offset>=0:
                if row[x+offset-1] == row[x-offset]:
                    offset += 1
                else:
                    mirror = False
                    break
            if not mirror:
                break
        if mirror and x != past_answer:
            return x
        
    # if no mirror found, return a score of 0    
    return 0


def part1(data):
    score = 0
    answers = []
    for entry in data:
        grid = [list(line) for line in entry.split("\n")]
        new_score = find_mirror(grid, 0)
        answers.append(new_score)
        score += new_score
    return score, answers

def part2(data, answers):
    score = 0
    for q, entry in enumerate(data):
        grid = [list(line) for line in entry.split("\n")]
        grid_height = len(grid)
        grid_width = len(grid[0])
        for y in range(grid_height):
            for x in range(grid_width):
                new_grid = deepcopy(grid)

                if new_grid[y][x] == ".":
                    new_grid[y][x] = "#"
                else:
                    new_grid[y][x] = "."
                    
                new_score = find_mirror(new_grid, answers[q])

                if new_score != 0:
                    break
            if new_score != 0:
                break
        
        score += new_score
        

    return score



if __name__ == "__main__":
    main()