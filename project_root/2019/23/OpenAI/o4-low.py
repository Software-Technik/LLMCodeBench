import sys
from collections import deque, defaultdict

def run(data, q):
    prog = defaultdict(int, enumerate(data))
    i = rel = 0
    while True:
        instr = prog[i]; op = instr % 100
        if op == 99: break
        m1 = instr // 100 % 10; m2 = instr // 1000 % 10; m3 = instr // 10000 % 10
        def addr(m, k):
            v = prog[i+k]
            return v+rel if m==2 else (i+k if m==1 else v)
        p1 = addr(m1,1); p2 = addr(m2,2); p3 = addr(m3,3)
        if op == 1:
            prog[p3] = prog[p1] + prog[p2]; i += 4
        elif op == 2:
            prog[p3] = prog[p1] * prog[p2]; i += 4
        elif op == 3:
            if q:
                prog[p1] = q.popleft()
                i += 2
            else:
                prog[p1] = -1
                i += 2
                yield "CONTINUE"
        elif op == 4:
            yield prog[p1]; i += 2
        elif op == 5:
            i = prog[p2] if prog[p1] else i+3
        elif op == 6:
            i = prog[p2] if not prog[p1] else i+3
        elif op == 7:
            prog[p3] = int(prog[p1] < prog[p2]); i += 4
        elif op == 8:
            prog[p3] = int(prog[p1] == prog[p2]); i += 4
        elif op == 9:
            rel += prog[p1]; i += 2

def part1(data):
    qs = [deque([i]) for i in range(50)]
    comps = [run(data, q) for q in qs]
    while True:
        for c in comps:
            addr = next(c)
            if addr == "CONTINUE": continue
            x = next(c); y = next(c)
            if addr == 255:
                return y
            qs[addr].append(x); qs[addr].append(y)

def part2(data):
    qs = [deque([i]) for i in range(50)]
    comps = [run(data, q) for q in qs]
    nat = (0,0); last = None
    while True:
        idle = True
        for c in comps:
            addr = next(c)
            if addr == "CONTINUE": continue
            idle = False
            x = next(c); y = next(c)
            if addr == 255:
                nat = (x, y)
            else:
                qs[addr].append(x); qs[addr].append(y)
        if idle:
            x, y = nat
            if y == last:
                return y
            qs[0].append(x); qs[0].append(y)
            last = y

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = list(map(int, f.read().splitlines()[0].split(",")))
    print(part1(data), part2(data))