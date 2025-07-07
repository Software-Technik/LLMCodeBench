import sys
from functools import lru_cache
from itertools import combinations

numeric_pad = {'7':(0,0),'8':(0,1),'9':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),'1':(2,0),'2':(2,1),'3':(2,2),'0':(3,1),'A':(3,2)}
direction_pad = {'^':(0,1),'A':(0,2),'<':(1,0),'v':(1,1),'>':(1,2)}
numeric_coords = set(numeric_pad.values())
direction_coords = set(direction_pad.values())
dd = {'>':(0,1),'v':(1,0),'<':(0,-1),'^':(-1,0)}

def get_combos(ca,a,cb,b):
    for idxs in combinations(range(a+b), r=a):
        res = [cb]*(a+b)
        for i in idxs:
            res[i] = ca
        yield ''.join(res)

@lru_cache(None)
def generate_moves(pad_type, a, b):
    pad = direction_pad if pad_type else numeric_pad
    coords = direction_coords if pad_type else numeric_coords
    ci,cj = pad[a]
    ni,nj = pad[b]
    di = ni-ci; dj = nj-cj
    ac = abs(di); bc = abs(dj)
    vch = 'v' if di>0 else '^' if di<0 else None
    hch = '>' if dj>0 else '<' if dj<0 else None
    if ac==0 and bc==0:
        return ['A']
    v0 = vch if ac>0 else hch
    h0 = hch if bc>0 else vch
    res = []
    for seq in get_combos(v0, ac, h0, bc):
        ii,jj = ci,cj
        ok = True
        for c in seq:
            di2,dj2 = dd[c]
            ii += di2; jj += dj2
            if (ii,jj) not in coords:
                ok = False; break
        if ok:
            res.append(seq+'A')
    return res

@lru_cache(None)
def get_cost(a, b, pad_type, depth):
    if depth == 0:
        return len(generate_moves(True, a, b)[0])
    combos = generate_moves(pad_type, a, b)
    best = float('inf')
    for seq in combos:
        cost = 0
        prev = 'A'
        for c in seq:
            cost += get_cost(prev, c, True, depth-1)
            prev = c
        if cost < best:
            best = cost
    return best

def get_code_cost(code, depth):
    cost = 0
    prev = 'A'
    for c in code:
        cost += get_cost(prev, c, False, depth)
        prev = c
    return cost

def main():
    lines = open(sys.argv[1]).read().strip().splitlines()
    ans1 = ans2 = 0
    for line in lines:
        n = int(line[:-1])
        ans1 += get_code_cost(line, 2) * n
        ans2 += get_code_cost(line, 25) * n
    print(ans1, ans2)

if __name__ == '__main__':
    main()