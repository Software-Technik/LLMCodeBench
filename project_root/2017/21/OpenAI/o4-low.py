import sys
from collections import Counter

def to_bool_row(s):
    return tuple(c=='#' for c in s)

def parse_input(lines):
    rules={}
    for line in lines:
        if '=>' not in line: continue
        src,dst=line.split(' => ')
        src=tuple(tuple(r) for r in (to_bool_row(r) for r in src.split('/')))
        dst=tuple(to_bool_row(r) for r in dst.split('/'))
        g=src
        for _ in range(4):
            rules[g]=dst
            fg=tuple(reversed(g))
            rules[fg]=dst
            g=tuple(zip(*g[::-1]))
    return rules

def find_next(grid,rules):
    n=len(grid)
    s=2 if n%2==0 else 3
    ns=n//s*(s+1)
    ng=[[False]*ns for _ in range(ns)]
    for i in range(0,n,s):
        for j in range(0,n,s):
            sq=tuple(tuple(grid[i+x][j+y] for y in range(s)) for x in range(s))
            ed=rules[sq]
            bi=i//s*(s+1); bj=j//s*(s+1)
            for x,row in enumerate(ed):
                for y,v in enumerate(row):
                    ng[bi+x][bj+y]=v
    return tuple(tuple(r) for r in ng)

def pixels_on(grid):
    return sum(sum(row) for row in grid)

def part1(data):
    rules=parse_input(data)
    grid=tuple(to_bool_row(r) for r in ".#./..#/###".split("/"))
    for _ in range(5): grid=find_next(grid,rules)
    return pixels_on(grid)

def fast_count(grid,rules,steps):
    def forward3(pat):
        g=pat
        for _ in range(3): g=find_next(g,rules)
        c=Counter()
        n=len(g)
        for i in range(0,n,3):
            for j in range(0,n,3):
                sq=tuple(tuple(g[i+x][j+y] for y in range(3)) for x in range(3))
                c[sq]+=1
        return c
    counts=Counter({grid:1})
    mc={}
    for _ in range(steps//3):
        nc=Counter()
        for pat,n in counts.items():
            if pat not in mc: mc[pat]=forward3(pat)
            for sp,sn in mc[pat].items():
                nc[sp]+=n*sn
        counts=nc
    return sum(pixels_on(pat)*n for pat,n in counts.items())

def part2(data):
    rules=parse_input(data)
    grid=tuple(to_bool_row(r) for r in ".#./..#/###".split("/"))
    return fast_count(grid,rules,18)

data=[l.strip() for l in open(sys.argv[1]) if l.strip()]
print(part1(data))
print(part2(data))