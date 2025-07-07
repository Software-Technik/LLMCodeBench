import sys
from collections import deque
f=open(sys.argv[1])
h=[]
sx=sy=tx=ty=0
A=ord('a');Z=ord('z')
for i,line in enumerate(f):
    line=line.strip()
    row=[]
    for j,ch in enumerate(line):
        if ch=='S':
            sx,sy=i,j;row.append(A)
        elif ch=='E':
            tx,ty=i,j;row.append(Z)
        else:
            row.append(ord(ch))
    h.append(row)
f.close()
n=len(h);m=len(h[0]) if n else 0
dist=[[-1]*m for _ in range(n)]
q=deque([(sx,sy)]);dist[sx][sy]=0
while q:
    i,j=q.popleft()
    if i==tx and j==ty:break
    v=h[i][j];d=dist[i][j]+1
    if i>0 and dist[i-1][j]<0 and h[i-1][j]-v<=1:dist[i-1][j]=d;q.append((i-1,j))
    if i+1<n and dist[i+1][j]<0 and h[i+1][j]-v<=1:dist[i+1][j]=d;q.append((i+1,j))
    if j>0 and dist[i][j-1]<0 and h[i][j-1]-v<=1:dist[i][j-1]=d;q.append((i,j-1))
    if j+1<m and dist[i][j+1]<0 and h[i][j+1]-v<=1:dist[i][j+1]=d;q.append((i,j+1))
res1=dist[tx][ty]
for ii in range(n):
    row=dist[ii]
    for jj in range(m):
        row[jj]=-1
q=deque([(tx,ty)]);dist[tx][ty]=0
res2=0
while q:
    i,j=q.popleft()
    if h[i][j]==A:
        res2=dist[i][j];break
    v=h[i][j];d=dist[i][j]+1
    if i>0 and dist[i-1][j]<0 and h[i-1][j]>=v-1:dist[i-1][j]=d;q.append((i-1,j))
    if i+1<n and dist[i+1][j]<0 and h[i+1][j]>=v-1:dist[i+1][j]=d;q.append((i+1,j))
    if j>0 and dist[i][j-1]<0 and h[i][j-1]>=v-1:dist[i][j-1]=d;q.append((i,j-1))
    if j+1<m and dist[i][j+1]<0 and h[i][j+1]>=v-1:dist[i][j+1]=d;q.append((i,j+1))
sys.stdout.write(f"{res1}\n{res2}\n")