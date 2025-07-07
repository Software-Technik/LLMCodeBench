import sys
f=sys.argv[1]
with open(f) as file:
    d=file.readline().split()
r=int(d[-3][:-1]); c=int(d[-1][:-1])
r1=(r*(r-1))//2+1
rc=r1+(((r+1)+(r+1+c-2))*(c-1))//2
mod=33554393; m=252533
s=20151125*pow(m, rc-1, mod)%mod
sys.stdout.write(f"{s}\n")