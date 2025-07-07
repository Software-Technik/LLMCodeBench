import sys
f=open(sys.argv[1])
init=f.readline().split()[2]
f.readline()
rules=[0]*32
for line in f:
    parts=line.split()
    if len(parts)==3 and parts[2]=='#':
        p=parts[0]
        rules[(p[0]=='#')<<4|(p[1]=='#')<<3|(p[2]=='#')<<2|(p[3]=='#')<<1|(p[4]=='#')]=1
f.close()
initial={i for i,c in enumerate(init) if c=='#'}
low0=min(initial)
high0=max(initial)
s=initial.copy(); low,high=low0,high0
for _ in range(20):
    new=set(); nl=10**9; nh=-10**9
    for i in range(low-2,high+3):
        pat=((i-2 in s)<<4)|((i-1 in s)<<3)|((i in s)<<2)|((i+1 in s)<<1)|(i+2 in s)
        if rules[pat]:
            new.add(i)
            if i<nl: nl=i
            if i>nh: nh=i
    s,low,high=new,nl,nh
part1=sum(s)
s=initial.copy(); low,high=low0,high0
last_score=sum(s); last_diff=0; diffs=[]
for cycle in range(1,500):
    new=set(); nl=10**9; nh=-10**9
    for i in range(low-2,high+3):
        pat=((i-2 in s)<<4)|((i-1 in s)<<3)|((i in s)<<2)|((i+1 in s)<<1)|(i+2 in s)
        if rules[pat]:
            new.add(i)
            if i<nl: nl=i
            if i>nh: nh=i
    s,low,high=new,nl,nh
    score=sum(s)
    diff=score-last_score; last_score=score
    if diff==last_diff or diffs: diffs.append((diff,score,cycle))
    last_diff=diff
a,sc,c=diffs[-1]; b=sc-c*a
part2=a*50000000000+b
sys.stdout.write(f"{part1} {part2}")