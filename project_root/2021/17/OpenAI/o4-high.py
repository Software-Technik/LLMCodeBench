import sys,re
with open(sys.argv[1]) as f:
    for line in f:
        if line.strip():
            break
x1,x2,y1,y2=map(int,re.findall(r"-?\d+",line))
times_x={}
for vx in range(1,x2+1):
    x=0;v=vx;t=0;h=set()
    while x<=x2 and v>0:
        t+=1; x+=v; v-=1
        if x1<=x<=x2: h.add(t)
    stall=t if v==0 and x1<=x<=x2 else None
    if h or stall is not None: times_x[vx]=(h,stall)
times_y={}
vr=range(y1,-y1) if y1<0 else range(y1,y2+1)
for vy in vr:
    y=0;v=vy;t=0;h=set()
    while y>=y1:
        t+=1; y+=v; v-=1
        if y1<=y<=y2: h.add(t)
    if h: times_y[vy]=(h,max(h))
pairs=set()
for vx,(hx,stall) in times_x.items():
    for vy,(hy,hy_max) in times_y.items():
        if hx&hy or (stall is not None and hy_max>=stall):
            pairs.add((vx,vy))
c=len(pairs)
b=max(v*(v+1)//2 for _,v in pairs) if pairs else 0
sys.stdout.write(f"{b} {c}")