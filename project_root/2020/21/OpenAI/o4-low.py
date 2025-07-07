import sys

lines = open(sys.argv[1]).read().splitlines()
ing_lists = []
all_lists = []
for line in lines:
    parts = line[:-1].split(" (contains ")
    ing_lists.append(parts[0].split())
    all_lists.append(parts[1].split(", "))

cand = {}
for ings, alls in zip(ing_lists, all_lists):
    s = set(ings)
    for al in alls:
        if al in cand:
            cand[al] &= s
        else:
            cand[al] = s.copy()

res = {}
while len(res) < len(cand):
    for al, ss in cand.items():
        if len(ss) == 1 and al not in res:
            v = next(iter(ss))
            res[al] = v
            for other in cand:
                if other != al:
                    cand[other].discard(v)
            break

danger = set(res.values())
tot = 0
for ings in ing_lists:
    for ing in ings:
        if ing not in danger:
            tot += 1

canon = ",".join(res[al] for al in sorted(res))
print(tot, canon)