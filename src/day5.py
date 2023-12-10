from lib import *

def naive_ass_solution(maps, seed):
    #print(seed, maps)
    current_value = seed
    for map_group in maps:
        for m in map_group:
            dest, source, length = m
            if current_value in range(source, source + length):
                current_value = dest + (current_value - source)
                break
    return current_value

def seed_to_dest_ranges(seed_range, map_group):
    normal_ranges = [seed_range]
    dest_ranges = []
    for m in map_group:
        dest, source, length = m
        source_range = range(source, source + length)
        for i, n in enumerate(normal_ranges):
            if source_range.start > n.start or \
                source_range.stop < n.stop:
                new_ranges = []
                dest_range_start, dest_range_stop = dest + (n.start - source), dest + (n.stop - source)
                if source_range.start > n.start:
                    new_ranges.append(range(n.start, source_range.start))
                    dest_range_start = dest
                if source_range.stop < n.stop:
                    new_ranges.append(range(source_range.stop, n.stop))
                    dest_range_stop = dest + length
                del normal_ranges[i]
                normal_ranges += new_ranges
                dest_ranges.append(range(dest_range_start, dest_range_stop))
                break
    return normal_ranges + dest_ranges


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
        location_list.append(naive_ass_solution(maps, seed))
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

    seed_ranges = []
    for i in range(0, len(seeds), 2):
        seed, seed_length = seeds[i], seeds[i + 1]
        seed_range = range(seed, seed + seed_length)
        seed_ranges.append(seed_range)
    
    for seed_range in seed_ranges:
        current_ranges = [seed_range]
        for map_group in maps:
            new_ranges = []
            for r in current_ranges:
                new_ranges += seed_to_dest_ranges(r, map_group)
            print(new_ranges)
            current_ranges = new_ranges


def main():
    data = read_input(5)
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()