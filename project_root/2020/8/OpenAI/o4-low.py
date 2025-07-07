import sys

def run(prog):
    acc = 0
    idx = 0
    seen = set()
    n = len(prog)
    while idx not in seen:
        if idx >= n:
            return acc
        seen.add(idx)
        op, val = prog[idx]
        if op == 'acc':
            acc += val
            idx += 1
        elif op == 'jmp':
            idx += val
        else:
            idx += 1
    return None if idx < n else acc

with open(sys.argv[1]) as f:
    prog = [(l.split()[0], int(l.split()[1])) for l in f.read().splitlines()]

# Part 1
acc1 = 0
idx = 0
seen = set()
while idx not in seen:
    seen.add(idx)
    op, val = prog[idx]
    if op == 'acc':
        acc1 += val
        idx += 1
    elif op == 'jmp':
        idx += val
    else:
        idx += 1

# Part 2
acc2 = None
for i in range(len(prog)):
    op, val = prog[i]
    if op == 'acc': continue
    prog[i] = ('jmp' if op == 'nop' else 'nop', val)
    res = run(prog)
    prog[i] = (op, val)
    if res is not None:
        acc2 = res
        break

print(acc1, acc2)