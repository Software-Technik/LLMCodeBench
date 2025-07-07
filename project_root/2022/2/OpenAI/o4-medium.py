import sys
d1={'A':0,'B':1,'C':2}
p1m={'X':0,'Y':1,'Z':2}
p2r={'X':0,'Y':3,'Z':6}
s1=s2=0
with open(sys.argv[1]) as f:
    for l in f:
        a,b=l.split()
        x=d1[a]; y=p1m[b]; diff=(y-x)%3
        if diff==0: s1+=y+1+3
        elif diff==1: s1+=y+1+6
        else: s1+=y+1
        r=p2r[b]
        if r==3: y2=x
        elif r==6: y2=(x+1)%3
        else: y2=(x+2)%3
        s2+=y2+1+r
print(s1)
print(s2)