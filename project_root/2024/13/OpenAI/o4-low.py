import sys,re

pA=re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
pB=re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
pP=re.compile(r"Prize: X=(\d+), Y=(\d+)")

def solve(lines, offset):
    total=0
    for block in lines:
        l1,l2,l3=block.split("\n")
        a0,a1=map(int,pA.findall(l1)[0])
        b0,b1=map(int,pB.findall(l2)[0])
        p0,p1=map(int,pP.findall(l3)[0])
        p0+=offset; p1+=offset
        D=a0*b1 - a1*b0
        if D==0: continue
        iN = p0*b1 - p1*b0
        jN = -p0*a1 + p1*a0
        if iN % D or jN % D: continue
        i=iN//D; j=jN//D
        if i<0 or j<0: continue
        if offset==0 and (i>=100 or j>=100): continue
        total += 3*i + j
    return total

data=open(sys.argv[1]).read().strip().split("\n\n")
print(solve(data,0),solve(data,10**13))