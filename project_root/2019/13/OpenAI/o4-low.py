import sys
from collections import defaultdict

def runComputer(data, input_func):
    prog = defaultdict(int, enumerate(data))
    i = rel = 0
    while True:
        op = prog[i] % 100
        if op == 99: return
        m1 = prog[i]//100%10; m2 = prog[i]//1000%10; m3 = prog[i]//10000%10
        def addr(n, m):
            v = prog[i+n]
            return v+rel if m==2 else i+n if m==1 else v
        if op in (1,2,7,8):
            a, b, c = addr(1,m1), addr(2,m2), addr(3,m3)
            v1, v2 = prog[a], prog[b]
            if op==1: prog[c]=v1+v2
            elif op==2: prog[c]=v1*v2
            elif op==7: prog[c]=1 if v1<v2 else 0
            else: prog[c]=1 if v1==v2 else 0
            i+=4
        elif op==3:
            prog[addr(1,m1)] = input_func()
            i+=2
        elif op==4:
            yield prog[addr(1,m1)]
            i+=2
        elif op in (5,6):
            v = prog[addr(1,m1)]
            j = prog[addr(2,m2)]
            if (op==5 and v!=0) or (op==6 and v==0):
                i = j
            else:
                i += 3
        elif op==9:
            rel += prog[addr(1,m1)]
            i+=2

def part1(data):
    out = list(runComputer(data.copy(), lambda:0))
    return sum(1 for t in out[2::3] if t==2)

def part2(data):
    data = data.copy()
    data[0]=2
    score = 0
    inputs = [0]
    def inp():
        return inputs.pop()
    gen = runComputer(data, inp)
    px=bx=0
    for x in gen:
        y = next(gen); t = next(gen)
        if x==-1:
            score = t
        else:
            if t==3: px=x
            if t==4: bx=x
        inputs.append(0 if px==bx else (1 if px>bx else -1))
    return score

data = list(map(int, open(sys.argv[1]).read().splitlines()[0].split(',')))
print(part1(data), part2(data))