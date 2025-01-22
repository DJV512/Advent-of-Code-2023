FILENAME = "input.txt"
# FILENAME = "sample_input.txt"

def main():

    data, galaxy_locations, expanded_rows, expanded_cols = parse_data()

    answer1 = part1(galaxy_locations)
    answer2 = part2(data, expanded_rows, expanded_cols)

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
    
    galaxy = []
    total_expands = 0
    expanded_rows = []
    for i, row in enumerate(data):
        expand = True
        for column in row:
            if column == "#":
                expand = False
                break
        if expand:
            expanded_rows.append(i)
            galaxy.append(row.strip())
            galaxy.append(row.strip())
            total_expands += 1
        else:
            galaxy.append(row.strip())
    
    total_rows = len(galaxy)
    total_cols = len(galaxy[0])

    galaxy2 = [[0 for _ in range(total_cols)] for _ in range(total_rows)]
    total_expands = 0
    expanded_cols = []
    for i in range(total_cols):
        expand = True
        for j in range(total_rows):
            if galaxy[j][i] == "#":
                expand = False
            galaxy2[j][i+ total_expands] = galaxy[j][i]
        if expand:
            total_expands += 1
            expanded_cols.append(i)
            for q,row in enumerate(galaxy):
                galaxy2[q][i+total_expands] = "."
                galaxy2[q].append(0)
    
    total_rows = len(galaxy2)
    total_cols = len(galaxy2[0])

    galaxy_locations = []

    for i in range(total_rows):
        for j in range(total_cols):
            if galaxy2[i][j] == "#":
                galaxy_locations.append((i,j))
    
    with open("new_data.txt", "w") as f:
        for row in galaxy2:
            for column in row:
                f.writelines(column)
            f.writelines("\n")

    return data, galaxy_locations, expanded_rows, expanded_cols


def part1(data):
    num_galaxies = len(data)
    total_distance = 0
    for i in range(num_galaxies-1):
        for j in range(i+1, num_galaxies):
            first_gal = data[i]
            second_gal = data[j]
            distance = abs(first_gal[0]-second_gal[0]) + abs(first_gal[1]-second_gal[1])
            total_distance += distance
    return total_distance


def part2(data, expanded_rows, expanded_cols):
    galaxy_locations = []
    for i in range(len(data)):
        for j in range(len(data[0].strip())):
            if data[i][j] == "#":
                galaxy_locations.append((i,j))
    num_galaxies = len(galaxy_locations)
    total_distance = 0
    for i in range(num_galaxies-1):
        for j in range(i+1, num_galaxies):
            first_gal = galaxy_locations[i]
            second_gal = galaxy_locations[j]
            distance = abs(first_gal[0]-second_gal[0]) + abs(first_gal[1]-second_gal[1])
            for n in range(first_gal[0], second_gal[0]):
                if n in expanded_rows:
                    distance += 999999
            for n in range(min(first_gal[1], second_gal[1]), max(first_gal[1], second_gal[1])):
                if n in expanded_cols:
                    distance += 999999
            total_distance += distance
    return total_distance


if __name__ == "__main__":
    main()