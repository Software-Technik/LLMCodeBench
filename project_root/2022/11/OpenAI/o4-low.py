import sys
from collections import deque
from math import lcm

def parse(data):
    items, ops, tests, targets = [], [], [], []
    for block in "\n".join(data).split("\n\n"):
        lines = block.splitlines()
        items.append(deque(map(int, lines[1].split(":")[1].split(", "))))
        op_parts = lines[2].split("= ")[1].split()
        if op_parts[1] == '+':
            if op_parts[2] == 'old':
                ops.append(lambda x, o=ops: x + x)
            else:
                v = int(op_parts[2]); ops.append(lambda x, v=v: x + v)
        else:
            if op_parts[2] == 'old':
                ops.append(lambda x, o=ops: x * x)
            else:
                v = int(op_parts[2]); ops.append(lambda x, v=v: x * v)
        tests.append(int(lines[3].split()[-1]))
        f = int(lines[4].split()[-1]); t = int(lines[5].split()[-1])
        targets.append((f, t))
    times = [0]*len(items)
    return items, ops, tests, targets, times

def run(rounds, div3):
    items, ops, tests, targets, times = parse(data)
    mod = lcm(*tests)
    for _ in range(rounds):
        for i in range(len(items)):
            dq = items[i]
            op = ops[i]; test = tests[i]; t0, t1 = targets[i]
            while dq:
                times[i] += 1
                w = op(dq.popleft())
                w = (w//3 if div3 else w%mod)
                items[t1 if w%test==0 else t0].append(w)
    a, b = sorted(times)[-2:]
    return a*b

with open(sys.argv[1]) as f:
    data = [l.strip() for l in f]
print(run(20, True))
print(run(10000, False))