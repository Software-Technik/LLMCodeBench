import sys
from collections import deque
def run(data,q):
    mem = data[:] + [0]*10000
    i=0; rel=0
    while True:
        ins = mem[i]; op = ins%100; m=ins//100
        a_mode = m%10; b_mode = m//10%10; c_mode = m//100%10
        if op==99: return
        def addr(offset, mode):
            if mode==0: return mem[i+offset]
            if mode==1: return i+offset
            return mem[i+offset]+rel
        if op==1:
            ra=addr(1,a_mode); rb=addr(2,b_mode); rc=addr(3,c_mode)
            mem[rc]=mem[ra]+mem[rb]; i+=4
        elif op==2:
            ra=addr(1,a_mode); rb=addr(2,b_mode); rc=addr(3,c_mode)
            mem[rc]=mem[ra]*mem[rb]; i+=4
        elif op==3:
            ra=addr(1,a_mode)
            if q: mem[ra]=q.popleft()
            else: mem[ra]=-1; yield None
            i+=2; continue
        elif op==4:
            ra=addr(1,a_mode); yield mem[ra]; i+=2
        elif op==5:
            ra=addr(1,a_mode); rb=addr(2,b_mode)
            i=mem[rb] if mem[ra]!=0 else i+3
        elif op==6:
            ra=addr(1,a_mode); rb=addr(2,b_mode)
            i=mem[rb] if mem[ra]==0 else i+3
        elif op==7:
            ra=addr(1,a_mode); rb=addr(2,b_mode); rc=addr(3,c_mode)
            mem[rc]=1 if mem[ra]<mem[rb] else 0; i+=4
        elif op==8:
            ra=addr(1,a_mode); rb=addr(2,b_mode); rc=addr(3,c_mode)
            mem[rc]=1 if mem[ra]==mem[rb] else 0; i+=4
        elif op==9:
            ra=addr(1,a_mode); rel+=mem[ra]; i+=2

def part1(data):
    queues=[deque([i]) for i in range(50)]
    comps=[run(data,q) for q in queues]
    while True:
        for c in comps:
            addr=next(c)
            if addr is None: continue
            x=next(c); y=next(c)
            if addr==255: return y
            queues[addr].append(x); queues[addr].append(y)

def part2(data):
    queues=[deque([i]) for i in range(50)]
    comps=[run(data,q) for q in queues]
    nat=None; last_y=None; idle=0
    while True:
        if idle==50 and nat is not None:
            x,y=nat
            if y==last_y: return y
            queues[0].append(x); queues[0].append(y)
            last_y=y
        idle=0
        for c in comps:
            addr=next(c)
            if addr is None:
                idle+=1; continue
            x=next(c); y=next(c)
            if addr==255: nat=(x,y)
            else: queues[addr].append(x); queues[addr].append(y)

if __name__=='__main__':
    with open(sys.argv[1]) as f:
        data=list(map(int,f.read().strip().split(',')))
    r1=part1(data); r2=part2(data)
    sys.stdout.write(f"{r1} {r2}")