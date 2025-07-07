import sys,math
data=[]
with open(sys.argv[1]) as f:
    for l in f:
        if l.strip():
            parts=l.strip().split(', ')
            p=tuple(map(int,parts[0][3:-1].split(',')))
            v=tuple(map(int,parts[1][3:-1].split(',')))
            a=tuple(map(int,parts[2][3:-1].split(',')))
            data.append((p,v,a))
def mag2(a):return a[0]*a[0]+a[1]*a[1]+a[2]*a[2]
print(min(range(len(data)),key=lambda i:mag2(data[i][2])))
def solve_dim(p,v,a):
    b=2*v+a; c=2*p
    if a==0:
        if b==0:
            return None if c==0 else set()
        if -c%b==0:
            t=-c//b
            return {t} if t>0 else set()
        return set()
    D=b*b-4*a*c
    if D<0:return set()
    d0=math.isqrt(D)
    if d0*d0!=D:return set()
    res=set();den=2*a
    for num in (-b+d0,-b-d0):
        if den!=0 and num%den==0:
            t=num//den
            if t>0:res.add(t)
    return res
n=len(data)
coll={}
for i in range(n):
    p1,v1,a1=data[i]
    for j in range(i+1,n):
        p2,v2,a2=data[j]
        ts=None
        for d in range(3):
            s=solve_dim(p1[d]-p2[d],v1[d]-v2[d],a1[d]-a2[d])
            if s is not None:
                if not s:
                    ts=set()
                    break
                ts=s if ts is None else ts&s
                if not ts:break
        if ts:
            t=min(ts)
            coll.setdefault(t,[]).append((i,j))
dead=set()
for t in sorted(coll):
    hit=set()
    for i,j in coll[t]:
        if i not in dead and j not in dead:
            hit.add(i);hit.add(j)
    dead |= hit
print(n-len(dead))