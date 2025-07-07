import sys

def main():
    import sys
    data = open(sys.argv[1]).read().splitlines()
    instr = []
    for line in data:
        l, r = line.split(" = ")
        if l == "mask":
            instr.append((l, r))
        else:
            addr = int(l[4:-1])
            val = int(r)
            instr.append((addr, val))

    mem1 = {}
    mask_or = mask_and = None
    for op, val in instr:
        if op == "mask":
            m = val
            mask_or = int(m.replace('X','0'),2)
            mask_and = int(m.replace('X','1'),2)
        else:
            addr, v = op, val
            mem1[addr] = (v | mask_or) & mask_and
    result1 = sum(mem1.values())

    mem2 = {}
    floating = []
    mask_or2 = None
    for op, val in instr:
        if op == "mask":
            m = val
            mask_or2 = int(m.replace('X','0'),2)
            floating = [35-i for i,ch in enumerate(m) if ch=='X']
        else:
            addr, v = op, val
            base = (addr | mask_or2)
            for pos in floating:
                base &= ~(1<<pos)
            n = len(floating)
            for combo in range(1<<n):
                a = base
                for j,pos in enumerate(floating):
                    if combo>>j &1:
                        a |= 1<<pos
                mem2[a] = v
    result2 = sum(mem2.values())

    print(result1, result2)

if __name__ == "__main__":
    main()