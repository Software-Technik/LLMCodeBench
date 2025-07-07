import sys
from collections import Counter

def parse(lines):
    segs = []
    for line in lines:
        a,b,c,d = map(int, line.replace(' -> ', ',').split(','))
        segs.append((a,b,c,d))
    return segs

def part1(segs):
    cnt = Counter()
    for x1,y1,x2,y2 in segs:
        if x1==x2:
            step = 1 if y2>=y1 else -1
            for y in range(y1,y2+step,step):
                cnt[(x1,y)] += 1
        elif y1==y2:
            step = 1 if x2>=x1 else -1
            for x in range(x1,x2+step,step):
                cnt[(x,y1)] += 1
    return sum(1 for v in cnt.values() if v>1)

def part2(segs):
    cnt = Counter()
    for x1,y1,x2,y2 in segs:
        dx = 0 if x1==x2 else (1 if x2>x1 else -1)
        dy = 0 if y1==y2 else (1 if y2>y1 else -1)
        x,y = x1,y1
        while True:
            cnt[(x,y)] += 1
            if x==x2 and y==y2: break
            x += dx; y += dy
    return sum(1 for v in cnt.values() if v>1)

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f if line.strip()]
segs = parse(data)
print(part1(segs), part2(segs))