TIME = [34, 90, 89, 86, 34908986]
DIST = [204, 1713, 1210, 1780, 204171312101780]

def main():

    answer1 = part1()
    answer2 = part2()

    print("<----------Part 1 Answer---------->")
    print(answer1)
    print()
    print("<----------Part 2 Answer---------->")
    print(answer2)

def ways_to_win(race):
    race_time = TIME[race]
    best_dist = DIST[race]
    ways = 0
    for i in range(1, race_time):
        move_time = race_time - i
        move_dist = move_time * i
        if move_dist > best_dist:
            print(f"Race {race} can be won by holding the button for {i} ms, which results in a distance of {move_dist} mm.")
            ways += 1
    print(f"Race {race} can be won in {ways} ways.")
    print()
    return ways

def part1():
    product = 1
    for j in range(4):
        race_ways = ways_to_win(j)
        product *= race_ways
    return product


def part2():
    return ways_to_win(4)


if __name__ == "__main__":
    main()