from lib import *

def part1(data):
    s = 0
    for l in data:
        nums = [int(n) for n in l.split()]
        next_value = nums[-1]
        while not all(n == 0 for n in nums):
            new_nums = []
            for i in range(len(nums) - 1, 0, -1):
                new_nums.insert(0, nums[i] - nums[i - 1])
            nums = new_nums
            next_value += nums[-1]
        s += next_value
    return s

def part2(data):
    s = 0
    for l in data:
        nums = [int(n) for n in l.split()]
        first_nums = [nums[0]]
        while not all(n == 0 for n in nums):
            new_nums = []
            for i in range(len(nums) - 1, 0, -1):
                new_nums.insert(0, nums[i] - nums[i - 1])
            nums = new_nums
            first_nums.append(nums[0])
        previous_value = 0
        for i in range(len(first_nums) - 2, -1, -1):
            previous_value = first_nums[i] - previous_value
        s += previous_value
    return s

def main():
    data = read_input(9)
    print(part1(data))
    print(part2(data))

if __name__ == '__main__':
    main()