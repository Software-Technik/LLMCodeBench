import sys
def run(a,n,v):
    m=a[:] ; m[1]=n ; m[2]=v ; i=0
    while m[i]!=99:
        x,y,z=m[i+1],m[i+2],m[i+3]
        m[z]=m[x]+m[y] if m[i]==1 else m[x]*m[y]
        i+=4
    return m[0]
data=list(map(int,open(sys.argv[1]).read().split(',')))
p1=run(data,12,2)
t=19690720
r=0
for n in range(100):
    for v in range(100):
        if run(data,n,v)==t:
            r=100*n+v
            break
    if r: break
sys.stdout.write(f"{p1} {r}")