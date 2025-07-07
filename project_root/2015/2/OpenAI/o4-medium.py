import sys
tot1=tot2=0
with open(sys.argv[1]) as f:
    for line in f:
        l,w,h=map(int,line.split('x'))
        lw=l*w; wh=w*h; hl=h*l
        m=lw if lw<wh else wh
        if hl<m: m=hl
        tot1+=2*(lw+wh+hl)+m
        a,b,c=l,w,h
        if a>b: a,b=b,a
        if b>c: b,c=c,b
        if a>b: a,b=b,a
        tot2+=2*(a+b)+lw*h
print(tot1)
print(tot2)