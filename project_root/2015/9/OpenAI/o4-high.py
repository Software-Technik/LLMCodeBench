import sys
from itertools import permutations

locs=set(); edges=[]
with open(sys.argv[1]) as f:
    for line in f:
        parts=line.split()
        if not parts: continue
        a,_,b,_,d=parts
        locs.add(a); locs.add(b)
        edges.append((a,b,int(d)))
idx={loc:i for i,loc in enumerate(locs)}
n=len(locs)
mat=[[0]*n for _ in range(n)]
for a,b,d in edges:
    i,j=idx[a],idx[b]
    mat[i][j]=d; mat[j][i]=d
mn=10**18; mx=0
for perm in permutations(range(n)):
    s=0
    for u,v in zip(perm,perm[1:]):
        s+=mat[u][v]
    if s<mn: mn=s
    if s>mx: mx=s
print(mn)
print(mx)