from lib import *

num_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def part1(data):
    s = 0
    for l in data:
        first, last = None, None
        for c in l:
            if c.isdigit():
                if first is None:
                    first = c
                last = c
        s += int(first + last)
    return s

def part2(data):
    s = 0
    for l in data:
        first, last = None, None
        str_build = ''
        digit = None
        for c in l:
            if c.isdigit():
                str_build = ''
                digit = c
            else:
                str_build += c
                for k in num_dict.keys():
                    if k in str_build:
                        digit = str(num_dict[k])
                        str_build = str_build[-1]
            if digit:
                if first is None:
                    first = digit
                last = digit
                digit = None
        s += int(first + last)
    return s

def main():
    data = read_input(1)
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()