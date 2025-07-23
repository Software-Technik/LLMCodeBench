import sys
from itertools import product

def calculate(nums, combo):
    val = nums[0]
    for i in range(1, len(nums)):
        if combo[i - 1] == '+':
            val += nums[i]
        elif combo[i - 1] == '|':
            val = int(f"{val}{nums[i]}")
        else:
            val *= nums[i]
    return val

def part1(lines):
    ans = 0
    for line in lines:
        parts = line.split()
        value, nums = int(parts[0][:-1]), list(map(int, parts[1:]))
        if any(value == calculate(nums, combo) for combo in product("*+", repeat=len(nums) - 1)):
            ans += value
    return ans

def part2(lines):
    ans = 0
    for line in lines:
        parts = line.split()
        value, nums = int(parts[0][:-1]), list(map(int, parts[1:]))
        if any(value == calculate(nums, combo) for combo in product("*+|", repeat=len(nums) - 1)):
            ans += value
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
print(part1(lines), part2(lines))