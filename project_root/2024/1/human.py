from collections import defaultdict
import sys


def part1(data):
    ans = 0
    a = []
    b = []

    for line in data.strip().split("\n"):
        nums = [int(i) for i in line.split("   ")]
        a.append(nums[0])
        b.append(nums[1])

    a.sort()
    b.sort()

    for i in range(len(a)):
        ans += abs(a[i] - b[i])

    return ans


def part2(data):
    ans = 0
    a = []
    b = []

    for line in data.strip().split("\n"):
        nums = [int(i) for i in line.split("   ")]
        a.append(nums[0])
        b.append(nums[1])

    counts = defaultdict(int)
    for x in b:
        counts[x] += 1

    for x in a:
        ans += x * counts[x]

    return ans


input_path = sys.argv[1]
with open(input_path) as fin:
    data = fin.read()
    print(part1(data), part2(data))
