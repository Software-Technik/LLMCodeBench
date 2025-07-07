import sys

def main():
    path = sys.argv[1]
    if "s" in sys.argv:
        path = "input_small.txt"
    with open(path) as f:
        lines = f.read().splitlines()
    candidates = {}
    all_ings = []
    for line in lines:
        if not line: continue
        ings_part, alls_part = line[:-1].split(" (contains ")
        ings = ings_part.split()
        all_ings.extend(ings)
        for a in alls_part.split(", "):
            s = set(ings)
            if a in candidates:
                candidates[a] &= s
            else:
                candidates[a] = s
    changed = True
    while changed:
        changed = False
        singles = {next(iter(v)) for v in candidates.values() if len(v) == 1}
        for a, v in candidates.items():
            if len(v) > 1:
                newv = v - singles
                if newv != v:
                    candidates[a] = newv
                    changed = True
    dangerous = set().union(*candidates.values())
    tot = sum(1 for ing in all_ings if ing not in dangerous)
    canonical = ",".join(next(iter(candidates[a])) for a in sorted(candidates))
    print(tot, canonical)

if __name__ == "__main__":
    main()