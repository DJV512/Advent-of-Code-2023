# FILENAME = "input.txt"
FILENAME = "sample_input.txt"

def main():

    springs, broken = parse_data()

    answer1 = part1(springs, broken)
    answer2 = part2(springs)

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

    springs = []
    broken = []
    for row in data:
        spring_list, broken_list = row.strip().split(" ")
        spring_list = [*spring_list]
        broken_list = broken_list.split(",")
        springs.append(spring_list)
        broken.append(broken_list)
    
    return springs, broken


def part1(springs, broken):
    data_len = len(springs)
    total = 0
    for i in range(data_len):
        current_springs = springs[i]
        current_broken = broken[i]
        print(f"Current springs input: {current_springs}")
        print(f"Current broken input: {current_broken}")


        q_marks = []
        working = []
        def_broken = []
        for j, char in enumerate(current_springs):
            if char == "?":
                q_marks.append(j)
            elif char == ".":
                working.append(j)
            elif char == "#":
                def_broken.append(j)
        
        print(f"Q-Marks: {q_marks}")
        print()
        all_possible = []
        num_q = len(q_marks)
        for k in range(num_q):
            temp_springs = current_springs.copy()
            # print(f"For each k, temp_springs starts at: {temp_springs}")
            # print(f"Current springs is now: {current_springs}")
            temp_springs[q_marks[k]] = "."
            for m in range(num_q):
                if q_marks[k] != q_marks[m]:
                    temp_springs[q_marks[m]] = "."
                    all_possible.append(temp_springs)
                    temp_springs = current_springs.copy()
            for m in range(num_q):
                if q_marks[k] != q_marks[m]:
                    temp_springs[q_marks[m]] = "#"
                    all_possible.append(temp_springs)
                    temp_springs = current_springs.copy()

            
                


def part2(data):

    return None


if __name__ == "__main__":
    main()