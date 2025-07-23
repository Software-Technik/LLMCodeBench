import sys
from itertools import product


def part1(lines):
    ans = 0
    for line in lines:
        parts = line.split()
        value = int(parts[0][:-1])
        nums = list(map(int, parts[1:]))
        length = len(nums) - 1
        
        for combo in product("*+", repeat=length):
            res = nums[0]
            for i in range(length):
                if combo[i] == "+":
                    res += nums[i + 1]
                else:
                    res *= nums[i + 1]
            if res == value:
                ans += value
                break
    return ans


def part2(lines):
    ans = 0
    for line in lines:
        parts = line.split()
        value = int(parts[0][:-1])
        nums = list(map(int, parts[1:]))
        length = len(nums) - 1
        
        for combo in product("*+|", repeat=length):
            res = nums[0]
            for i in range(length):
                if combo[i] == "+":
                    res += nums[i + 1]
                elif combo[i] == "|":
                    res = int(f"{res}{nums[i + 1]}")
                else:
                    res *= nums[i + 1]
            if res == value:
                ans += value
                break
    return ans


input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))