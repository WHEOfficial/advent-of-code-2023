from collections import Counter
from enum import Enum
from functools import cmp_to_key
from lib import *

rankings_one = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
rankings_two = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

class Hands(Enum):
    FIVE_OF_A_KIND = 0
    FOUR_OF_A_KIND = 1
    FULL_HOUSE = 2
    THREE_OF_A_KIND = 3
    TWO_PAIR = 4
    ONE_PAIR = 5
    HIGH_CARD = 6

# this is ugly but i don't really care right now

def hand_sorter_one(x, y):
    x, y = x[0], y[0]
    for cx, cy in zip(x, y):
        x_val, y_val = rankings_one.index(cx), rankings_one.index(cy)
        if x_val > y_val:
            return 1
        elif x_val < y_val:
            return -1
    return 0

def hand_sorter_two(x, y):
    x, y = x[0], y[0]
    for cx, cy in zip(x, y):
        x_val, y_val = rankings_two.index(cx), rankings_two.index(cy)
        if x_val > y_val:
            return 1
        elif x_val < y_val:
            return -1
    return 0

def part1(data):
    hand_classes = [[] for i in range(7)]

    for l in data:
        hand, bid = l.split()
        hand_and_bid = (hand, int(bid))
        hand_counter = Counter(list(hand))

        hand_values = hand_counter.values()
        max_card = max(hand_counter)
        len_values = len(hand_values)

        if max_card == 5:
            hand_classes[Hands.FIVE_OF_A_KIND.value].append(hand_and_bid)
        elif max_card == 4:
            hand_classes[Hands.FOUR_OF_A_KIND.value].append(hand_and_bid)
        elif len_values == 2 and max_card == 3:
            hand_classes[Hands.FULL_HOUSE.value].append(hand_and_bid)
        elif max_card == 3:
            hand_classes[Hands.THREE_OF_A_KIND.value].append(hand_and_bid)
        elif len_values == 3 and max_card == 2:
            hand_classes[Hands.TWO_PAIR.value].append(hand_and_bid)
        elif max_card == 2:
            hand_classes[Hands.ONE_PAIR.value].append(hand_and_bid)
        else:
            hand_classes[Hands.HIGH_CARD.value].append(hand_and_bid)
        
    sorted_hand_classes = []
    for c in hand_classes:
        sorted_hand_classes += sorted(c, key=cmp_to_key(hand_sorter_one))

    s = 0
    length = len(sorted_hand_classes)
    for i, v in enumerate(sorted_hand_classes):
        s += v[1] * (length - i)
    
    return s    

def part2(data):
    hand_classes = [[] for i in range(7)]

    for l in data:
        hand, bid = l.split()
        hand_and_bid = (hand, int(bid))
        hand_counter = Counter(list(hand))

        joker_count = hand_counter['J'] if hand_counter['J'] is not None else 0

        # to handle the JJJJJ edge case
        if len(hand_counter) != 1:
            del hand_counter['J']
        else:
            joker_count = 0

        hand_values = hand_counter.values()
        max_card = max(hand_values) + joker_count
        len_values = len(hand_values)
        
        if max_card == 5:
            hand_classes[Hands.FIVE_OF_A_KIND.value].append(hand_and_bid)
        elif max_card == 4:
            hand_classes[Hands.FOUR_OF_A_KIND.value].append(hand_and_bid)
        elif len_values == 2 and max_card == 3:
            hand_classes[Hands.FULL_HOUSE.value].append(hand_and_bid)
        elif max_card == 3:
            hand_classes[Hands.THREE_OF_A_KIND.value].append(hand_and_bid)
        elif len_values == 3 and max_card == 2:
            hand_classes[Hands.TWO_PAIR.value].append(hand_and_bid)
        elif max_card == 2:
            hand_classes[Hands.ONE_PAIR.value].append(hand_and_bid)
        else:
            hand_classes[Hands.HIGH_CARD.value].append(hand_and_bid)
        
    sorted_hand_classes = []
    for c in hand_classes:
        sorted_hand_classes += sorted(c, key=cmp_to_key(hand_sorter_two))

    s = 0
    length = len(sorted_hand_classes)
    for i, v in enumerate(sorted_hand_classes):
        s += v[1] * (length - i)
    
    return s    

def main():
    data = read_input(7)
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()