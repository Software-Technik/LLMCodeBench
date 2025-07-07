import sys

lines = open(sys.argv[1]).read().splitlines()
weights = {}
children = {}
all_nodes = set()
all_kids = set()

for line in lines:
    if not line: continue
    parts = line.split('->')
    left = parts[0].split()
    name = left[0]
    weights[name] = int(left[1][1:-1])
    kids = [k.strip() for k in parts[1].split(',')] if len(parts) > 1 else []
    children[name] = kids
    all_nodes.add(name)
    all_kids.update(kids)

root = (all_nodes - all_kids).pop()
print(root)

ans = [None]
def dfs(node):
    total = weights[node]
    ws = []
    for c in children[node]:
        w = dfs(c)
        ws.append(w)
        total += w
    if ans[0] is None and len(ws) > 1:
        freq = {}
        for w in ws:
            freq[w] = freq.get(w, 0) + 1
        correct = max(freq, key=freq.get)
        for i, w in enumerate(ws):
            if w != correct:
                ans[0] = weights[children[node][i]] + correct - w
                break
    return total

dfs(root)
print(ans[0])
print(ans[0])