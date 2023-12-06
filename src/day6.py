from math import ceil
import numpy as np
from lib import *

# naive solution
def part1(data):
    times, distances = \
        [int(i) for i in data[0].split()[1:]], \
        [int(i) for i in data[1].split()[1:]]
    t_and_d = zip(times, distances)
    win_times = []
    for t, d in t_and_d:
        ways_to_win = 0
        for i in range(1, t + 1):
            distance_traveled = i * (t - i)
            if distance_traveled > d:
                ways_to_win += 1
        win_times.append(ways_to_win)
    
    return np.prod(win_times)

# smart solution
def part2(data):
    times, distances = \
        data[0].split()[1:], \
        data[1].split()[1:]
    t_and_d = zip(times, distances)
    time, distance = '', ''
    for t, d in t_and_d:
        time += t
        distance += d
    time, distance = int(time), int(distance)
    coeff = [-1, time, -distance]
    roots = sorted(np.roots(coeff))
    
    return ceil(roots[1]) - ceil(roots[0])

def main():
    data = read_input(6)
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()