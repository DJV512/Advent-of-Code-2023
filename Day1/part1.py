FILENAME = "input.txt"

with open(FILENAME, "r") as f:
    data = f.readlines()

total_sum = 0
numbers = []
for row in data:
    for char in row:
        if char.isdigit():
            numbers.append(char)
    total_sum += int(numbers[0]+numbers[-1])
    numbers = []
print(total_sum)