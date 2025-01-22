FILENAME = "input.txt"

def main():
    data = parse_data()

    answer1, half_pos, path_only, starting_pos = part1(data)
    with open("path_only.txt", "w") as f:
        for row in path_only:
            for column in row:
                f.writelines(column)
            f.writelines("\n")
    answer2 = part2(path_only, starting_pos)

    print()
    print("--------Part 1 Answer-------------")
    print(f"The middle position of the loop is at {half_pos}, which is {answer1} steps from the start.")
    print()
    print("--------Part 2 Answer-------------")
    print(f"Exactly {answer2} cells are within the loop.")
    print()


def parse_data():
    with open(FILENAME) as f:
        data = f.readlines()
    map = [row.strip() for row in data]
    return map


def part1(data):
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == "S":
                starting_pos = (i,j)
    path = 0
    ending_symbol = ""
    previous_pos = starting_pos    
    i = starting_pos[0]
    j = starting_pos[1]
    path_only = [["." for _ in range(140)] for _ in range(140)]
    path_only[i][j] = "S"
    while ending_symbol != "S":
        if data[i][j] in ["J", "|", "L", "S"] and data[i-1][j] in ["|", "F", "7"] and previous_pos != (i-1, j):
            path += 1
            previous_pos = (i,j)
            i -= 1
            ending_symbol = data[i][j]
            path_only[i][j] = data[i][j]
        elif data[i][j] in ["-", "J", "7", "S"] and data[i][j-1] in ["-", "F", "L"] and previous_pos != (i, j-1):
            path += 1
            previous_pos = (i,j)
            j -= 1
            ending_symbol = data[i][j-1]
            path_only[i][j] = data[i][j]
        elif data[i][j] in ["-", "F", "L", "S"] and data[i][j+1] in ["-", "7", "J"] and previous_pos != (i, j+1):
            path += 1
            previous_pos = (i,j)
            j += 1
            ending_symbol = data[i][j+1]
            path_only[i][j] = data[i][j]
        elif data[i][j] in ["|", "F", "7", "S"] and data[i+1][j] in ["|", "J", "L"] and previous_pos != (i+1, j):
            path += 1
            previous_pos = (i,j)
            i += 1
            ending_symbol = data[i+1][j]
            path_only[i][j] = data[i][j]
        if path == 7030:
            half_pos = (i,j)
    
    half_path = int(path/2 + 0.5)
    return half_path, half_pos, path_only, starting_pos
    


def part2(data, starting_pos):
    data[starting_pos[0]][starting_pos[1]] = "J"
    count = 0
    for row in data:
        last_bend = "."
        is_inside = False
        for column in row:
            if column == "J":
                if last_bend == "L":
                    if is_inside:
                        is_inside = False
                    else:
                        is_inside = True
                last_bend = "J"
            elif column == "7":
                if last_bend == "F":
                    if is_inside:
                        is_inside = False
                    else:
                        is_inside = True
                last_bend = "7"
            elif column in ["F", "L", "|"]:
                if is_inside:
                    is_inside = False
                else:
                    is_inside = True
                if column == "F":
                    last_bend = "F"
                elif column == "L":
                    last_bend = "L"
                elif column == "|":
                    last_bend = "|"
            if is_inside and column == ".":
                count += 1
    return count


if __name__ == "__main__":
    main()