#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import heapq

RESET = "\033[0m"       # Resets all styles
RED = "\033[31m"        # Red text
GREEN = "\033[32m"      # Green text
YELLOW = "\033[33m"     # Yellow text
BLUE = "\033[34m"       # Blue text

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
    print(f"Data Parse Execution Time: {1000*(parse_time - start):.2f} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time):.2f} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time):.2f} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start):.2f} ms")
    print("---------------------------------------------------")


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()
    data = [list(line.strip()) for line in data]
    return data

def find_best_path(data, start, end):
    stack = []
    heapq.heappush(stack, (0, start, set(start), (0, 1), 1)) # start position, score, path, current_direction, tiles going straight
    heapq.heappush(stack, (0, start, set(start), (1, 0), 1))
    visited = {}
    results = []
    best_score = float("inf")

    while stack:
        score, position, path, current_direction, straight = heapq.heappop(stack)
        
        state_key = (position, current_direction, straight)
        if state_key in visited and visited[state_key] <= score:
            continue
        visited[state_key] = score

        if position == end:
            if score < best_score:
                best_score = score 
                results = (score, path)
            continue

        for next_direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
            new_position = (position[0] + next_direction[0], position[1] + next_direction[1])

            if 0 <= new_position[0] < len(data) and 0 <= new_position[1] < len(data[0]):
                if new_position in path:
                    continue

                new_score = score + int(data[new_position[0]][new_position[1]]) 

                if next_direction == current_direction:
                    if straight < 3:
                        heapq.heappush(stack, (new_score, new_position, path | {new_position}, next_direction, straight+1))
                else:
                    heapq.heappush(stack, (new_score, new_position, path | {new_position}, next_direction, 1))
    return results
                    

def find_best_path_part2(data, start, end):
    stack = []
    heapq.heappush(stack, (0, start, set(start), (0, 1), 1)) # start position, score, path, current_direction, tiles going straight
    heapq.heappush(stack, (0, start, set(start), (1, 0), 1))
    visited = {}
    results = []
    best_score = float("inf")

    while stack:
        score, position, path, current_direction, straight = heapq.heappop(stack)
        
        state_key = (position, current_direction, straight)
        if state_key in visited and visited[state_key] <= score:
            continue
        visited[state_key] = score

        if position == end and straight >=4:
            if score < best_score:
                best_score = score 
                results = (score, path)
            continue

        for next_direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
            new_position = (position[0] + next_direction[0], position[1] + next_direction[1])

            if 0 <= new_position[0] < len(data) and 0 <= new_position[1] < len(data[0]):
                if new_position in path:
                    continue

                new_score = score + int(data[new_position[0]][new_position[1]]) 

                if next_direction == current_direction:
                    if straight < 10:
                        heapq.heappush(stack, (new_score, new_position, path | {new_position}, next_direction, straight+1))
                else:
                    if straight >= 4:
                        heapq.heappush(stack, (new_score, new_position, path | {new_position}, next_direction, 1))
    return results


def print_path(data, results):
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (y,x) in results[1]:
                print(f"{RED}{data[y][x]}{RESET}", end="")
            else:
                print(data[y][x], end="")
        print()
    print()


def part1(data):
    start = (0,0)
    end = (len(data)-1, len(data[0])-1)
    heat_loss = find_best_path(data, start, end)
    print_path(data, heat_loss)
    return heat_loss[0]


def part2(data):
    start = (0,0)
    end = (len(data)-1, len(data[0])-1)
    heat_loss = find_best_path_part2(data, start, end)
    print_path(data, heat_loss)
    return heat_loss[0]


if __name__ == "__main__":
    main()