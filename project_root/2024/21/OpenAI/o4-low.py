import sys
from functools import lru_cache
from itertools import combinations

numeric_keypad = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
    "0": (3, 1), "A": (3, 2),
}
direction_keypad = {
    "^": (0, 1), "A": (0, 2), "<": (1, 0),
    "v": (1, 1), ">": (1, 2),
}
dd = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}

def get_combos(ca, a, cb, b):
    for idxs in combinations(range(a+b), a):
        res = [cb]*(a+b)
        for i in idxs: res[i] = ca
        yield "".join(res)

@lru_cache(None)
def get_ways(a, b, kf):
    kp = direction_keypad if kf else numeric_keypad
    ci, cj = kp[a]; ni, nj = kp[b]
    di, dj = ni-ci, nj-cj
    m = []
    if di>0: m.extend(("v", di))
    else: m.extend(("^", -di))
    if dj>0: m.extend((">", dj))
    else: m.extend(("<", -dj))
    raw = set("".join(x)+"A" for x in get_combos(m[0], m[1], m[2], m[3]))
    res = []
    for seq in raw:
        i,j = ci,cj; ok = True
        for c in seq[:-1]:
            di,dj = dd[c]; i+=di; j+=dj
            if (i,j) not in kp.values():
                ok = False; break
        if ok: res.append(seq)
    return res

@lru_cache(None)
def get_cost(a, b, kf, d):
    if d==0 and kf:
        return min(map(len, get_ways(a,b,True)))
    best = 1<<60
    for seq in get_ways(a,b,kf):
        seq = "A"+seq
        c = 0
        for x,y in zip(seq, seq[1:]):
            c += get_cost(x,y,True,d-1)
        if c<best: best=c
    return best

def get_code_cost(code, depth):
    s = "A"+code
    c=0
    for x,y in zip(s, s[1:]):
        c += get_cost(x,y,False,depth)
    return c

lines = open(sys.argv[1]).read().splitlines()
p1 = sum(get_code_cost(l,2)*int(l[:-1]) for l in lines)
p2 = sum(get_code_cost(l,25)*int(l[:-1]) for l in lines)
print(p1, p2)