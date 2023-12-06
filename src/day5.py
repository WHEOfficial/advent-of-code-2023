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

def source_to_dest_ranges(source_range, map_group):
    dest_ranges = []
    for m in map_group:
        dest, source, length = m
        m_source_range = range(source, source + length)
        m_dest_range = range(dest, dest + length)
        #print(m_dest_range)
        print(source_range, m_source_range.start, m_source_range.stop)
        if m_source_range.start in source_range and \
            m_source_range.stop in source_range:
            dest_ranges.append(m_dest_range)
        elif m_source_range.start in source_range:
            dest_ranges.append(range(dest, source_range.stop))
        elif m_source_range.stop in source_range:
            dest_ranges.append(range(source_range.start,  dest + length))
    return dest_ranges

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
    
    print(source_to_dest_ranges(range(100), maps[0]))
    
    # p = Pool()
    # location_list = []
    # for i, seed_range in enumerate(seed_ranges):
    #     print(f"Starting range {i + 1}/{len(seed_ranges)} ({seed_range})")
    #     answer = p.map(partial(naive_ass_solution, maps), seed_range)
    #     location_list.append(min(answer))
    #     print(f"Completed range {i + 1}/{len(seed_ranges)}")
    # return min(location_list)
    
    # for i in range(0, len(seeds), 2):
    #     seed, seed_length = seeds[i], seeds[i + 1]
    #     seed_range = range(seed, seed + seed_length)
    #     current_ranges = [seed_range]
        
        # for map_group in maps:
        #     print(current_ranges)
        #     new_ranges = []
        #     for r in current_ranges:
        #         num = r.start
        #         while num < r.stop:
        #             for m in map_group:
        #                 dest, source, length = m
        #                 source_range = range(source, source + length)
        #                 if num in source_range:
        #                     new_range = dest + (num - source)
        #                     if (source + length) - 1 in r:
        #                         new_range = range(new_range, source + length)
        #                         new_ranges.append(new_range)
        #                         num = source + length
        #                         break
        #                     else:


def main():
    data = read_input(5)
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()