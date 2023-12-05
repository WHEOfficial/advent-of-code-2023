from lib import *

def part1(data):
    seeds = [int(i) for i in data[0].split()[1:]]
    maps = []
    map_index = -1
    line = 1
    while line < len(data):
        if data[line] == '':
            map_index +=1 
            maps.append([])
            line += 1
        else:
            one_map = [int(i) for i in data[line].split()]
            maps[map_index].append(one_map)
        line += 1
    
    location_list = []
    for seed in seeds:
        current_value = seed
        for map_group in maps:
            for m in map_group:
                dest, source, length = m
                if current_value in range(source, source + length):
                    current_value = dest + (current_value - source)
                    break
        location_list.append(current_value)
    return min(location_list)

def part2(data):
    seeds = [int(i) for i in data[0].split()[1:]]
    maps = []
    map_index = -1
    line = 1
    while line < len(data):
        if data[line] == '':
            map_index +=1 
            maps.append([])
            line += 1
        else:
            one_map = [int(i) for i in data[line].split()]
            maps[map_index].append(one_map)
        line += 1
    
    for i in range(0, len(seeds), 2):
        seed, length = seeds[i], seeds[i + 1]
        seed_range = range(seed, seed + length)
        current_values = []
        starting_maps = maps[0]
        print(starting_maps)


def main():
    data = read_input(5)
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()