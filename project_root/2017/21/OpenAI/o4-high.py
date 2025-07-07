import sys
from collections import Counter

def parse_input(fname):
    r2={}
    r3={}
    with open(fname) as f:
        for line in f:
            line=line.strip()
            if not line or '=>' not in line:
                continue
            a,b=line.split('=>')
            a=a.strip()
            b=b.strip()
            xs=a.split('/')
            n=len(xs)
            s=[]
            for row in xs:
                v=0
                for j,ch in enumerate(row):
                    if ch=='#':
                        v|=1<<j
                s.append(v)
            s_tup=tuple(s)
            ys=b.split('/')
            d=[]
            for row in ys:
                v=0
                for j,ch in enumerate(row):
                    if ch=='#':
                        v|=1<<j
                d.append(v)
            d_tup=tuple(d)
            g=s_tup
            for _ in range(4):
                if n==2:
                    r2[g]=d_tup
                    r2[g[::-1]]=d_tup
                else:
                    r3[g]=d_tup
                    r3[g[::-1]]=d_tup
                g=tuple(
                    sum(((g[n-1-j]>>i)&1)<<j for j in range(n))
                    for i in range(n)
                )
    return r2,r3

def find_next(grid,r2,r3):
    size=len(grid)
    if size&1==0:
        bs=2
        rules=r2
    else:
        bs=3
        rules=r3
    db=bs+1
    blocks=size//bs
    new=[0]*(blocks*db)
    mask=(1<<bs)-1
    for br in range(blocks):
        i0=br*bs
        for bc in range(blocks):
            j0=bc*bs
            pat=tuple((grid[i0+r]>>j0)&mask for r in range(bs))
            dp=rules[pat]
            ri=br*db
            shift=bc*db
            for v in dp:
                new[ri]|=v<<shift
                ri+=1
    return new

def part1(init,r2,r3):
    g=init
    for _ in range(5):
        g=find_next(g,r2,r3)
    return sum(x.bit_count() for x in g)

def fast_count(init,r2,r3,steps):
    def fwd(pat):
        g=list(pat)
        for _ in range(3):
            g=find_next(g,r2,r3)
        cnt=Counter()
        for i in range(0,len(g),3):
            for j in range(0,len(g),3):
                sq=tuple((g[i+r]>>j)&7 for r in range(3))
                cnt[sq]+=1
        return cnt
    counts=Counter({tuple(init):1})
    cache={}
    for _ in range(steps//3):
        nxt=Counter()
        for pat,n in counts.items():
            if pat not in cache:
                cache[pat]=fwd(pat)
            for sp,c in cache[pat].items():
                nxt[sp]+=n*c
        counts=nxt
    total=0
    for pat,n in counts.items():
        for row in pat:
            total+=row.bit_count()*n
    return total

def main():
    fname=sys.argv[1]
    r2,r3=parse_input(fname)
    init=[2,4,7]
    print(part1(init,r2,r3))
    print(fast_count(init,r2,r3,18))

if __name__=='__main__':
    main()