import sys
from collections import deque, Counter
def part1(data):
    elves = {(i,j) for i,line in enumerate(data) for j,c in enumerate(line) if c=="#"}
    directions = deque([
        ((-1,0), [(-1,-1),(-1,0),(-1,1)]),
        ((1,0), [(1,-1),(1,0),(1,1)]),
        ((0,-1), [(-1,-1),(0,-1),(1,-1)]),
        ((0,1), [(-1,1),(0,1),(1,1)]),
    ])
    neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for _ in range(10):
        proposals = {}
        counts = Counter()
        for elf in elves:
            if not any((elf[0]+dy,elf[1]+dx) in elves for dy,dx in neighbors):
                continue
            for move,checks in directions:
                if not any((elf[0]+dy,elf[1]+dx) in elves for dy,dx in checks):
                    dest = (elf[0]+move[0],elf[1]+move[1])
                    proposals[elf]=dest
                    counts[dest]+=1
                    break
        new_elves=set()
        for elf in elves:
            dest=proposals.get(elf)
            if dest and counts[dest]==1:
                new_elves.add(dest)
            else:
                new_elves.add(elf)
        elves=new_elves
        directions.rotate(-1)
    ys=[p[0] for p in elves]; xs=[p[1] for p in elves]
    return (max(ys)-min(ys)+1)*(max(xs)-min(xs)+1)-len(elves)
def part2(data):
    elves = {(i,j) for i,line in enumerate(data) for j,c in enumerate(line) if c=="#"}
    directions = deque([
        ((-1,0), [(-1,-1),(-1,0),(-1,1)]),
        ((1,0), [(1,-1),(1,0),(1,1)]),
        ((0,-1), [(-1,-1),(0,-1),(1,-1)]),
        ((0,1), [(-1,1),(0,1),(1,1)]),
    ])
    neighbors = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    round=1
    while True:
        proposals = {}
        counts = Counter()
        for elf in elves:
            if not any((elf[0]+dy,elf[1]+dx) in elves for dy,dx in neighbors):
                continue
            for move,checks in directions:
                if not any((elf[0]+dy,elf[1]+dx) in elves for dy,dx in checks):
                    dest = (elf[0]+move[0],elf[1]+move[1])
                    proposals[elf]=dest
                    counts[dest]+=1
                    break
        moved=False
        new_elves=set()
        for elf in elves:
            dest=proposals.get(elf)
            if dest and counts[dest]==1:
                new_elves.add(dest)
                moved=True
            else:
                new_elves.add(elf)
        if not moved:
            return round
        elves=new_elves
        directions.rotate(-1)
        round+=1
data=[l.strip() for l in open(sys.argv[1])]
print(part1(data))
print(part2(data))