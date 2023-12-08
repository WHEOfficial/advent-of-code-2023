from functools import reduce
from lib import *
from re import search

# borrowed (stolen) from https://stackoverflow.com/questions/147515/least-common-multiple-for-3-or-more-numbers
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(a):
    """Return lcm of args."""
    return reduce(lcm, a)

def part1(data):
    directions = data[0]
    network_map = {}

    for l in data[2:]:
        result = search(r"(.*) = \((.*), (.*)\)", l)
        node, left, right = result.groups()
        network_map[node] = (left, right)
    
    steps = 0
    dir_index = 0
    current_node = 'AAA'
    while current_node != 'ZZZ':
        direction = 0 if directions[dir_index] == 'L' else 1
        current_node = network_map[current_node][direction]
        dir_index = (dir_index + 1) % len(directions)
        steps += 1

    return steps


def part2(data):
    directions = data[0]
    network_map = {}
    current_nodes = []

    for l in data[2:]:
        result = search(r"(.*) = \((.*), (.*)\)", l)
        node, left, right = result.groups()
        network_map[node] = (left, right)
        if node.endswith('A'):
            current_nodes.append(node)

    steps = 0
    steps_list = []
    dir_index = 0
    while not all([node.endswith('Z') for node in current_nodes]):
        direction = 0 if directions[dir_index] == 'L' else 1
        for i, node in enumerate(current_nodes):
            if not node.endswith('Z'):
                current_nodes[i] = network_map[node][direction]
                if current_nodes[i].endswith('Z'):
                    steps_list.append(steps + 1)
        dir_index = (dir_index + 1) % len(directions)
        steps += 1
    
    return lcmm(steps_list)

def main():
    data = read_input(8)
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()