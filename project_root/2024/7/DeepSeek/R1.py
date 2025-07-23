import sys
from itertools import product

def part1(lines):
    ans = 0
    for line in lines:
        parts = line.split()
        value = int(parts[0][:-1])
        nums = list(map(int, parts[1:]))
        
        for combo in product("*+", repeat=len(nums)-1):
            cur = nums[0]
            for i in range(1, len(nums)):
                if cur > value:
                    break
                if combo[i-1] == '+':
                    cur += nums[i]
                else:
                    cur *= nums[i]
            else:
                if cur == value:
                    ans += value
                    break
    return ans

def part2(lines):
    ans = 0
    for line in lines:
        parts = line.split()
        value = int(parts[0][:-1])
        nums = list(map(int, parts[1:]))
        
        for combo in product("*+|", repeat=len(nums)-1):
            cur = nums[0]
            for i in range(1, len(nums)):
                if cur > value:
                    break
                op = combo[i-1]
                if op == '+':
                    cur += nums[i]
                elif op == '|':
                    num_digits = len(str(nums[i]))
                    cur = cur * (10 ** num_digits) + nums[i]
                else:
                    cur *= nums[i]
            else:
                if cur == value:
                    ans += value
                    break
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))