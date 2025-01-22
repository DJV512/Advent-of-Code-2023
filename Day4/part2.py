FILENAME = "input.txt"

with open(FILENAME) as f:
    data = f.readlines()

card_count = {}
for i in range(1,206):
    card_count[i] = 1

for row in data:
    card, numbers = row.split(":")
    card_number = card.split(" ")
    winning, mine = numbers.split("|")
    winning_nums = winning.split(" ")
    my_nums = mine.split(" ")

    for i, num in enumerate(winning_nums.copy()):
        if num == "":
            winning_nums.remove(num)

    for i, num in enumerate(my_nums.copy()):
        if num == "":
            my_nums.remove(num)

    matches = 0
    for num in my_nums:
        if num.strip() in winning_nums:
            matches += 1

    for i in range(1,matches+1):
        card_count[int(card_number[-1])+i] += card_count[int(card_number[-1])]

total_cards = 0
for key in card_count:
    total_cards += card_count[key]

print(total_cards)

    




    