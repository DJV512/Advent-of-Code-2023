FILENAME = "input.txt"

def main():

    data = parse_data()

    answer1 = part1(data)
    answer2 = part2(data)

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
    return [row.strip().split(" ") for row in data]


def part1(data):
    sum_list = []
    for row in data:
        all_diffs = []
        all_diffs.append(row)
        diff = [int(row[n])-int(row[n-1]) for n in range(1, len(row))]
        all_diffs.append(diff)
        while len(set(diff)) != 1: 
            diff = [int(diff[j])-int(diff[j-1]) for j in range(1, len(diff))]
            all_diffs.append(diff)
        new_value = int(all_diffs[-1][-1]) + int(all_diffs[-2][-1])
        if len(all_diffs) > 2:
            for q in range(-3, -len(all_diffs)-1, -1):
                new_value = int(all_diffs[q][-1]) + new_value

        sum_list.append(new_value)
    
    return sum(sum_list)


def part2(data):
    sum_list = []
    for row in data:
        print(row)
        all_diffs = []
        all_diffs.append(row)
        diff = [int(row[n])-int(row[n-1]) for n in range(1, len(row))]
        print(diff)
        all_diffs.append(diff)
        while len(set(diff)) != 1: 
            diff = [int(diff[j])-int(diff[j-1]) for j in range(1, len(diff))]
            print(diff)
            all_diffs.append(diff)
        new_value = int(all_diffs[-2][0]) - int(all_diffs[-1][0])
        print(new_value)
        if len(all_diffs) > 2:
            for q in range(-3, -len(all_diffs)-1, -1):
                new_value = int(all_diffs[q][0])-new_value
                print(new_value)

        sum_list.append(new_value)
    
    return sum(sum_list)


if __name__ == "__main__":
    main()
    