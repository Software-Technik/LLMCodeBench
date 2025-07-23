import sys
import math
from itertools import combinations

def part1(data):
    packages, target_weight, max_pack_size = parse(data, 3)
    return get_min_qe(packages, target_weight, max_pack_size, can_partition_two)

def part2(data):
    packages, target_weight, max_pack_size = parse(data, 4)
    return get_min_qe(packages, target_weight, max_pack_size, can_partition_three)

def parse(data, n):
    packages = sorted(map(int, data), reverse=True)
    target_weight = sum(packages) // n
    max_pack_size = 0
    s = 0
    for i, w in enumerate(packages):
        s += w
        if s >= target_weight:
            max_pack_size = i+1
            break
    return packages, target_weight, max_pack_size

def get_min_qe(packages, target_weight, max_pack_size, func):
    for i in range(1, max_pack_size+1):
        combs = []
        for c in combinations(packages, i):
            if sum(c) == target_weight:
                combs.append(c)
        if not combs:
            continue
        combs.sort(key=lambda c: math.prod(c))
        for c in combs:
            if func(packages, target_weight, c):
                return math.prod(c)

def can_partition_two(packages, target_weight, c):
    rest = [x for x in packages if x not in c]
    total_rest = sum(rest)
    if total_rest != 2 * target_weight:
        return False
    dp = [False] * (target_weight+1)
    dp[0] = True
    for num in rest:
        for s in range(target_weight, num-1, -1):
            if dp[s-num]:
                dp[s] = True
        if dp[target_weight]:
            return True
    return dp[target_weight]

def can_partition_three(packages, target_weight, c):
    rest = [x for x in packages if x not in c]
    total_rest = sum(rest)
    if total_rest != 3 * target_weight:
        return False
    dp = set()
    dp.add((0,0))
    for num in rest:
        new_dp = set()
        for (a, b) in dp:
            if a + num <= target_weight:
                new_dp.add((a+num, b))
            if b + num <= target_weight:
                new_dp.add((a, b+num))
            new_dp.add((a, b))
        dp = new_dp
        if (target_weight, target_weight) in dp:
            return True
    return False

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")