import sys
with open(sys.argv[1]) as f:
    points=[tuple(map(int,line.split(','))) for line in f if line.strip()]
n=len(points)
parent=list(range(n))
rank=[0]*n
def find(i):
    while parent[i]!=i:
        parent[i]=parent[parent[i]]
        i=parent[i]
    return i
def union(i,j):
    ri,rj=find(i),find(j)
    if ri==rj: return
    if rank[ri]<rank[rj]:
        parent[ri]=rj
    else:
        parent[rj]=ri
        if rank[ri]==rank[rj]:
            rank[ri]+=1
for i in range(n):
    pi=points[i]
    for j in range(i+1,n):
        s=0
        for a,b in zip(pi,points[j]):
            s+=abs(a-b)
            if s>3: break
        if s<=3:
            union(i,j)
roots={find(i) for i in range(n)}
sys.stdout.write(str(len(roots)))