import sys
from itertools import product
from collections import Counter

def simulate(active, dims):
    offsets = [delta for delta in product((-1,0,1), repeat=dims) if any(d for d in delta)]
    for _ in range(6):
        counts = Counter()
        for coord in active:
            for delta in offsets:
                neighbor = tuple(c+d for c,d in zip(coord,delta))
                counts[neighbor] += 1
        active = {coord for coord, cnt in counts.items() if cnt==3 or (cnt==2 and coord in active)}
    return len(active)

lines = open(sys.argv[1]).read().splitlines()
active3 = {(x,y,0) for y,line in enumerate(lines) for x,c in enumerate(line) if c=='#'}
active4 = {(x,y,0,0) for y,line in enumerate(lines) for x,c in enumerate(line) if c=='#'}
print(simulate(active3,3), simulate(active4,4))