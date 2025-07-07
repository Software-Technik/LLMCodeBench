import sys
from collections import defaultdict

data = open(sys.argv[1]).read().splitlines()
reactions = {}
for line in data:
    lhs, rhs = line.split(' => ')
    out_n, out_c = rhs.split()
    inputs = []
    for tok in lhs.split(', '):
        n, c = tok.split()
        inputs.append((int(n), c))
    reactions[out_c] = (int(out_n), inputs)

def ore_needed(fuel):
    need = {'FUEL': fuel}
    leftovers = defaultdict(int)
    ore = 0
    while True:
        chem = next((c for c in need if c != 'ORE' and need[c] > 0), None)
        if not chem:
            break
        qty = need.pop(chem)
        avail = leftovers[chem]
        if avail >= qty:
            leftovers[chem] = avail - qty
            continue
        qty -= avail
        leftovers[chem] = 0
        out_qty, ingredients = reactions[chem]
        times = (qty + out_qty - 1) // out_qty
        leftovers[chem] += times * out_qty - qty
        for n, c in ingredients:
            if c == 'ORE':
                ore += n * times
            else:
                need[c] = need.get(c, 0) + n * times
    ore += need.get('ORE', 0)
    return ore

p1 = ore_needed(1)
limit = 10**12
l, r = 1, 1
while ore_needed(r) <= limit:
    r *= 2
while l < r:
    m = (l + r + 1) // 2
    if ore_needed(m) <= limit:
        l = m
    else:
        r = m - 1
p2 = l

print(p1, p2)