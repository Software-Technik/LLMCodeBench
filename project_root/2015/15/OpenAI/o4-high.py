import sys
props=[]
for line in open(sys.argv[1]):
    line=line.strip()
    if not line: continue
    t=line.replace(':','').replace(',','').split()
    props.append((int(t[2]),int(t[4]),int(t[6]),int(t[8]),int(t[10])))
n=len(props)
max1=0
max2=0
if n==4:
    c0,d0,f0,t0,ca0=props[0]
    c1,d1,f1,t1,ca1=props[1]
    c2,d2,f2,t2,ca2=props[2]
    c3,d3,f3,t3,ca3=props[3]
    for a in range(101):
        for b in range(101-a):
            for c in range(101-a-b):
                d=100-a-b-c
                s0=a*c0+b*c1+c*c2+d*c3
                s1=a*d0+b*d1+c*d2+d*d3
                s2=a*f0+b*f1+c*f2+d*f3
                s3=a*t0+b*t1+c*t2+d*t3
                if s0<0: s0=0
                if s1<0: s1=0
                if s2<0: s2=0
                if s3<0: s3=0
                score=s0*s1*s2*s3
                cal=a*ca0+b*ca1+c*ca2+d*ca3
                if score>max1: max1=score
                if cal==500 and score>max2: max2=score
else:
    def dfs(i,rem,s0,s1,s2,s3,cal):
        global max1,max2
        if i==n-1:
            v=rem
            c,d,f,t,ca=props[i]
            s0n=s0+v*c
            s1n=s1+v*d
            s2n=s2+v*f
            s3n=s3+v*t
            caln=cal+v*ca
            if s0n<0: s0n=0
            if s1n<0: s1n=0
            if s2n<0: s2n=0
            if s3n<0: s3n=0
            score=s0n*s1n*s2n*s3n
            if score>max1: max1=score
            if caln==500 and score>max2: max2=score
        else:
            c,d,f,t,ca=props[i]
            for v in range(rem+1):
                dfs(i+1,rem-v,s0+v*c,s1+v*d,s2+v*f,s3+v*t,cal+v*ca)
    dfs(0,100,0,0,0,0,0)
sys.stdout.write(f"{max1}\n{max2}\n")