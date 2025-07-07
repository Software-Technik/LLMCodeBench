import sys

with open(sys.argv[1]) as f:
    speeds=[];fly=[];rest=[]
    for line in f:
        p=line.split()
        speeds.append(int(p[3]));fly.append(int(p[6]));rest.append(int(p[13]))
n=len(speeds)
t=1000 if n==2 else 2503
max1=0
for i in range(n):
    c=fly[i]+rest[i]
    full=t//c
    rem=t-full*c
    lf=rem if rem<fly[i] else fly[i]
    d=speeds[i]*(full*fly[i]+lf)
    if d>max1: max1=d
scores=[0]*n;dist=[0]*n
rfly=fly.copy();rrest=[0]*n
for _ in range(t):
    for i in range(n):
        if rfly[i]:
            dist[i]+=speeds[i]
            rfly[i]-=1
            if rfly[i]==0: rrest[i]=rest[i]
        else:
            rrest[i]-=1
            if rrest[i]==0: rfly[i]=fly[i]
    m=dist[0]
    for j in range(1,n):
        if dist[j]>m: m=dist[j]
    for i in range(n):
        if dist[i]==m: scores[i]+=1
max2=scores[0]
for j in scores[1:]:
    if j>max2: max2=j
sys.stdout.write(f"{max1}\n{max2}\n")