import sys

from collections import defaultdict, deque

input_path = sys.argv[1]
contains = {}
contained_by = defaultdict(list)

with open(input_path) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parent, rest = line.split(" bags contain ")
        rest = rest.rstrip('.')
        parts = rest.split(", ")
        d = {}
        for p in parts:
            if p.startswith("no other"):
                continue
            tokens = p.split()
            qty = int(tokens[0])
            name = tokens[1] + " " + tokens[2]
            d[name] = qty
            contained_by[name].append(parent)
        contains[parent] = d

# part 1
seen = set()
queue = deque(["shiny gold"])
while queue:
    cur = queue.popleft()
    for p in contained_by.get(cur, []):
        if p not in seen:
            seen.add(p)
            queue.append(p)
result1 = len(seen)

# part 2
from functools import lru_cache

@lru_cache(None)
def count_inside(bag):
    total = 0
    for child, qty in contains.get(bag, {}).items():
        total += qty * (1 + count_inside(child))
    return total

result2 = count_inside("shiny gold")

print(result1, result2)