import sys

def parse_snailfish(s):
    tokens=[];num=''
    for c in s:
        if c.isdigit():
            num+=c
        else:
            if num:
                tokens.append(int(num));num=''
            if c in '[]':
                tokens.append(c)
    if num:
        tokens.append(int(num))
    return tokens

def add(a,b):
    return ['[']+a+b+[']']

def explode(n):
    depth=0
    for i,s in enumerate(n):
        if s=='[': depth+=1
        elif s==']': depth-=1
        if depth>4 and s=='[' and isinstance(n[i+1],int) and isinstance(n[i+2],int) and n[i+3]==']':
            for j in range(i-1,-1,-1):
                if isinstance(n[j],int):
                    n[j]+=n[i+1];break
            for j in range(i+4,len(n)):
                if isinstance(n[j],int):
                    n[j]+=n[i+2];break
            return n[:i]+[0]+n[i+4:],True
    return n,False

def split(n):
    for i,s in enumerate(n):
        if isinstance(s,int) and s>=10:
            a=s//2; b=s-a
            return n[:i]+['[',a,b,']']+n[i+1:],True
    return n,False

def reduce(n):
    while True:
        n,ok=explode(n)
        if ok: continue
        n,ok=split(n)
        if not ok: break
    return n

def magnitude(n):
    while len(n)>1:
        for i,s in enumerate(n):
            if s=='[' and isinstance(n[i+1],int) and isinstance(n[i+2],int) and n[i+3]==']':
                val=3*n[i+1]+2*n[i+2]
                n=n[:i]+[val]+n[i+4:]
                break
    return n[0]

data=[line.strip() for line in open(sys.argv[1])]
parsed=[parse_snailfish(line) for line in data]

m=parsed[0][:]
for p in parsed[1:]:
    m=reduce(add(m,p[:]))
part1=magnitude(m)

maxm=0
for i in range(len(parsed)):
    for j in range(len(parsed)):
        if i!=j:
            a=add(parsed[i][:],parsed[j][:])
            maxm=max(maxm,magnitude(reduce(a)))
part2=maxm

print(part1,part2)