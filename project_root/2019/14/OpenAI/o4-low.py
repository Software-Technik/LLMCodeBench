import sys
from math import ceil
from collections import defaultdict

def ore_needed(reactions, fuel):
    needed = {"FUEL": fuel}
    leftovers = defaultdict(int)
    while True:
        if not any(chem != "ORE" for chem in needed):
            return needed["ORE"]
        newneeded = {}
        if "ORE" in needed:
            newneeded["ORE"] = needed["ORE"]
        for chem, qty in needed.items():
            if chem == "ORE": continue
            avail = leftovers[chem]
            req = max(0, qty - avail)
            leftovers[chem] = avail - (qty - req)
            if req == 0: continue
            prod, inputs = reactions[chem]
            factor = (req + prod - 1) // prod
            leftovers[chem] += prod * factor - req
            for iq, ic in inputs:
                newneeded[ic] = newneeded.get(ic, 0) + iq * factor
        needed = newneeded

def main():
    lines = open(sys.argv[1]).read().splitlines()
    reactions = {}
    for line in lines:
        lhs, rhs = line.split(" => ")
        out_qty, out_chem = rhs.split()
        inputs = [(int(q), c) for part in lhs.split(", ") for q, c in [part.split()]]
        reactions[out_chem] = (int(out_qty), inputs)
    part1 = ore_needed(reactions, 1)
    trillion = 10**12
    lo, hi = 1, trillion
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if ore_needed(reactions, mid) <= trillion:
            lo = mid
        else:
            hi = mid - 1
    print(part1, lo)

if __name__ == "__main__":
    main()