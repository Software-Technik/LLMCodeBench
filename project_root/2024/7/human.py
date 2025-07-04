import sys
from itertools import product


def part1(lines):

    ans = 0
    for i, line in enumerate(lines):
        parts = line.split()
        value = int(parts[0][:-1])
        nums = list(map(int, parts[1:]))

        def test(combo):
            ans = nums[0]
            for i in range(1, len(nums)):
                if combo[i - 1] == "+":
                    ans += nums[i]
                else:
                    ans *= nums[i]
            return ans

        for combo in product("*+", repeat=len(nums) - 1):
            if test(combo) == value:
                ans += value
                break

    return ans


def part2(lines):

    ans = 0
    for i, line in enumerate(lines):
        parts = line.split()
        value = int(parts[0][:-1])
        nums = list(map(int, parts[1:]))

        def test(combo):
            ans = nums[0]
            for i in range(1, len(nums)):
                if combo[i - 1] == "+":
                    ans += nums[i]
                elif combo[i - 1] == "|":
                    ans = int(f"{ans}{nums[i]}")
                else:
                    ans *= nums[i]
            return ans

        for combo in product("*+|", repeat=len(nums) - 1):
            if test(combo) == value:
                ans += value
                break

    return ans


input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n")
    print(part1(lines), part2(lines))
