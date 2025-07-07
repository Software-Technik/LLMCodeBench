import sys
from collections import deque
def run(mem,q):
    ip=0
    rb=0
    pop=q.popleft
    while True:
        inst=mem[ip]
        op=inst%100
        md=inst//100
        if op==99:
            return
        m1=md%10
        m2=md//10%10
        m3=md//100%10
        if op in (1,2,7,8):
            p1=mem[ip+1]
            p2=mem[ip+2]
            p3=mem[ip+3]
            if m1==2:
                a=p1+rb
            elif m1==1:
                a=ip+1
            else:
                a=p1
            if m2==2:
                b=p2+rb
            elif m2==1:
                b=ip+2
            else:
                b=p2
            if m3==2:
                c=p3+rb
            else:
                c=p3
            v1=mem[a]
            v2=mem[b]
            if op==1:
                mem[c]=v1+v2
            elif op==2:
                mem[c]=v1*v2
            elif op==7:
                mem[c]=1 if v1<v2 else 0
            else:
                mem[c]=1 if v1==v2 else 0
            ip+=4
        elif op==3:
            p1=mem[ip+1]
            if m1==2:
                a=p1+rb
            elif m1==1:
                a=ip+1
            else:
                a=p1
            if q:
                mem[a]=pop()
                ip+=2
            else:
                mem[a]=-1
                ip+=2
                yield None
        elif op==4:
            p1=mem[ip+1]
            if m1==2:
                a=p1+rb
            elif m1==1:
                a=ip+1
            else:
                a=p1
            val=mem[a]
            ip+=2
            yield val
        elif op in (5,6):
            p1=mem[ip+1]
            p2=mem[ip+2]
            if m1==2:
                a=p1+rb
            elif m1==1:
                a=ip+1
            else:
                a=p1
            if m2==2:
                b=p2+rb
            elif m2==1:
                b=ip+2
            else:
                b=p2
            v1=mem[a]
            v2=mem[b]
            if op==5:
                if v1!=0:
                    ip=v2
                else:
                    ip+=3
            else:
                if v1==0:
                    ip=v2
                else:
                    ip+=3
        elif op==9:
            p1=mem[ip+1]
            if m1==2:
                a=p1+rb
            elif m1==1:
                a=ip+1
            else:
                a=p1
            rb+=mem[a]
            ip+=2
        else:
            return

def part1(data):
    queues=[deque([i]) for i in range(50)]
    comps=[run(data.copy(),queues[i]) for i in range(50)]
    while True:
        for i in range(50):
            res=next(comps[i])
            if res is None:
                continue
            addr=res
            x=next(comps[i])
            y=next(comps[i])
            if addr==255:
                return y
            queues[addr].append(x)
            queues[addr].append(y)

def part2(data):
    queues=[deque([i]) for i in range(50)]
    comps=[run(data.copy(),queues[i]) for i in range(50)]
    nat=(0,0)
    lasty=None
    natready=False
    while True:
        idle=0
        for i in range(50):
            res=next(comps[i])
            if res is None:
                idle+=1
                continue
            addr=res
            x=next(comps[i])
            y=next(comps[i])
            if addr==255:
                nat=(x,y)
                natready=True
            else:
                queues[addr].append(x)
                queues[addr].append(y)
        if idle==50 and natready:
            x,y=nat
            if y==lasty:
                return y
            queues[0].append(x)
            queues[0].append(y)
            lasty=y
            natready=False

if __name__=='__main__':
    with open(sys.argv[1]) as f:
        raw=list(map(int,f.read().splitlines()[0].split(',')))
    base=raw+[0]*10000
    sys.stdout.write(f"{part1(base)} {part2(base)}")