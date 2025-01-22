FILENAME = "input.txt"

written = {"one":"1",
           "two":"2",
           "three":"3",
           "four":"4",
           "five":"5",
           "six":"6",
           "seven":"7",
           "eight":"8",
           "nine":"9",
            }

with open(FILENAME, "r") as f:
    data = f.readlines()

total_sum = 0
numbers = []
in_row = []
for row in data:
    for word in written:
        if word in row:
            in_row.append(word)
    for i, char in enumerate(row):
        if char.isdigit():
            numbers.append(char)
        for word in in_row:
            if word == row[i:i+len(word)]:
                numbers.append(written[word])
    new_num = int(numbers[0]+numbers[-1])
    total_sum += new_num
    numbers = []
    in_row = []
print(total_sum)