#FILENAME = "sample2.txt"
#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
from collections import deque
from collections import defaultdict
from copy import deepcopy

RESET = "\033[0m"         # Resets all styles
BLACK = "\033[30;1m"      # Black text
RED = "\033[31;1m"        # Red text
GREEN = "\033[32;1m"      # Green text
YELLOW = "\033[33;1m"     # Yellow text
BLUE = "\033[34;1m"       # Blue text
MAGENTGA = "\033[35;1m"   # Magenta text
CYAN = "\033[36;1m"       # Cyan text
WHITE = "\033[37;1m"      # White text

BOLD = "\033[1m"          # Bold text
UNDERLINE = "\033[4m"     # Underlined text

def main():
    start = time.time()

    data, all_status = parse_data()
    data2 = deepcopy(data)
    all_status2 = deepcopy(all_status)

    parse_time = time.time()

    answer1 = part1(data, all_status)
    part1_time = time.time()
    answer2 = part2(data2, all_status2)
    part2_time = time.time()

    print("---------------------------------------------------")
    print(f"Part 1 Answer: {answer1}")
    print()
    print(f"Part 2 Answer: {answer2}")
    print()
    print(f"Data Parse Execution Time: {1000*(parse_time - start)} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time)} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time)} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start)} ms")
    print("---------------------------------------------------")
    


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.read()

    data = data.split("\n")
    module_dict = {}
    all_status = {}
    input_dict = defaultdict(list)

    for line in data:
        module, target = line.split(" -> ")
        targets = target.split(", ")

        if "broadcaster" in module:
            module_dict["broadcaster"] =  ("broadcaster", targets)
            all_status["broadcaster"] = 0
            continue

        module_type = module[0]
        module_name = module[1:]
        module_dict[module_name] = (module_type, targets)

        for target in targets:
            input_dict[target].append(module_name)

        if module_type == "%":
            all_status[module_name] = 0
        elif module_type == "&":
            all_status[module_name] = {}

    for key in module_dict:
        if module_dict[key][0] == "&":
            for input in input_dict[key]:
                all_status[key][input] = 0
    return module_dict, all_status


def part1(data, all_status):
    highs = 0
    lows = 0
    for i in range(1000):
        lows += 1
        stack = deque()
        stack.append(("button", 0, "broadcaster"))
        while stack:
            prev_module, input, module_name, = stack.popleft()
            # print(prev_module, input, module_name)
            # print(all_status)
            try:
                type, targets = data[module_name]
            except KeyError:
                continue
            else:
                if type == "&":
                    all_status[module_name][prev_module] = input
                    flag = False
                    for key in all_status[module_name]:
                        if all_status[module_name][key] == 0:
                            output = 1
                            flag = True
                            continue
                    if not flag:
                        output = 0
                    for target in targets:
                        if output == 0:
                            lows += 1
                        else:
                            highs += 1
                        stack.append((module_name, output, target))
                elif type == "%":
                    if input == 0:
                        if all_status[module_name] == 0:
                            all_status[module_name] = 1
                            output = 1
                        else:
                            all_status[module_name] = 0
                            output = 0
                        for target in targets:
                            if output == 0:
                                lows += 1
                            else:
                                highs += 1
                            stack.append((module_name, output, target))
                elif type == "broadcaster":
                    for target in targets:
                        lows += 1
                        stack.append((module_name, 0, target))
        # print(f"After button push {i+1}, lows = {lows}, highs = {highs}")
        # print()
        
    # breakpoint()
    return highs*lows


def part2(data, all_status):
    for i in range(10000000):
        stack = deque()
        stack.append(("button", 0, "broadcaster"))
        while stack:
            prev_module, input, module_name, = stack.popleft()
            if prev_module in ["ks", "pm", "dl", "vk"]:
                if input == 1:
                    print(f"At button press {i+1}, {prev_module} sent {input} to {module_name}.")
            try:
                type, targets = data[module_name]
            except KeyError:
                continue
            else:
                if type == "&":
                    all_status[module_name][prev_module] = input
                    flag = False
                    for key in all_status[module_name]:
                        if all_status[module_name][key] == 0:
                            output = 1
                            flag = True
                            continue
                    if not flag:
                        output = 0
                    for target in targets:
                        stack.append((module_name, output, target))
                elif type == "%":
                    if input == 0:
                        if all_status[module_name] == 0:
                            all_status[module_name] = 1
                            output = 1
                        else:
                            all_status[module_name] = 0
                            output = 0
                        for target in targets:
                            stack.append((module_name, output, target))
                elif type == "broadcaster":
                    for target in targets:
                        stack.append((module_name, 0, target))
    return all_status


if __name__ == "__main__":
    main()