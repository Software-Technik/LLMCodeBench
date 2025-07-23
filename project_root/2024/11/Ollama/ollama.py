import sys
from collections import defaultdict

def blink1(arr):
    res = [1 if x == 0 else (sum((int(str(x)[: l // 2]), int(str(x)[l // 2 :])))) ** ((len(str(x)) % 2 != 0) + 1)) for x in arr]
    return res

def part1(nums):
    for _ in range(25): nums = blink1(nums)
    return len(nums)

def blink2(nums: dict):
    new_nums = defaultdict(int)
    for (x, cnt) in nums.items():
        l = len(str(x))
        if x == 0:
            new_nums[1] += cnt
        elif l % 2 == 0:
            left = int(str(x)[: l // 2])
            right = int(str(x)[l // 2 :])
            new_nums[left] += cnt
            new_nums[right] += cnt
        else:
            new_nums[x * 2024] += cnt
    return new_nums

def part2(raw_nums):
    nums = defaultdict(int)
    for x in raw_nums: nums[x] += 1

    for _ in range(75): nums = blink2(nums)

    return sum(nums.values())

input_path = sys.argv[1]
with open(input_path) as fin:
    raw_nums = list(map(int, fin.read().strip().split()))
    print(part1(raw_nums), part2(raw_nums))