COUNT_RED = 12
COUNT_GREEN = 13
COUNT_BLUE = 14

COLOR_RED = "red"
COLOR_GREEN = "green"
COLOR_BLUE = "blue"

FILENAME = "input.txt"

with open(FILENAME, "r") as f:
    data = f.readlines()

total_count = 0
for row in data:
    works = True
    game_no, games = row.split(": ")
    number = game_no.split(" ")[1]
    print("Game", number)
    indv_games = games.split("; ")
    for game in indv_games:
        one_game = game.split(", ")
        for draw in one_game:
            count, color = draw.split(" ")
            color = color.rstrip().lstrip()
            if color == COLOR_RED:
                if int(count) > COUNT_RED:
                    works = False
                    print(f"{color} = {count} - TOO MANY!!")
            if color == COLOR_GREEN:
                if int(count) > COUNT_GREEN:
                    works = False
                    print(f"{color} = {count} - TOO MANY!!")
            if color == COLOR_BLUE:
                if int(count) > COUNT_BLUE:
                    works = False
                    print(f"{color} = {count} - TOO MANY!!")
                    
    if works:
        print("WORKED!")
        total_count += int(number)
    else:
        print("DIDN'T WORK!")
    print(f"Total Count = {total_count}")
            
    print()
    print()

print(total_count)