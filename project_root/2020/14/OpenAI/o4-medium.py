import sys

data = open(sys.argv[1]).read().splitlines()
mem1 = {}
mem2 = {}
mask_or1 = mask_and1 = mask_or2 = 0
xs = []

for line in data:
    if not line: continue
    op, val = line.split(' = ')
    if op == 'mask':
        m = val.strip()
        mask_or1 = int(m.replace('X','0'), 2)
        mask_and1 = int(m.replace('X','1'), 2)
        mask_or2 = mask_or1
        xs = [35 - i for i, c in enumerate(m) if c == 'X']
    else:
        addr = int(op[4:-1])
        v = int(val)
        mem1[addr] = (v | mask_or1) & mask_and1
        base = addr | mask_or2
        n = len(xs)
        for c in range(1 << n):
            a = base
            for j, p in enumerate(xs):
                if (c >> j) & 1:
                    a |= 1 << p
                else:
                    a &= ~(1 << p)
            mem2[a] = v

print(sum(mem1.values()), sum(mem2.values()))