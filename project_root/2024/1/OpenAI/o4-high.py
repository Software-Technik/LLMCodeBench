import sys
from collections import defaultdict

a=[]; b=[]; counts=defaultdict(int)
with open(sys.argv[1]) as f:
    for line in f:
        s=line.strip()
        if not s: continue
        x,y=map(int, s.split("   "))
        a.append(x); b.append(y)
        counts[y]+=1
a.sort(); b.sort()
print(sum(abs(x-y) for x,y in zip(a,b)), sum(x*counts[x] for x in a))