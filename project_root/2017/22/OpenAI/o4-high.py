import sys
lines=open(sys.argv[1]).read().splitlines()
n=len(lines); m=len(lines[0])
sx=n//2; sy=m//2
initial={(i,j) for i,line in enumerate(lines) for j,c in enumerate(line) if c=='#'}
dxs=(-1,0,1,0); dys=(0,1,0,-1)
infected=set(initial)
x=sx; y=sy; d=0; cnt=0
has=infected.__contains__; add=infected.add; rem=infected.remove
for _ in range(10000):
    pos=(x,y)
    if has(pos):
        d=(d+1)&3; rem(pos)
    else:
        d=(d-1)&3; add(pos); cnt+=1
    x+=dxs[d]; y+=dys[d]
print(cnt)
grid={pos:2 for pos in initial}
x=sx; y=sy; d=0; cnt=0
get=grid.get; pop=grid.pop; setitem=grid.__setitem__
for _ in range(10000000):
    pos=(x,y)
    st=get(pos,0)
    if st==0: d=(d-1)&3
    elif st==2: d=(d+1)&3
    elif st==3: d=(d+2)&3
    ns=(st+1)&3
    if ns: setitem(pos,ns)
    else: pop(pos)
    if ns==2: cnt+=1
    x+=dxs[d]; y+=dys[d]
print(cnt)