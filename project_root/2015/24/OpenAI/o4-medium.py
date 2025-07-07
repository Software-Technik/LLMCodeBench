import sys,math,itertools

packages = [int(line) for line in open(sys.argv[1])]
total = sum(packages)
packages.sort(reverse=True)

def can_partition(rest, groups, target):
    if groups == 1:
        return sum(rest) == target
    n = len(rest)
    for size in range(1, n - (groups - 1) + 1):
        for comb in itertools.combinations(rest, size):
            if sum(comb) == target:
                nr = list(rest)
                for v in comb: nr.remove(v)
                if can_partition(nr, groups - 1, target):
                    return True
    return False

def solve(groups):
    target = total // groups
    for size in range(1, len(packages) + 1):
        qes = []
        for comb in itertools.combinations(packages, size):
            if sum(comb) == target:
                rest = list(packages)
                for v in comb: rest.remove(v)
                if can_partition(rest, groups - 1, target):
                    qes.append(math.prod(comb))
        if qes:
            return min(qes)

print(solve(3))
print(solve(4))