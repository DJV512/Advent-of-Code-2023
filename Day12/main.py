FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
from collections import deque
from itertools import permutations

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

def determine_sequence(springs, query):
    output = []
    start_char = springs[0]
    total = 1
    for z, char in enumerate(springs[1:]):
        if char == start_char:
            total += 1
        else:
            output.append((start_char,total))
            start_char = springs[z+1]
            total = 1
    output.append((start_char, total))

    final_output = []
    for char, number in output:
        if char == query:
            final_output.append(number)

    return final_output





def part1(springs, broken):
    total = 0
    for i, spring in enumerate(springs):
        print(f"Current springs input: {spring}")
        print(f"Current broken input: {broken[i]}")

        q_marks = []
        for z, position in enumerate(spring):
            if position == "?":
                q_marks.append(z)
        number_of_q = len(q_marks)
        print(f"Number of ?, {number_of_q} total")

        number_of_starting_brokens = sum(determine_sequence(spring, "#"))
        print(f"Number of confirmed broken springs: {number_of_starting_brokens}")

        number_of_broken_needed = sum(broken[i])
        print(f"Number of needed #: {number_of_broken_needed}")

        number_of_broken_to_add = number_of_broken_needed - number_of_starting_brokens
        print(f"Need to add {number_of_broken_to_add} #s")
    
        possibles = ["#" for _ in range(number_of_broken_to_add)] + ["." for _ in range(number_of_q-number_of_broken_to_add)]
        print(possibles)
        combos = permutations(possibles, number_of_q)
        unique_combos = set()
        for combo in combos:
            unique_combos.add(combo)


        print()



    return total


def part2(springs, broken):
    return None


if __name__ == "__main__":
    main()