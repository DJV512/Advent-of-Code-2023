FILENAME = "input.txt"

with open(FILENAME) as f:
    data = f.readlines()

total_points=0
for row in data:
    card, numbers = row.split(":")
    winning, mine = numbers.split("|")
    winning_nums = winning.split(" ")
    my_nums = mine.split(" ")

    for i, num in enumerate(winning_nums.copy()):
        if num == "":
            winning_nums.remove(num)

    for i, num in enumerate(my_nums.copy()):
        if num == "":
            my_nums.remove(num)

    points = 0
    for num in my_nums:
        if num.strip() in winning_nums:
            print(f"WINNER! - Number {num} on {card}")
            if points == 0:
                points = 1
            else:
                points *= 2
    total_points += points
    print(f"Points on {card} = {points}.")
    print(f"Total points so far = {total_points}.")
    print()
    
print(total_points)



    