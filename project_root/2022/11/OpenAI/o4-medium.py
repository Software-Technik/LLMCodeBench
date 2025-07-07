import sys, math
from collections import deque

def parse(s):
    monkeys=[]
    for block in s.strip().split('\n\n'):
        lines=block.splitlines()
        items=deque(map(int, lines[1].split(':',1)[1].strip().split(', ')))
        parts=lines[2].split('=')[1].split()
        if parts[2]=='old':
            op=0 if parts[1]=='+' else 2
            val=0
        else:
            val=int(parts[2])
            op=1 if parts[1]=='+' else 3
        div=int(lines[3].split()[-1])
        t_true=int(lines[4].split()[-1])
        t_false=int(lines[5].split()[-1])
        monkeys.append([items,op,val,div,t_false,t_true,0])
    return monkeys

def simulate(monkeys, rounds, part2=False, mod=1):
    for _ in range(rounds):
        for m in monkeys:
            q,op,val,div,f,t,_=m
            while q:
                m[6]+=1
                x=q.popleft()
                if op==0: x+=x
                elif op==1: x+=val
                elif op==2: x*=x
                else: x*=val
                if part2: x%=mod
                else: x//=3
                (monkeys[t][0] if x%div==0 else monkeys[f][0]).append(x)
    a=sorted(m[6] for m in monkeys)
    return a[-1]*a[-2]

data=open(sys.argv[1]).read()
m1=parse(data)
m2=parse(data)
mod=math.lcm(*[m[3] for m in m1])
print(simulate(m1,20), simulate(m2,10000, True, mod), sep='\n')