import sys
import math
from itertools import combinations

def part1(data):
    packages, target_weight, max_pack_size = parse(data, 3)
    return get_min_qe(packages, target_weight, max_pack_size, get_conf3)

def part2(data):
    packages, target_weight, max_pack_size = parse(data, 4)
    return get_min_qe(packages, target_weight, max_pack_size, get_conf4)

def parse(data, n):
    packages = [*map(int, data)]
    target_weight = sum(packages) // n

    max_pack_size = len(packages)
    total = 0
    for i, p in enumerate(packages, 1):
        total += p
        if total >= target_weight:
            max_pack_size = i
            break
    return packages, target_weight, max_pack_size

def get_min_qe(packages, target_weight, max_pack_size, func):
    packages_sorted = sorted(packages, reverse=True)
    for i in range(1, max_pack_size + 1):
        min_qe = None
        for c in combinations(packages_sorted, i):
            if sum(c) != target_weight:
                continue
            conf = func(packages_sorted, target_weight, c)
            if conf is not False:
                current_qe = math.prod(conf[0])
                if min_qe is None or current_qe < min_qe:
                    min_qe = current_qe
        if min_qe is not None:
            return min_qe
    return None

def get_conf3(packages, target_weight, c):
    rest = [x for x in packages if x not in c]
    for j in range(len(c), len(rest) + 1):
        for c2 in combinations(rest, j):
            if sum(c2) != target_weight:
                continue
            c3 = [x for x in rest if x not in c2]
            if sum(c3) == target_weight:
                return (c, c2, c3)
    return False

def get_conf4(packages, target_weight, c):
    rest = [x for x in packages if x not in c]
    for j in range(len(c), len(rest) + 1):
        for c2 in combinations(rest, j):
            if sum(c2) != target_weight:
                continue
            rest2 = [x for x in rest if x not in c2]
            for k in range(len(c), len(rest2) + 1):
                for c3 in combinations(rest2, k):
                    if sum(c3) != target_weight:
                        continue
                    c4 = [x for x in rest2 if x not in c3]
                    if sum(c4) == target_weight:
                        return (c, c2, c3, c4)
    return False

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")