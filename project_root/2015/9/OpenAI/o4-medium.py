import sys
from itertools import permutations

lines = open(sys.argv[1]).read().splitlines()
dist = {}
locs = set()
for line in lines:
    a,_,b,_,d = line.split()
    d = int(d)
    locs.add(a); locs.add(b)
    dist[a,b] = d; dist[b,a] = d
locs = list(locs)
min_d = float('inf')
max_d = 0
for p in permutations(locs):
    s = 0
    for i in range(len(p)-1):
        s += dist[p[i],p[i+1]]
    if s < min_d: min_d = s
    if s > max_d: max_d = s
sys.stdout.write(f"{min_d}\n{max_d}\n")