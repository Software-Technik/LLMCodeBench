import sys
from collections import defaultdict

def part1(nums):
    def blink(arr):
        res = []
        for x in arr:
            if x == 0:
                res.append(1)
            else:
                s = str(x)
                l = len(s)
                if l % 2 == 0:
                    half = l // 2
                    res.append(int(s[:half]))
                    res.append(int(s[half:]))
                else:
                    res.append(x * 2024)
        return res

    for _ in range(25):
        nums = blink(nums)
    return len(nums)

def part2(raw_nums):
    sys.setrecursionlimit(1 << 30)
    nums = defaultdict(int)
    for x in raw_nums:
        nums[x] += 1

    for _ in range(75):
        new_nums = defaultdict(int)
        for x, count in nums.items():
            if x == 0:
                new_nums[1] += count
            else:
                s = str(x)
                l = len(s)
                if l % 2 == 0:
                    half = l // 2
                    new_nums[int(s[:half])] += count
                    new_nums[int(s[half:])] += count
                else:
                    new_nums[x * 2024] += count
        nums = new_nums
    return sum(nums.values())

input_path = sys.argv[1]
with open(input_path) as fin:
    raw_nums = list(map(int, fin.read().strip().split()))
    print(part1(raw_nums), part2(raw_nums))