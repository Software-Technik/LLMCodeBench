import sys
from collections import Counter

def parse_input(lines):
    to_bool=lambda c:c=='#'
    rules={}
    for line in lines:
        if '=>' not in line: continue
        src,dst=line.split('=>')
        src_rows=src.strip().split('/')
        dst_rows=dst.strip().split('/')
        src_g=tuple(tuple(to_bool(c) for c in row) for row in src_rows)
        dst_g=tuple(tuple(to_bool(c) for c in row) for row in dst_rows)
        g=src_g
        for _ in range(4):
            rules[g]=dst_g
            rules[tuple(reversed(g))]=dst_g
            g=tuple(zip(*g[::-1]))
    return rules

def find_next(grid,rules):
    n=len(grid)
    s=2 if n%2==0 else 3
    ns=n//s*(s+1)
    new=[[False]*ns for _ in range(ns)]
    for i in range(0,n,s):
        bi=i//s*(s+1)
        for j in range(0,n,s):
            block=tuple(grid[i+x][j:j+s] for x in range(s))
            nb=rules[block]
            bj=j//s*(s+1)
            for x,row in enumerate(nb):
                nr=new[bi+x]
                for y,val in enumerate(row):
                    nr[bj+y]=val
    return tuple(tuple(r) for r in new)

def pixels_on(grid):
    return sum(sum(row) for row in grid)

def part1(lines):
    rules=parse_input(lines)
    grid=tuple(tuple(c=='#' for c in row) for row in ".#./..#/###".split('/'))
    for _ in range(5):
        grid=find_next(grid,rules)
    return pixels_on(grid)

def part2(lines):
    rules=parse_input(lines)
    init=tuple(tuple(c=='#' for c in row) for row in ".#./..#/###".split('/'))
    def forward3(pat):
        g=pat
        for _ in range(3): g=find_next(g,rules)
        cnt=Counter()
        L=len(g)
        for i in range(0,L,3):
            for j in range(0,L,3):
                sq=tuple(g[i+x][j:j+3] for x in range(3))
                cnt[sq]+=1
        return cnt
    counts=Counter({init:1})
    cache={}
    for _ in range(6):
        nc=Counter()
        for pat,n in counts.items():
            sub=cache.get(pat)
            if sub is None:
                sub=forward3(pat); cache[pat]=sub
            for sp,cn in sub.items():
                nc[sp]+=n*cn
        counts=nc
    return sum(pixels_on(pat)*n for pat,n in counts.items())

if __name__=='__main__':
    lines=[l.strip() for l in open(sys.argv[1]) if l.strip()]
    print(part1(lines))
    print(part2(lines))