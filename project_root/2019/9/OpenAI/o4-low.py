import sys
from collections import defaultdict

def runComputer(data, inp):
    p = defaultdict(int, enumerate(data))
    i = rel = 0
    out = None
    get = p.get
    while True:
        instr = p[i]; op = instr % 100; m1 = instr//100%10; m2 = instr//1000%10; m3 = instr//10000%10
        if op == 99: break
        a = p[i+1] + (rel if m1==2 else 0) if m1 else p[i+1]
        b = p[i+2] + (rel if m2==2 else 0) if m2 else p[i+2]
        if op in (1,2,7,8,):
            c = p[i+3] + (rel if m3==2 else 0)
            x = p[a] if m1!=1 else p[i+1]
            y = p[b] if m2!=1 else p[i+2]
            if op==1: p[c]=x+y
            elif op==2: p[c]=x*y
            elif op==7: p[c]=1 if x<y else 0
            else: p[c]=1 if x==y else 0
            i+=4
        elif op==3:
            p[a]=inp; i+=2
        elif op==4:
            out = p[a] if m1!=1 else p[i+1]; i+=2
        elif op==5 or op==6:
            x = p[a] if m1!=1 else p[i+1]
            y = p[b] if m2!=1 else p[i+2]
            if (op==5 and x) or (op==6 and not x): i=y
            else: i+=3
        elif op==9:
            rel += p[a] if m1!=1 else p[i+1]; i+=2
    return out

def part1(d): return runComputer(d,1)
def part2(d): return runComputer(d,2)

with open(sys.argv[1]) as f:
    data=list(map(int,f.read().splitlines()[0].split(',')))
print(part1(data),part2(data))