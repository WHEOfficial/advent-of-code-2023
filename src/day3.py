from lib import *

def check_adjacent(data, row, col):
    for r in range(row - 1, row + 2):
        if r >= 0 and r < len(data):
            for c in range(col - 1, col + 2):
                if c >= 0 and c < len(data):
                    ch = data[r][c]
                    if not ch.isdigit() and ch != '.':
                        return True
    return False

def find_adjacent_numbers(data, row, col):
    adj_nums = []
    covered = []
    for r in range(row - 1, row + 2):
        if r >= 0 and r < len(data):
            for c in range(col - 1, col + 2):
                if c >= 0 and c < len(data):
                    ch = data[r][c]
                    if ch.isdigit() and (r, c) not in covered:
                        num = ch
                        dc = c - 1
                        while dc >= 0 and data[r][dc].isdigit():
                            num = data[r][dc] + num
                            covered.append((r, dc))
                            dc -= 1
                        dc = c + 1
                        while dc < len(data) and data[r][dc].isdigit():
                            num += data[r][dc]
                            covered.append((r, dc))
                            dc += 1
                        adj_nums.append(int(num))
                    covered.append((r, c))
    return adj_nums

def part1(data):
    s = 0
    for row, l in enumerate(data):
        num = ''
        valid = False
        for col, c in enumerate(l):
            if c.isdigit():
                num += c
                if not valid:
                    valid = check_adjacent(data, row, col)
            else:
                if num != '' and valid:
                    num = int(num)
                    s += num
                    valid = False
                num = ''
        if num != '' and valid:
            num = int(num)
            s += num
    
    return s

def part2(data):
    s = 0
    for row, l in enumerate(data):
        star_pos = [i for i, c in enumerate(l) if c == '*']
        for col in star_pos:
            adj_nums = find_adjacent_numbers(data, row, col)
            if len(adj_nums) == 2:
                s += adj_nums[0] * adj_nums[1]

    return s

def main():
    data = read_input(3)
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()