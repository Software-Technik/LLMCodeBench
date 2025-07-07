import sys
import math
from itertools import combinations
from functools import lru_cache

def parse(data, n):
    packs = tuple(sorted(map(int, data), reverse=True))
    target = sum(packs) // n
    return packs, target

@lru_cache(None)
def can_partition(packs, k):
    if k == 1:
        return True
    total = sum(packs)
    target = total // k
    length = len(packs)
    for size in range(1, length):
        for combo in combinations(packs, size):
            if sum(combo) != target:
                continue
            rem = list(packs)
            for x in combo:
                rem.remove(x)
            rem = tuple(rem)
            if can_partition(tuple(sorted(rem, reverse=True)), k-1):
                return True
    return False

def solve(data, n):
    packs, target = parse(data, n)
    length = len(packs)
    for size in range(1, length):
        qes = []
        for combo in combinations(packs, size):
            if sum(combo) != target:
                continue
            rem = list(packs)
            for x in combo:
                rem.remove(x)
            if can_partition(tuple(sorted(rem, reverse=True)), n-1):
                qes.append(math.prod(combo))
        if qes:
            return min(qes)

data = [line.strip() for line in open(sys.argv[1])]
print(solve(data, 3))
print(solve(data, 4))