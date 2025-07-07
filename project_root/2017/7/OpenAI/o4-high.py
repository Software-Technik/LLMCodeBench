import sys
from collections import Counter

def main():
    with open(sys.argv[1]) as f:
        lines = [l.strip() for l in f if l.strip()]
    weights = {}
    children = {}
    all_nodes = set()
    all_kids = set()
    for line in lines:
        parts = line.split('->')
        left = parts[0].split()
        name = left[0]
        wt = int(left[1].strip('()'))
        kids = [k.strip() for k in parts[1].split(',')] if len(parts) > 1 else []
        weights[name] = wt
        children[name] = kids
        all_nodes.add(name)
        all_kids.update(kids)
    root = (all_nodes - all_kids).pop()
    print(root)
    corrected = None
    def dfs(u):
        nonlocal corrected
        total = weights[u]
        subs = []
        for v in children.get(u, ()):
            w = dfs(v)
            subs.append(w)
            total += w
        if corrected is None and subs:
            cnt = Counter(subs)
            if len(cnt) > 1:
                common, _ = cnt.most_common(1)[0]
                wrong = next(x for x in cnt if x != common)
                idx = subs.index(wrong)
                node = children[u][idx]
                diff = common - wrong
                corrected = weights[node] + diff
        return total
    dfs(root)
    print(corrected)
    print(corrected)

if __name__ == '__main__':
    main()