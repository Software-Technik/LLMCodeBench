import sys,re
pattern=re.compile(r"\d+")
s1=s2=0
with open(sys.argv[1]) as f:
    for block in f.read().strip().split("\n\n"):
        a0,a1,b0,b1,p0,p1=map(int,pattern.findall(block))
        D=a0*b1-a1*b0
        cost=1<<60
        if D:
            num=p0*b1-p1*b0
            if num%D==0:
                i=num//D
                j=(p1-a1*i)//b1
                if 0<=i<100 and 0<=j<100 and a0*i+b0*j==p0 and a1*i+b1*j==p1:
                    cost=3*i+j
        else:
            for i in range(100):
                rem=p0-a0*i
                if b0 and rem%b0==0:
                    j=rem//b0
                    if 0<=j<100 and a1*i+b1*j==p1:
                        c=3*i+j
                        if c<cost: cost=c
        if cost<1<<60: s1+=cost
        p0+=10000000000000
        p1+=10000000000000
        num=p0*b1-p1*b0
        i=num//D
        j=(p1-a1*i)//b1
        if i>=0 and j>=0 and a0*i+b0*j==p0 and a1*i+b1*j==p1:
            s2+=3*i+j
print(s1,s2)