import sys
dirs={'e':(2,0),'w':(-2,0),'se':(1,1),'ne':(1,-1),'nw':(-1,-1),'sw':(-1,1)}
argv=sys.argv
fpath=argv[1] if len(argv)>1 else ""
if "s" in argv: fpath="input_small.txt"
with open(fpath) as fp:
    lines=[l.strip() for l in fp if l.strip()]
blacks=set()
for line in lines:
    x=y=i=0
    while i<len(line):
        c=line[i]
        if c in ('e','w'):
            d=c; i+=1
        else:
            d=line[i:i+2]; i+=2
        dx,dy=dirs[d]
        x+=dx; y+=dy
    if (x,y) in blacks: blacks.remove((x,y))
    else: blacks.add((x,y))
res1=len(blacks)
nd=list(dirs.values())
for _ in range(100):
    cnt={}
    for x,y in blacks:
        for dx,dy in nd:
            n=(x+dx,y+dy)
            cnt[n]=cnt.get(n,0)+1
    new=set()
    for pos,c in cnt.items():
        if c==2 or (c==1 and pos in blacks):
            new.add(pos)
    blacks=new
res2=len(blacks)
print(res1,res2)