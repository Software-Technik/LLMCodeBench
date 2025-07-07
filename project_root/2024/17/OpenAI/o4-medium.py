import sys
def part1(lines):
    a=int(lines[0].split(':',1)[1])
    b=int(lines[1].split(':',1)[1])
    c=int(lines[2].split(':',1)[1])
    prog=list(map(int,lines[4].split(':',1)[1].split(',')))
    out=[]
    p=0; L=len(prog)
    while p< L:
        op=prog[p]; x=prog[p+1]
        if op==0:
            if x<=3: v=x
            elif x==4: v=a
            elif x==5: v=b
            else: v=c
            a >>= v
        elif op==1:
            b ^= x
        elif op==2:
            if x<=3: v=x
            elif x==4: v=a
            elif x==5: v=b
            else: v=c
            b = v & 7
        elif op==3:
            if a!=0:
                p=x; continue
        elif op==4:
            b ^= c
        elif op==5:
            if x<=3: v=x
            elif x==4: v=a
            elif x==5: v=b
            else: v=c
            out.append(str(v&7))
        elif op==6:
            if x<=3: v=x
            elif x==4: v=a
            elif x==5: v=b
            else: v=c
            b = a >> v
        elif op==7:
            if x<=3: v=x
            elif x==4: v=a
            elif x==5: v=b
            else: v=c
            c = a >> v
        else:
            raise ValueError
        p+=2
    return ','.join(out)
def part2(lines):
    prog=list(map(int,lines[4].split(':',1)[1].split(',')))
    if prog[-2:]!=[3,0]: raise AssertionError
    n=len(prog)-2
    def rec(d,ans):
        if d<0: return ans
        tgt=prog[d]
        for t in range(8):
            a=(ans<<3)|t; b=0; c=0; outv=None; adv=False
            for i in range(0,n,2):
                op=prog[i]; x=prog[i+1]
                if op==0:
                    if adv or x!=3: raise ValueError
                    adv=True
                elif op==1:
                    b ^= x
                elif op==2:
                    if x<=3: v=x
                    elif x==4: v=a
                    elif x==5: v=b
                    else: v=c
                    b = v & 7
                elif op==3:
                    raise AssertionError
                elif op==4:
                    b ^= c
                elif op==5:
                    if outv is not None: raise ValueError
                    if x<=3: v=x
                    elif x==4: v=a
                    elif x==5: v=b
                    else: v=c
                    outv = v & 7
                elif op==6:
                    if x<=3: v=x
                    elif x==4: v=a
                    elif x==5: v=b
                    else: v=c
                    b = a >> v
                elif op==7:
                    if x<=3: v=x
                    elif x==4: v=a
                    elif x==5: v=b
                    else: v=c
                    c = a >> v
                else:
                    raise AssertionError
            if outv==tgt:
                res=rec(d-1,a)
                if res is not None: return res
        return None
    return rec(len(prog)-1,0)
lines=open(sys.argv[1]).read().splitlines()
print(part1(lines),part2(lines))