import sys
from collections import defaultdict, Counter
f = open(sys.argv[1])
weights = {}
children = defaultdict(list)
all_nodes = set()
all_kids = set()
for line in f:
    parts = line.split()
    if not parts: continue
    name = parts[0]
    weight = int(parts[1].strip("()"))
    kids = [p.strip(",") for p in parts[3:]]
    weights[name] = weight
    children[name] = kids
    all_nodes.add(name)
    all_kids.update(kids)
root = (all_nodes - all_kids).pop()
print(root)
imbalance = [None]
def dfs(node):
    wts = []
    for c in children[node]:
        wts.append((c, dfs(c)))
    sums = [w for _,w in wts]
    if imbalance[0] is None and len(set(sums))>1:
        cnt = Counter(sums)
        correct = cnt.most_common(1)[0][0]
        for c, w in wts:
            if w != correct:
                imbalance[0] = weights[c] + (correct - w)
                break
    return weights[node] + sum(sums)
dfs(root)
print(imbalance[0])