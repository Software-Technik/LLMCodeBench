import sys
from itertools import permutations

def parse_guest(data):
    g = {}
    for line in data:
        p = line.split()
        h = int(p[3]) * (1 if p[2] == 'gain' else -1)
        a, b = p[0], p[10][:-1]
        g.setdefault(a, {})[b] = h
    return g

def calc_max_happiness(g):
    keys = list(g.keys())
    n = len(keys)
    best = -10**18
    for arr in permutations(keys):
        s = 0
        for i, v in enumerate(arr):
            s += g[v][arr[(i+1)%n]] + g[v][arr[i-1]]
        if s > best:
            best = s
    return best

def part1(data):
    return calc_max_happiness(parse_guest(data))

def part2(data):
    g = parse_guest(data)
    for k in list(g):
        g[k]['me'] = 0
    g['me'] = {k: 0 for k in g}
    return calc_max_happiness(g)

data = [l.strip() for l in open(sys.argv[1])]
print(part1(data))
print(part2(data))