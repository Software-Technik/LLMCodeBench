import sys
mod=20201227
a,b=map(int,open(sys.argv[1]).read().split())
dl=cl=0
v=1
for i in range(1,mod):
    v=v*7%mod
    if v==a: dl=i
    if v==b: cl=i
    if dl and cl: break
print(pow(a,cl,mod),pow(b,dl,mod))