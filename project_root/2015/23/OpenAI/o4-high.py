import sys

def run(insts, a0):
    regs = [a0, 0]
    i = 0
    n = len(insts)
    while 0 <= i < n:
        op, x, y = insts[i]
        if op == 0:
            regs[x] //= 2
            i += 1
        elif op == 1:
            regs[x] *= 3
            i += 1
        elif op == 2:
            regs[x] += 1
            i += 1
        elif op == 3:
            i += y
        elif op == 4:
            i += y if regs[x] & 1 == 0 else 1
        else:
            i += y if regs[x] == 1 else 1
    return regs[1]

data = open(sys.argv[1]).read().splitlines()
insts = []
for l in data:
    c = l[0]
    if c == 'h':
        insts.append((0, 0 if l[4] == 'a' else 1, 0))
    elif c == 't':
        insts.append((1, 0 if l[4] == 'a' else 1, 0))
    elif c == 'i':
        insts.append((2, 0 if l[4] == 'a' else 1, 0))
    else:
        if l[1] == 'm':
            insts.append((3, 0, int(l[4:])))
        else:
            r = 0 if l[4] == 'a' else 1
            y = int(l[7:])
            insts.append((4 if l[2] == 'e' else 5, r, y))

print(run(insts, 0))
print(run(insts, 1))