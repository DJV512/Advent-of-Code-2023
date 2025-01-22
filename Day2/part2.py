COLOR_RED = "red"
COLOR_GREEN = "green"
COLOR_BLUE = "blue"

FILENAME = "input.txt"

with open(FILENAME, "r") as f:
    data = f.readlines()

total_count = 0
for row in data:
    max_red = 0
    max_green = 0
    max_blue = 0
    product = 0
    game_no, games = row.split(": ")
    number = game_no.split(" ")[1]
    indv_games = games.split("; ")
    for game in indv_games:
        one_game = game.split(", ")
        for draw in one_game:
            count, color = draw.split(" ")
            color = color.rstrip().lstrip()
            if color == COLOR_RED:
                if int(count) > max_red:
                    max_red = int(count)
            if color == COLOR_GREEN:
                if int(count) > max_green:
                    max_green = int(count)
            if color == COLOR_BLUE:
                if int(count) > max_blue:
                    max_blue = int(count)
    product = max_red * max_green * max_blue
    total_count += product       

print(total_count)