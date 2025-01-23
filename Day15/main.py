#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
from collections import defaultdict

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
        data = f.read()
        data = data.split(",")
    return data

def hash(string):
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value = current_value  % 256
    return current_value
        

def part1(data):
    total = 0
    for string in data:
        total += hash(string)
    return total


def part2(data):
    boxes = defaultdict(list)
    for string in data:
        if "=" in string:
            label, focal = string.split("=")
            box = hash(label)
            if not any(label in value for value in boxes[box]):
                boxes[box].append(f"{label} {focal}")
            else:
                for i, value in enumerate(boxes[box].copy()):
                    if label in value:
                        boxes[box][i] = f"{label} {focal}"
        else:
            label = string[:-1]
            box = hash(label)
            for value in boxes[box].copy():
                    if label in value:
                        boxes[box].remove(value)

    for box in boxes:
        print(f"{box}: {boxes[box]}")

    total = 0
    for key in boxes:
        for i, value in enumerate(boxes[key]):
            total += ((key+1)*(i+1)*(int(value[-1])))


    return total


if __name__ == "__main__":
    main()