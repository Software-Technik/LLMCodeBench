import sys
from collections import Counter

def part1(nums):
    def blink(arr):
        res = []
        for x in arr:
            if x == 0:
                res.append(1)
            elif len(str(x)) % 2 == 0:
                l = len(str(x))
                res.append(int(str(x)[: l // 2]))
                res.append(int(str(x)[l // 2 :]))
            else:
                res.append(x * 2024)
        return res

    for _ in range(25):
        nums = blink(nums)

    return len(nums)

def part2(raw_nums):
    nums = Counter(raw_nums)

    def blink(nums):
        new_nums = Counter()
        for x, count in nums.items():
            l = len(str(x))
            if x == 0:
                new_nums[1] += count
            elif l % 2 == 0:
                new_nums[int(str(x)[: l // 2])] += count
                new_nums[int(str(x)[l // 2 :])] += count
            else:
                new_nums[x * 2024] += count
        return new_nums

    for _ in range(75):
        nums = blink(nums)

    return sum(nums.values())

input_path = sys.argv[1]
with open(input_path) as fin:
    raw_nums = list(map(int, fin.read().strip().split()))
    print(part1(raw_nums), part2(raw_nums))