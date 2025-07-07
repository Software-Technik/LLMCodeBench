import sys

def parse(s):
    res=[]
    d=0
    i=0
    while i<len(s):
        c=s[i]
        if c=='[':
            d+=1; i+=1
        elif c==']':
            d-=1; i+=1
        elif c==',':
            i+=1
        else:
            j=i
            while j<len(s) and s[j].isdigit(): j+=1
            res.append([int(s[i:j]),d])
            i=j
    return res

def add(a,b):
    return [[v,d+1] for v,d in a]+[[v,d+1] for v,d in b]

def reduce_sf(res):
    while True:
        exploded=False
        for i in range(len(res)-1):
            if res[i][1]>4 and res[i][1]==res[i+1][1]:
                if i>0: res[i-1][0]+=res[i][0]
                if i+2<len(res): res[i+2][0]+=res[i+1][0]
                res[i:i+2]=[[0,res[i][1]-1]]
                exploded=True
                break
        if exploded: continue
        split=False
        for i,(v,d) in enumerate(res):
            if v>=10:
                l=v//2; r=v-l
                res[i:i+1]=[[l,d+1],[r,d+1]]
                split=True
                break
        if not exploded and not split:
            break
    return res

def magnitude(res):
    res=[x[:] for x in res]
    while len(res)>1:
        md=max(d for v,d in res)
        for i in range(len(res)-1):
            if res[i][1]==md and res[i+1][1]==md:
                v=3*res[i][0]+2*res[i+1][0]
                res[i:i+2]=[[v,md-1]]
                break
    return res[0][0]

data=open(sys.argv[1]).read().splitlines()

# Part 1
m=parse(data[0])
for s in data[1:]:
    m=reduce_sf(add(m,parse(s)))
p1=magnitude(m)

# Part 2
p2=0
for i in range(len(data)):
    for j in range(len(data)):
        if i!=j:
            m1=parse(data[i]); m2=parse(data[j])
            p2=max(p2, magnitude(reduce_sf(add(m1,m2))))
sys.stdout.write(f"{p1} {p2}")