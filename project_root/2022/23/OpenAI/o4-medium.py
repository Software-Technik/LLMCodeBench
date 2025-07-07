import sys
from collections import defaultdict

neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
dirs = [((-1,0),[(-1,-1),(-1,0),(-1,1)]),
        ((1,0),[(1,-1),(1,0),(1,1)]),
        ((0,-1),[(-1,-1),(0,-1),(1,-1)]),
        ((0,1),[(-1,1),(0,1),(1,1)])]

def parse(data):
    elves = set()
    for r,line in enumerate(data):
        for c,ch in enumerate(line):
            if ch=='#': elves.add((r,c))
    return elves

def part1(data):
    elves = parse(data)
    order = dirs.copy()
    for _ in range(10):
        proposals = {}
        dest_count = defaultdict(int)
        for e in elves:
            if not any((e[0]+dy,e[1]+dx) in elves for dy,dx in neighbors):
                continue
            for d,checks in order:
                if all((e[0]+dy,e[1]+dx) not in elves for dy,dx in checks):
                    ne=(e[0]+d[0],e[1]+d[1])
                    proposals[e]=ne
                    dest_count[ne]+=1
                    break
        new_elves=set()
        for e in elves:
            if e in proposals and dest_count[proposals[e]]==1:
                new_elves.add(proposals[e])
            else:
                new_elves.add(e)
        elves=new_elves
        order=order[1:]+order[:1]
    rs=[r for r,c in elves]; cs=[c for r,c in elves]
    min_r,min_c,max_r,max_c=min(rs),min(cs),max(rs),max(cs)
    return (max_r-min_r+1)*(max_c-min_c+1)-len(elves)

def part2(data):
    elves = parse(data)
    order = dirs.copy()
    round=1
    while True:
        proposals = {}
        dest_count = defaultdict(int)
        for e in elves:
            if not any((e[0]+dy,e[1]+dx) in elves for dy,dx in neighbors):
                continue
            for d,checks in order:
                if all((e[0]+dy,e[1]+dx) not in elves for dy,dx in checks):
                    ne=(e[0]+d[0],e[1]+d[1])
                    proposals[e]=ne
                    dest_count[ne]+=1
                    break
        new_elves=set()
        for e in elves:
            if e in proposals and dest_count[proposals[e]]==1:
                new_elves.add(proposals[e])
            else:
                new_elves.add(e)
        if new_elves==elves:
            return round
        elves=new_elves
        order=order[1:]+order[:1]
        round+=1

data = [line.strip() for line in open(sys.argv[1])]
print(part1(data))
print(part2(data))