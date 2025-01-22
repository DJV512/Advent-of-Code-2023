from math import lcm

FILENAME = "input.txt"

def main():

    directions, nodes = parse_data()

    answer1 = part1(directions, nodes)
    answer2 = part2(directions, nodes)

    print()
    print("--------Part 1 Answer-------------")
    print(answer1)
    print()
    print("--------Part 2 Answer-------------")
    print(answer2)
    print()


def parse_data():
    with open(FILENAME) as f:
        data = f.readlines()
    directions = data[0]
    nodes = {}
    for n in range(2, 756):
        location, options = data[n].strip().split(" = ")
        option1, option2 = options.replace("(", "").replace(")","").split(", ")
        nodes[location] = option1, option2
    return directions, nodes


def part1(directions, nodes):
    steps = 0
    location = "AAA"
    while location != "ZZZ":
        for char in directions:
            if char == "R":
                next_location = nodes[location][1]
                steps += 1
            elif char == "L":
                next_location = nodes[location][0]
                steps += 1
            if next_location == "ZZZ":
                return steps
            else:
                location = next_location


def part2(directions, nodes):
    directions = directions.strip()
    
    starting_locations = []
    for key in nodes:
        if key[2] == "A":
            starting_locations.append(key)
    
    steps_per_cycle = []
    for location in starting_locations:
        steps = 0
        while location[2] != "Z":
            for char in directions:
                if char == "R":
                    next_location = nodes[location][1]
                    steps += 1
                elif char == "L":
                    next_location = nodes[location][0]
                    steps += 1
                if next_location[2] == "Z":
                    steps_per_cycle.append(steps)
                location = next_location

    return lcm(steps_per_cycle[0], steps_per_cycle[1], steps_per_cycle[2], steps_per_cycle[3], steps_per_cycle[4], steps_per_cycle[5])

   
if __name__ == "__main__":
    main()