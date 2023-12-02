import numpy
from lib import *

maxes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def part1(data):
    s = 0
    for id, l in enumerate(data):
        cleaned = l.split(' ')
        valid = True
        for i in range(2, len(cleaned), 2):
            number, color = int(cleaned[i]), cleaned[i + 1].replace(',', '').replace(';', '')
            if number > maxes[color]:
                #print(id, number, maxes[color])
                valid = False
                break
        if valid:
            s += (id + 1)
    return s


def part2(data):
    s = 0
    for l in data:
        cleaned = l.split(' ')
        color_map = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for i in range(2, len(cleaned), 2):
            number, color = int(cleaned[i]), cleaned[i + 1].replace(',', '').replace(';', '')
            if number > color_map[color]:
                color_map[color] = number
        product = numpy.prod([v for v in color_map.values()])
        s += product
    return s

def main():
    data = read_input(2)
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()