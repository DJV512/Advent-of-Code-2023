#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

# ChatGPT code. Works well for part 1 and part 2 sample input. But takes way way too long for real input on part 2.

import time
from functools import lru_cache

def main():
    start = time.time()

    springs, broken = parse_data()
    parse_time = time.time()

    answer1 = part1(springs, broken)
    part1_time = time.time()
    answer2 = part2(springs, broken)
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
    
    springs = []
    broken = []
    for row in data:
        spring_list, broken_list = row.strip().split(" ")
        spring_list = [*spring_list]
        broken_list = broken_list.split(",")
        springs.append(spring_list)
        broken_ints = []
        for broke in broken_list.copy():
            broken_ints.append(int(broke))
        broken.append(broken_ints)
    
    return springs, broken

@lru_cache(maxsize=None)
def count_ways(sequence, numbers, index=0, pos=0):
    # Base case: If we have satisfied all groups of numbers
    if index == len(numbers):
        # Ensure all remaining characters are "." (if any)
        return all(c != '#' for c in sequence[pos:])
    
    # If we run out of space in the sequence
    if pos >= len(sequence):
        return 0
    
    # Count the total ways for this configuration
    total_ways = 0
    
    # Try placing the required number of '#' at the current position
    group_size = numbers[index]
    if pos + group_size <= len(sequence):  # Ensure there's enough space for this group
        # Check if the placement of '#' is valid
        if all(sequence[i] in ('?', '#') for i in range(pos, pos + group_size)):
            # Create a new sequence with '#' placed
            new_sequence = list(sequence)
            for i in range(pos, pos + group_size):
                new_sequence[i] = '#'
            
            # Ensure there's at least one '.' after this group (if not the last group)
            next_pos = pos + group_size
            if index + 1 < len(numbers):  # Not the last group, so we need at least one '.'
                if next_pos < len(sequence) and sequence[next_pos] in ('?', '.'):
                    new_sequence[next_pos] = '.'
                    total_ways += count_ways(tuple(new_sequence), tuple(numbers), index + 1, next_pos + 1)
            else:  # Last group, no need for a trailing '.'
                total_ways += count_ways(tuple(new_sequence), tuple(numbers), index + 1, next_pos)

    # Skip the current position if it's a '.'
    if sequence[pos] in ('?', '.'):
        total_ways += count_ways(tuple(sequence), tuple(numbers), index, pos + 1)
    
    return total_ways

# Helper function to simplify the interface
def part1(springs, broken):
    end_total = 0
    for q, spring in enumerate(springs):
        end_total += count_ways(tuple(list(spring)), tuple(broken[q]))

    return end_total

def part2(springs, broken):
    unfolded_springs = []
    for spring in springs:
        new_spring = spring+["?"]+spring+["?"]+spring+["?"]+spring+["?"]+spring
        unfolded_springs.append(new_spring)

    unfolded_broken = []
    for broke in broken:
        new_broken = 5*broke
        unfolded_broken.append(new_broken)
    
    end_total = 0
    for q, spring in enumerate(unfolded_springs):
        end_total += count_ways(tuple(list(spring)), tuple(unfolded_broken[q]))
        # print(f"{end_total=}")

    return end_total


if __name__ == "__main__":
    main()