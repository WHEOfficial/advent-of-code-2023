from collections import Counter
from lib import *

rankings = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def part1(data):
    hand_classes = [[] for i in range(6)]
    print(hand_classes)

    for l in data:
        hand, bid = l.split()
        hand_counter = Counter(list(hand)).values()
        


def part2(data):
    pass

def main():
    data = read_input(7)
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()