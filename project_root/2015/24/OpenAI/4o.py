import sys
import math
from itertools import combinations

def part1(data):
    packages, target_weight = parse(data, 3)
    return get_min_qe(packages, target_weight, get_conf3)

def part2(data):
    packages, target_weight = parse(data, 4)
    return get_min_qe(packages, target_weight, get_conf4)

def parse(data, n):
    packages = list(map(int, data))
    target_weight = sum(packages) // n
    return packages, target_weight

def get_min_qe(packages, target_weight, func):
    for i in range(len(packages)):
        combs = (combs for combs in combinations(packages, i) if sum(combs) == target_weight)
        valid_confs = (func(packages, target_weight, c) for c in combs)
        valid_confs = [conf for conf in valid_confs if conf is not False]
        if valid_confs:
            return min(math.prod(i[0]) for i in valid_confs)

def get_conf3(packages, target_weight, c):
    rest = set(packages) - set(c)
    for j in range(1, len(rest) + 1):
        combs2 = (combs2 for combs2 in combinations(rest, j) if sum(combs2) == target_weight)
        for c2 in combs2:
            c3 = rest - set(c2)
            if sum(c3) == target_weight:
                return (c, c2, c3)
    return False

def get_conf4(packages, target_weight, c):
    rest = set(packages) - set(c)
    for j in range(1, len(rest) + 1):
        combs2 = (combs2 for combs2 in combinations(rest, j) if sum(combs2) == target_weight)
        for c2 in combs2:
            rest2 = rest - set(c2)
            for k in range(1, len(rest2) + 1):
                combs3 = (combs3 for combs3 in combinations(rest2, k) if sum(combs3) == target_weight)
                for c3 in combs3:
                    c4 = rest2 - set(c3)
                    if sum(c4) == target_weight:
                        return (c, c2, c3, c4)
    return False

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        data = [line.strip() for line in f]
    print(part1(data))
    print(part2(data))