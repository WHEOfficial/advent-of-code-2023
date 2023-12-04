from lib import *

def part1(data):
    s = 0
    for l in data:
        cleaned = l.split()[2:]
        winning_numbers = []
        valid_numbers = []
        pipe_status = False
        for num in cleaned:
            if num == '|':
                pipe_status = True
                continue
            if not pipe_status:
                winning_numbers.append(int(num))
            else:
                if int(num) in winning_numbers:
                    valid_numbers.append(int(num))
        if len(valid_numbers) == 0:
            continue
        s += 2**(len(valid_numbers) - 1)
    return s
    

def part2(data):
    num_cards = [1] * len(data)
    for i, l in enumerate(data):
        cleaned = l.split()[2:]
        winning_numbers = []
        valid_numbers = []
        pipe_status = False
        for num in cleaned:
            if num == '|':
                pipe_status = True
                continue
            if not pipe_status:
                winning_numbers.append(int(num))
            else:
                if int(num) in winning_numbers:
                    valid_numbers.append(int(num))
        if len(valid_numbers) == 0:
            continue
        for j in range(i + 1, min(len(data), i + len(valid_numbers) + 1)):
            num_cards[j] += num_cards[i]
    return sum(num_cards)

def main():
    data = read_input(4)
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()