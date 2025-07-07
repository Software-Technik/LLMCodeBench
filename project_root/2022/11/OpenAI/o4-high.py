import sys
from collections import deque
from math import lcm
def parse(s):
    blocks = s.split("\n\n")
    n = len(blocks)
    items = [None]*n
    codes = [0]*n
    vals = [0]*n
    tests = [0]*n
    t_true = [0]*n
    t_false = [0]*n
    times = [0]*n
    for i, b in enumerate(blocks):
        lines = b.splitlines()
        items[i] = deque(map(int, lines[1].split(":")[1].split(",")))
        op = lines[2].split("=",1)[1].strip().split()
        if op[1] == "+":
            if op[2] == "old":
                codes[i] = 2
            else:
                codes[i] = 0; vals[i] = int(op[2])
        else:
            if op[2] == "old":
                codes[i] = 3
            else:
                codes[i] = 1; vals[i] = int(op[2])
        tests[i] = int(lines[3].split("by")[1])
        t_true[i] = int(lines[4].split("monkey")[1])
        t_false[i] = int(lines[5].split("monkey")[1])
    return items, codes, vals, tests, t_true, t_false, times
def run1(r, items, codes, vals, tests, t_true, t_false, times):
    n = len(items)
    for _ in range(r):
        for i in range(n):
            dq = items[i]
            code = codes[i]
            val = vals[i]
            div = tests[i]
            pt = items[t_true[i]].append
            pf = items[t_false[i]].append
            pop = dq.popleft
            while dq:
                times[i] += 1
                w = pop()
                if code == 0:
                    w += val
                elif code == 1:
                    w *= val
                elif code == 2:
                    w += w
                else:
                    w *= w
                w //= 3
                if w % div == 0:
                    pt(w)
                else:
                    pf(w)
def run2(r, modv, items, codes, vals, tests, t_true, t_false, times):
    n = len(items)
    for _ in range(r):
        for i in range(n):
            dq = items[i]
            code = codes[i]
            val = vals[i]
            div = tests[i]
            pt = items[t_true[i]].append
            pf = items[t_false[i]].append
            pop = dq.popleft
            while dq:
                times[i] += 1
                w = pop()
                if code == 0:
                    w += val
                elif code == 1:
                    w *= val
                elif code == 2:
                    w += w
                else:
                    w *= w
                w %= modv
                if w % div == 0:
                    pt(w)
                else:
                    pf(w)
def main():
    data = open(sys.argv[1]).read().strip()
    items, codes, vals, tests, t_true, t_false, times = parse(data)
    run1(20, items, codes, vals, tests, t_true, t_false, times)
    a = b = 0
    for x in times:
        if x > a:
            b = a; a = x
        elif x > b:
            b = x
    res1 = a * b
    items, codes, vals, tests, t_true, t_false, times = parse(data)
    modv = lcm(*tests)
    run2(10000, modv, items, codes, vals, tests, t_true, t_false, times)
    a = b = 0
    for x in times:
        if x > a:
            b = a; a = x
        elif x > b:
            b = x
    res2 = a * b
    sys.stdout.write(f"{res1}\n{res2}\n")
if __name__ == "__main__":
    main()