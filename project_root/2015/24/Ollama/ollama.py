import sys
from itertools import combinations

def part1(data):
    packages, target_weight, max_pack_size = parse(data, 3)
    return get_min_qe(packages, target_weight, max_pack_size, get_conf3)

def part2(data):
    packages, target_weight, max_pack_size = parse(data, 4)
    return get_min_qe(packages, target_weight, max_pack_size, get_conf4)

def parse(data, n):
    packages = list(map(int, data))
    target_weight = sum(packages) // n
    max_pack_size = next(i for i in range(1, len(packages)) if sum(packages[:i]) >= target_weight)
    return packages, target_weight, max_pack_size

def get_min_qe(packages, target_weight, max_pack_size, func):
    confs = []
    for i in range(1, max_pack_size + 1):
        combs = (c for c in combinations(packages, i) if sum(c) == target_weight)
        for c in combs:
            conf = func(packages, target_weight, c)
            if conf is not False:
                confs.append(conf)

        if confs:
            s = [prod(c) for c in confs]
            return min(s)

def get_conf3(packages, target_weight, c):
    rest = [x for x in packages if x not in c]
    for j in range(1, len(rest)):
        combs2 = (c2 for c2 in combinations(rest, j) if sum(c2) == target_weight)
        for c2 in combs2:
            c3 = [i for i in rest if i not in c2]
            if sum(c3) == target_weight:
                return (c, c2, c3)
    return False

def get_conf4(packages, target_weight, c):
    rest = [x for x in packages if x not in c]
    for j in range(1, len(rest)):
        combs2 = (c2 for c2 in combinations(rest, j) if sum(c2) == target_weight)
        for c2 in combs2:
            rest2 = [x for x in rest if x not in c2]
            for k in range(1, len(rest2)):
                combs3 = (c3 for c3 in combinations(rest2, k) if sum(c3) == target_weight)
                for c3 in combs3:
                    c4 = [x for x in rest2 if x not in c3]
                    if sum(c4) == target_weight:
                        return (c, c2, c3, c4)
    return False

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")