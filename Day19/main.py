#FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import re

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

    all_rules, part_dict = parse_data()
    parse_time = time.time()

    answer1 = part1(all_rules, part_dict)
    part1_time = time.time()
    answer2 = part2(all_rules)
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
    workflow, part = data.split("\n\n")
    workflows = workflow.split("\n")
    parts = part.split("\n")

    all_rules = {}
    for workflow in workflows:
        name, rules = workflow.split("{")
        rule_list = rules[:-1].split(",")
        final_rulelist = []
        for rule in rule_list:
            match = re.match(r"(\w+)(>|<)(-?\d+):(\w*)", rule)
            if match:
                var, op, value, go_to = match.groups()
                final_rulelist.append((var, op, int(value), go_to))
            else:
                last_string = rule.strip()
                final_rulelist.append(last_string)
        all_rules[name] = final_rulelist

    part_dict = {}
    for i, part in enumerate(parts):
        part = part[1:-1]
        match = re.match(r"(x)(=)(\d+),(m)(=)(\d+),(a)(=)(\d+),(s)(=)(\d+)", part)
        _, _, x_val, _, _, m_val, _, _, a_val, _, _, s_val = match.groups()
        part_dict[i] = {
                "x": int(x_val),
                "m": int(m_val),
                "a": int(a_val),
                "s": int(s_val)
            }

    return all_rules, part_dict
    

def where_to(part_specs, all_rules, rule, level):
    if isinstance(all_rules[rule][level], tuple):
        var, op, value, go_to = all_rules[rule][level]
        if var == "x":
            if op == ">":
                if part_specs[0] > value:
                    return (go_to, 0)
                else:
                    return (rule, level+1)
            else:
                if part_specs[0] < value:
                    return (go_to, 0)
                else:
                    return (rule, level+1)
        
        elif var == "m":
            if op == ">":
                if part_specs[1] > value:
                    return (go_to, 0)
                else:
                    return (rule, level+1)
            else:
                if part_specs[1] < value:
                    return (go_to, 0)
                else:
                    return (rule, level+1)
        
        elif var == "a":
            if op == ">":
                if part_specs[2] > value:
                    return (go_to, 0)
                else:
                    return (rule, level+1)
            else:
                if part_specs[2] < value:
                    return (go_to, 0)
                else:
                    return (rule, level+1)

        elif var == "s":
            if op == ">":
                if part_specs[3] > value:
                    return (go_to, 0)
                else:
                    return (rule, level+1)
            else:
                if part_specs[3] < value:
                    return (go_to, 0)
                else:
                    return (rule, level+1)
    else:
        return (all_rules[rule][level], 0)

def part1(all_rules, part_dict):

    accepted_parts = []
    for part in part_dict:
        x = part_dict[part]["x"]
        m = part_dict[part]["m"]
        a = part_dict[part]["a"]
        s = part_dict[part]["s"]
        part_specs = (x, m, a, s)
        level = 0
        rule = "in"
        keep_going = True

        while keep_going:
            rule, level = where_to(part_specs, all_rules, rule, level)
            if rule == "A":
                accepted_parts.append((x + m + a + s))
                keep_going = False
            if rule == "R":
                keep_going = False

    total = sum(accepted_parts)

    return total


def part2(all_rules):
    start = ("in", 0, (1,4000), (1,4000), (1,4000), (1,4000))
    stack = []
    stack.append(start)
    
    total = 0
    while stack:
        rule, level, range_x, range_m, range_a, range_s = stack.pop()
        
        if rule == "R":
            continue
        elif rule == "A":
            new_accepted = (range_x[1]-range_x[0]+1)*(range_m[1]-range_m[0]+1)*(range_a[1]-range_a[0]+1)*(range_s[1]-range_s[0]+1)
            total += new_accepted
            continue

        current_rule = all_rules[rule][level]

        if isinstance(current_rule, str):
            if current_rule == "R":
                continue
            elif current_rule == "A":
                new_accepted = (range_x[1]-range_x[0]+1)*(range_m[1]-range_m[0]+1)*(range_a[1]-range_a[0]+1)*(range_s[1]-range_s[0]+1)
                total += new_accepted
                continue
            else:
                stack.append((current_rule, 0, range_x, range_m, range_a, range_s))
                continue

        if current_rule[1] == "<":
            if eval(f"range_{current_rule[0]}[0]") < current_rule[2]-1 < eval(f"range_{current_rule[0]}[1]"):
                new_range_low = (eval(f"range_{current_rule[0]}[0]"), current_rule[2]-1)
                new_range_high = (current_rule[2], eval(f"range_{current_rule[0]}[1]"))
                if current_rule[0] == "x":
                    stack.append((current_rule[3], 0, new_range_low, range_m, range_a, range_s))
                    stack.append((rule, level+1, new_range_high, range_m, range_a, range_s))
                elif current_rule[0] == "m":
                    stack.append((current_rule[3], 0, range_x, new_range_low, range_a, range_s))
                    stack.append((rule, level+1, range_x, new_range_high, range_a, range_s))
                elif current_rule[0] == "a":
                    stack.append((current_rule[3], 0, range_x, range_m, new_range_low, range_s))
                    stack.append((rule, level+1, range_x, range_m, new_range_high, range_s))
                elif current_rule[0] == "s":
                    stack.append((current_rule[3], 0, range_x, range_m, range_a, new_range_low))
                    stack.append((rule, level+1, range_x, range_m, range_a, new_range_high))
            elif current_rule[2]-1 < eval(f"range_{current_rule[0]}[0]"):
                continue
            else: 
                stack.append((current_rule[3], 0, range_x, range_m, range_a, range_s))
        elif current_rule[1] == ">":
            if eval(f"range_{current_rule[0]}[0]") < current_rule[2] < eval(f"range_{current_rule[0]}[1]"):
                new_range_low = (eval(f"range_{current_rule[0]}[0]"), current_rule[2])
                new_range_high = (current_rule[2]+1, eval(f"range_{current_rule[0]}[1]"))
                if current_rule[0] == "x":
                    stack.append((rule, level+1, new_range_low, range_m, range_a, range_s))
                    stack.append((current_rule[3], 0, new_range_high, range_m, range_a, range_s))
                elif current_rule[0] == "m":
                    stack.append((rule, level+1, range_x, new_range_low, range_a, range_s))
                    stack.append((current_rule[3], 0, range_x, new_range_high, range_a, range_s))
                elif current_rule[0] == "a":
                    stack.append((rule, level+1, range_x, range_m, new_range_low, range_s))
                    stack.append((current_rule[3], 0, range_x, range_m, new_range_high, range_s))
                elif current_rule[0] == "s":
                    stack.append((rule, level+1, range_x, range_m, range_a, new_range_low))
                    stack.append((current_rule[3], 0, range_x, range_m, range_a, new_range_high))
            elif current_rule[2] < eval(f"range_{current_rule[0]}[0]"):
                stack.append((current_rule[3], 0, range_x, range_m, range_a, range_s))
            else:
                continue
    
    return total


if __name__ == "__main__":
    main()