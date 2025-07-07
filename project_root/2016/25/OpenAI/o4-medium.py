import sys
lines = open(sys.argv[1]).read().splitlines()
inst = []
for line in lines:
    parts = line.split()
    op = parts[0]
    if op == 'cpy':
        x, y = parts[1], parts[2]
        if x.isalpha():
            xi, xv = True, ord(x) - 97
        else:
            xi, xv = False, int(x)
        inst.append((0, xi, xv, ord(y) - 97))
    elif op == 'inc':
        inst.append((1, ord(parts[1]) - 97))
    elif op == 'dec':
        inst.append((2, ord(parts[1]) - 97))
    elif op == 'jnz':
        x, y = parts[1], parts[2]
        if x.isalpha():
            xi, xv = True, ord(x) - 97
        else:
            xi, xv = False, int(x)
        if y.isalpha():
            yi, yv = True, ord(y) - 97
        else:
            yi, yv = False, int(y)
        inst.append((3, xi, xv, yi, yv))
    elif op == 'out':
        x = parts[1]
        if x.isalpha():
            xi, xv = True, ord(x) - 97
        else:
            xi, xv = False, int(x)
        inst.append((4, xi, xv))
i = 0
while True:
    regs = [i, 0, 0, 0]
    pc = 0
    last = 1
    count = 0
    while pc < len(inst):
        ins = inst[pc]
        opc = ins[0]
        if opc == 0:
            _, xi, xv, yv = ins
            regs[yv] = regs[xv] if xi else xv
        elif opc == 1:
            regs[ins[1]] += 1
        elif opc == 2:
            regs[ins[1]] -= 1
        elif opc == 3:
            _, xi, xv, yi, yv = ins
            v = regs[xv] if xi else xv
            if v != 0:
                pc += regs[yv] if yi else yv
                continue
        else:
            _, xi, xv = ins
            v = regs[xv] if xi else xv
            if v not in (0, 1) or v == last:
                break
            last = v
            count += 1
            if count >= 10:
                sys.stdout.write(str(i))
                sys.exit()
        pc += 1
    i += 1