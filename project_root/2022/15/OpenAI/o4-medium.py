import sys,re
data=open(sys.argv[1]).read().splitlines()
coords=[tuple(map(int,re.findall(r'-?\d+',line))) for line in data]
sensors=[(sx,sy,abs(sx-bx)+abs(sy-by)) for sx,sy,bx,by in coords]
sample=coords[0]==(2,18,-2,15)
ty1=10 if sample else 2000000
ints=[]
for sx,sy,d in sensors:
    dy=abs(ty1-sy);dx=d-dy
    if dx>=0:ints.append((sx-dx,sx+dx))
ints.sort()
merged=[]
for s,e in ints:
    if not merged or s>merged[-1][1]+1:merged.append([s,e])
    else:
        if e>merged[-1][1]:merged[-1][1]=e
total=0
for s,e in merged:total+=e-s+1
sens_on_row={sx for sx,sy,_,_ in [(sx,sy,bx,by) for sx,sy,bx,by in coords] if sy==ty1}
beac_on_row={bx for sx,sy,bx,by in coords if by==ty1}
res1=total
for x in sens_on_row:
    for s,e in merged:
        if s<=x<=e:
            res1-=1;break
for x in beac_on_row:
    for s,e in merged:
        if s<=x<=e:
            res1-=1;break
limit=20 if sample else 4000000
c1=[];c2=[]
for sx,sy,d in sensors:
    dd=d+1
    c1+= [sy-sx+dd,sy-sx-dd]
    c2+= [sy+sx+dd,sy+sx-dd]
res2=0
for a in c1:
    for b in c2:
        if (b-a)&1:continue
        x=(b-a)//2; y=(a+b)//2
        if x<0 or x>limit or y<0 or y>limit:continue
        ok=True
        for sx,sy,d in sensors:
            if abs(x-sx)+abs(y-sy)<=d:
                ok=False;break
        if ok:
            res2=x*4000000+y
            break
    if res2:break
print(res1)
print(res2)