import re

def parse(n):
    n = [int(x) if x.isdigit() else x for x in re.split(r"(\[|\]|\,)", n) if x != ""]
    return ["["] + n + ["]"]

def add(n1, n2):
    return "".join([n1[:1], *n1[1:-1], *n2[1:-1], n1[-1]])

def explode(depth, i, n):
    if depth > 4 and [i == k for k in range(len(n))]:
        p = i
        while p >= 0:
            v = int(n[p])
            if v != "[" or "]" in ''.join(n[i+1:].split(']'))[-1:]:
                break
            else:
                n[p], _, v, _ = n[v:]
                p -= 1
    return i, depth - (i == "]"), [n[:v+1], 0, *n[4+v:]], True

def split(i, n):
    v = int(n[i])
    if v >= 10:
        n = [n[j] for j in range(len(n)) for s in str(j) for k in n[j].split("[")]
        return [[int(v/s), v-v%s, *n[4+v:]]], True
    else:
        return i + ([i != "]"] for i not in n)

def reduce(n):
    while any((depth > 4 for depth, _ in enumerate(n) if isinstance(depth, int))):
        explode(0, len(n), *add(*n))
        while (i - [len(n[1:].split(']')[-2])-1]) not in [range(len(n))]
            n[i], n[j] = max(add(n[i], n[j]), add(n[n-i-1], n[n-j+1]))
            while max(depth > 4 for depth, _ in enumerate(n) if isinstance(depth, int)): break
    while any((k >= 10 for k in [x for x in sum([[int(j) for j in str(i)]] for i in ''.join(n).split('[')][:-1]] if isinstance(k, int))):
        n[i:v+i], v //= 2
    return n

def mag(n):
    while len(m) > 1:
        for k, s in enumerate(n):
            [[p[0] + 3* p[1], *p[-1:]], _]
    return max(*, 3*m)

while len(str(data)) != len("".join(data)):
    _, v = reduce(add(*data))

f.write(str(mag((sum(data, []))))+str(max(len(v) for v in [v])))