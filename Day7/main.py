# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

CARD_VALUE1 = {
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "J":11,
    "Q":12,
    "K":13,
    "A":14,
}

CARD_VALUE2 = {
    "J":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "T":10,
    "Q":12,
    "K":13,
    "A":14,
}

def main():
    data = parse_data()

    answer1 = part1(data)
    answer2 = part2(data)

    print("--------Part 1 Answer-------------")
    print(answer1)
    print()
    print("--------Part 2 Answer-------------")
    print(answer2)


def parse_data():
    with open(FILENAME) as f:
        data = f.readlines()
    
    all_hands = {}
    for row in data:
        hand, bet = row.strip().split(" ")
        all_hands[hand] = bet
    
    return all_hands

def sort_hand_list(hands, part):
    if part == 1:
        CARD_VALUE = CARD_VALUE1
    else:
        CARD_VALUE = CARD_VALUE2
    sorted_hands = [hands[0]]
    for j in range(1, len(hands)):
        location = 0
        for i, sorted_hand in enumerate(sorted_hands.copy()):
            if CARD_VALUE[hands[j][0]] < CARD_VALUE[sorted_hand[0]]:
                sorted_hands.insert(i, hands[j])
                break
            elif CARD_VALUE[hands[j][0]] == CARD_VALUE[sorted_hand[0]]:
                if CARD_VALUE[hands[j][1]] < CARD_VALUE[sorted_hand[1]]:
                    sorted_hands.insert(i, hands[j])
                    break
                elif CARD_VALUE[hands[j][1]] == CARD_VALUE[sorted_hand[1]]:
                    if CARD_VALUE[hands[j][2]] < CARD_VALUE[sorted_hand[2]]:
                        sorted_hands.insert(i, hands[j])
                        break
                    elif CARD_VALUE[hands[j][2]] == CARD_VALUE[sorted_hand[2]]:
                        if CARD_VALUE[hands[j][3]] < CARD_VALUE[sorted_hand[3]]:
                            sorted_hands.insert(i, hands[j])
                            break
                        elif CARD_VALUE[hands[j][3]] == CARD_VALUE[sorted_hand[3]]:
                            if CARD_VALUE[hands[j][4]] < CARD_VALUE[sorted_hand[4]]:
                                sorted_hands.insert(i, hands[j])
                                break
                            else:
                                if hands[j][0:3] == sorted_hands[i+1][0:3] and CARD_VALUE[hands[j][4]] > CARD_VALUE[sorted_hands[i+1][4]]:
                                    try:
                                        sorted_hands.insert(i+2, hands[j])
                                        break
                                    except IndexError:
                                        sorted_hands.append(hands[j])
                                        break
                                else:
                                    try:
                                        sorted_hands.insert(i+1, hands[j])
                                        break
                                    except IndexError:
                                        sorted_hands.append(hands[j])
                                        break
                        else:
                            if i == len(sorted_hands)-1:
                                sorted_hands.append(hands[j])
                    else:
                        if i == len(sorted_hands)-1:
                            sorted_hands.append(hands[j])
                else:
                    if i == len(sorted_hands)-1:
                        sorted_hands.append(hands[j])
            else:
                if i == len(sorted_hands)-1:
                    sorted_hands.append(hands[j])       
                        
    return sorted_hands
                    
                        



def part1(data):
    high_card = []
    one_pair = []
    two_pair = []
    three_kind = []
    full_house = []
    four_kind = []
    five_kind = []
    for key in data:
        hand_dict = {}
        for char in key:
            try:
                hand_dict[char] += 1
            except KeyError:
                hand_dict[char] = 1
        if max(hand_dict.values()) == 5:
            five_kind.append(key)
        elif max(hand_dict.values()) == 4:
            four_kind.append(key)
        elif max(hand_dict.values()) == 3:
            if len(hand_dict) == 2:
                full_house.append(key)
            else:
                three_kind.append(key)
        elif max(hand_dict.values()) == 2:
            if len(hand_dict) == 3:
                two_pair.append(key)
            else:
                one_pair.append(key)
        else:
            high_card.append(key)

    if len(high_card) != 0:
        high_card = sort_hand_list(high_card, 1)
    if len(one_pair) != 0:
        one_pair = sort_hand_list(one_pair, 1)
    if len(two_pair) != 0:
        two_pair = sort_hand_list(two_pair, 1)
    if len(three_kind) != 0:
        three_kind = sort_hand_list(three_kind, 1)
    if len(full_house) != 0:
        full_house = sort_hand_list(full_house, 1)
    if len(four_kind) != 0:
        four_kind = sort_hand_list(four_kind, 1)
    if len(five_kind) != 0:
        five_kind = sort_hand_list(five_kind, 1)

    all_sorted_hands = high_card + one_pair + two_pair + three_kind + full_house + four_kind + five_kind

    total = 0
    for i, hand in enumerate(all_sorted_hands):
        total += int(data[hand]) * (i+1)
        # print(f"Hand = {hand}. Bet = {data[hand]}. Rank = {i+1}. Product = {int(data[hand]) * (i+1)}. Total sum = {total}.")
    
    return total
    

def part2(data):
    high_card = []
    one_pair = []
    two_pair = []
    three_kind = []
    full_house = []
    four_kind = []
    five_kind = []
    for key in data:
        hand_dict = {}
        for char in key:
            try:
                hand_dict[char] += 1
            except KeyError:
                hand_dict[char] = 1
        try:
            num_jokers = hand_dict["J"]
        except KeyError:
            num_jokers = 0
        if max(hand_dict.values()) == 5 or num_jokers == 4:
            five_kind.append(key)
        elif max(hand_dict.values()) == 4:
            if num_jokers == 1:
                five_kind.append(key)
            else:
                four_kind.append(key)
        elif max(hand_dict.values()) == 3:
            if len(hand_dict) == 2:
                if num_jokers in [2,3]:
                    five_kind.append(key)
                else:
                    full_house.append(key)
            else:
                if num_jokers in [1,3]:
                    four_kind.append(key)
                else:
                    three_kind.append(key)
        elif max(hand_dict.values()) == 2:
            if len(hand_dict) == 3:
                if num_jokers == 2:
                    four_kind.append(key)
                elif num_jokers == 1:
                    full_house.append(key)
                else:
                    two_pair.append(key)
            else:
                if num_jokers in [1,2]:
                    three_kind.append(key)
                else:
                    one_pair.append(key)
        else:
            if num_jokers == 1:
                one_pair.append(key)
            else:
                high_card.append(key)

    if len(high_card) != 0:
        high_card = sort_hand_list(high_card, 2)
    if len(one_pair) != 0:
        one_pair = sort_hand_list(one_pair, 2)
    if len(two_pair) != 0:
        two_pair = sort_hand_list(two_pair, 2)
    if len(three_kind) != 0:
        three_kind = sort_hand_list(three_kind, 2)
    if len(full_house) != 0:
        full_house = sort_hand_list(full_house, 2)
    if len(four_kind) != 0:
        four_kind = sort_hand_list(four_kind, 2)
    if len(five_kind) != 0:
        five_kind = sort_hand_list(five_kind, 2)

    all_sorted_hands = high_card + one_pair + two_pair + three_kind + full_house + four_kind + five_kind

    total = 0
    for i, hand in enumerate(all_sorted_hands):
        total += int(data[hand]) * (i+1)
        # print(f"Hand = {hand}. Bet = {data[hand]}. Rank = {i+1}. Product = {int(data[hand]) * (i+1)}. Total sum = {total}.")
    
    return total


if __name__ == "__main__":
    main()