import sys
from collections import Counter

input_path = sys.argv[1]
with open(input_path) as f:
    lines = [l.strip() for l in f if l.strip()]

dirs3 = [(dx,dy,dz) for dx in (-1,0,1) for dy in (-1,0,1) for dz in (-1,0,1) if not (dx==dy==dz==0)]
dirs4 = [(dx,dy,dz,dw) for dx in (-1,0,1) for dy in (-1,0,1) for dz in (-1,0,1) for dw in (-1,0,1) if not (dx==dy==dz==dw==0)]

active3 = {(x,y,0) for y,row in enumerate(lines) for x,c in enumerate(row) if c=='#'}
active4 = {(x,y,0,0) for y,row in enumerate(lines) for x,c in enumerate(row) if c=='#'}

def simulate(active, dirs, cycles):
    for _ in range(cycles):
        counts = Counter()
        for cell in active:
            for d in dirs:
                nbr = tuple(cell[i]+d[i] for i in range(len(d)))
                counts[nbr] += 1
        new_active = set()
        for cell, cnt in counts.items():
            if cnt==3 or (cnt==2 and cell in active):
                new_active.add(cell)
        active = new_active
    return active

res1 = len(simulate(active3, dirs3, 6))
res2 = len(simulate(active4, dirs4, 6))
print(res1, res2)