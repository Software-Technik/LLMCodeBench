import sys

def is_increasing(nums):
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] not in (1, 2, 3):
            return False
    return True

def part1(lines):
    return sum(is_increasing([int(i) for i in line.split()]) for line in lines)

def is_redundant(nums):
    for i in range(len(nums)):
        if is_increasing(nums[:i] + nums[i + 1:]):
            return False
    return True

def part2(lines):
    return sum(is_increasing([int(i) for i in line.split()]) or is_redundant([int(i) for i in line.split()]) for line in lines)

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))