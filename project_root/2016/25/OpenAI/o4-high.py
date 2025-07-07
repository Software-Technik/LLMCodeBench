import sys

def main():
    reg_map = {'a':0,'b':1,'c':2,'d':3}
    lines = open(sys.argv[1]).read().splitlines()
    n = len(lines)
    ops = [0]*n
    xregs = [False]*n
    xvals = [0]*n
    yregs = [False]*n
    yvals = [0]*n
    for i,line in enumerate(lines):
        p = line.split()
        op = p[0]
        if op == 'cpy':
            ops[i] = 0
            x = p[1]
            if x.isalpha():
                xregs[i] = True; xvals[i] = reg_map[x]
            else:
                xregs[i] = False; xvals[i] = int(x)
            yregs[i] = True; yvals[i] = reg_map[p[2]]
        elif op == 'inc':
            ops[i] = 1
            xregs[i] = True; xvals[i] = reg_map[p[1]]
        elif op == 'dec':
            ops[i] = 2
            xregs[i] = True; xvals[i] = reg_map[p[1]]
        elif op == 'jnz':
            ops[i] = 3
            x = p[1]
            if x.isalpha():
                xregs[i] = True; xvals[i] = reg_map[x]
            else:
                xregs[i] = False; xvals[i] = int(x)
            y = p[2]
            if y.isalpha():
                yregs[i] = True; yvals[i] = reg_map[y]
            else:
                yregs[i] = False; yvals[i] = int(y)
        else:
            ops[i] = 4
            x = p[1]
            if x.isalpha():
                xregs[i] = True; xvals[i] = reg_map[x]
            else:
                xregs[i] = False; xvals[i] = int(x)
    a = 0
    while True:
        regs = [a,0,0,0]
        ip = 0
        prev = 1
        count = 0
        while 0 <= ip < n:
            op = ops[ip]
            if op == 0:
                regs[yvals[ip]] = regs[xvals[ip]] if xregs[ip] else xvals[ip]
                ip += 1
            elif op == 1:
                regs[xvals[ip]] += 1
                ip += 1
            elif op == 2:
                regs[xvals[ip]] -= 1
                ip += 1
            elif op == 3:
                xval = regs[xvals[ip]] if xregs[ip] else xvals[ip]
                if xval != 0:
                    ip += regs[yvals[ip]] if yregs[ip] else yvals[ip]
                else:
                    ip += 1
            else:
                outv = regs[xvals[ip]] if xregs[ip] else xvals[ip]
                if (outv != 0 and outv != 1) or outv == prev:
                    break
                prev = outv
                count += 1
                if count == 10:
                    sys.stdout.write(str(a))
                    return
                ip += 1
        a += 1

if __name__ == '__main__':
    main()