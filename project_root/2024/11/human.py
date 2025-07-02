import sys
from collections import defaultdict


def part1(nums):
    def blink(arr):
        res = []
        for x in arr:
            if x == 0:
                res.append(1)
            elif len(str(x)) % 2 == 0:
                l = len(str(x))
                res += [int(str(x)[: l // 2]), int(str(x)[l // 2 :])]
            else:
                res += [x * 2024]

        return res

    for i in range(25):
        nums = blink(nums)


    return len(nums)


def part2(raw_nums):
    sys.setrecursionlimit(2**30)

    nums = defaultdict(int)
    for x in raw_nums:
        nums[x] += 1

    def blink(nums: dict):
        new_nums = defaultdict(int)
        for x in nums:
            l = len(str(x))
            if x == 0:
                new_nums[1] += nums[0]
            elif l % 2 == 0:
                new_nums[int(str(x)[: l // 2])] += nums[x]
                new_nums[int(str(x)[l // 2 :])] += nums[x]
            else:
                new_nums[x * 2024] += nums[x]

        return new_nums

    for i in range(75):
        nums = blink(nums)

    ans = 0
    for x in nums:
        ans += nums[x]
    return ans


input_path = sys.argv[1]
with open(input_path) as fin:
    raw_nums = list(map(int, fin.read().strip().split()))
    print(part1(raw_nums), part2(raw_nums))
