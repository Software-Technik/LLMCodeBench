import sys
with open(sys.argv[1]) as f:
    edges=[];mx=0
    for line in f:
        s=line.strip()
        if not s: continue
        a,b=s.split(' <-> ')
        i=int(a);nbrs=[int(x) for x in b.split(', ')]
        edges.append((i,nbrs))
        if i>mx: mx=i
        for x in nbrs:
            if x>mx: mx=x
n=mx+1
g=[[] for _ in range(n)]
for i,nbrs in edges: g[i]=nbrs
del edges
vis=[False]*n
st=[0];cnt=0
while st:
    u=st.pop()
    if not vis[u]:
        vis[u]=True;cnt+=1;st.extend(g[u])
groups=1
for i in range(n):
    if not vis[i]:
        st=[i]
        while st:
            u=st.pop()
            if not vis[u]:
                vis[u]=True;st.extend(g[u])
        groups+=1
sys.stdout.write(f"{cnt}\n{groups}\n")