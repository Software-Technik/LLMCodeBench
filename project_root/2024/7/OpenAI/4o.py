import sys
from itertools import product


def part1(lines):
    ans = 0
    for line in lines:
        parts = line.split()
        value = int(parts[0][:-1])
        nums = list(map(int, parts[1:]))
        for combo in product("*+", repeat=len(nums) - 1):
            result = nums[0]
            for i, op in enumerate(combo):
                result = result + nums[i + 1] if op == "+" else result * nums[i + 1]
            if result == value:
                ans += value
                break
    return ans


def part2(lines):
    ans = 0
    for line in lines:
        parts = line.split()
        value = int(parts[0][:-1])
        nums = list(map(int, parts[1:]))
        for combo in product("*+|", repeat=len(nums) - 1):
            result = nums[0]
            for i, op in enumerate(combo):
                if op == "+":
                    result += nums[i + 1]
                elif op == "|":
                    result = int(f"{result}{nums[i + 1]}")
                else:
                    result *= nums[i + 1]
            if result == value:
                ans += value
                break
    return ans


input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))