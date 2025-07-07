import sys
mod=20201227
a,b=map(int,open(sys.argv[1]).read().split())
val=1
loop=0
while val!=a:
    val=val*7%mod
    loop+=1
secret=pow(b,loop,mod)
print(secret,secret)