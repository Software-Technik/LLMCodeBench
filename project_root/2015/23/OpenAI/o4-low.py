import sys

def run(start_a, instrs):
    regs = [start_a, 0]
    idx, n = 0, len(instrs)
    while 0 <= idx < n:
        op, r, off = instrs[idx]
        if op == 0:
            regs[r] //= 2
            idx += 1
        elif op == 1:
            regs[r] *= 3
            idx += 1
        elif op == 2:
            regs[r] += 1
            idx += 1
        elif op == 3:
            idx += off
        elif op == 4:
            idx += off if regs[r] & 1 == 0 else 1
        else:
            idx += off if regs[r] == 1 else 1
    return regs[1]

lines = [l.strip() for l in open(sys.argv[1])]
instrs = []
for L in lines:
    op = L[:3]
    t = L[4:]
    if op == "hlf":
        instrs.append((0, 0 if t=="a" else 1, 0))
    elif op == "tpl":
        instrs.append((1, 0 if t=="a" else 1, 0))
    elif op == "inc":
        instrs.append((2, 0 if t=="a" else 1, 0))
    elif op == "jmp":
        instrs.append((3, 0, int(t)))
    elif op == "jie":
        r, o = t.split(", ")
        instrs.append((4, 0 if r=="a" else 1, int(o)))
    else:
        r, o = t.split(", ")
        instrs.append((5, 0 if r=="a" else 1, int(o)))

sys.stdout.write(f"{run(0, instrs)}\n{run(1, instrs)}\n")