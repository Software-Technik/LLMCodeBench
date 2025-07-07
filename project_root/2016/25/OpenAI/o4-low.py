import sys

data = open(sys.argv[1]).read().splitlines()
ops = []
reg_map = {'a':0,'b':1,'c':2,'d':3}
for line in data:
    parts = line.split()
    op = parts[0]
    x = parts[1]
    y = parts[2] if len(parts)>2 else None
    if x.isalpha():
        xi = reg_map[x]; x_is_reg = True
    else:
        xi = int(x); x_is_reg = False
    if y is not None:
        if y.isalpha():
            yi = reg_map[y]; y_is_reg = True
        else:
            yi = int(y); y_is_reg = False
    else:
        yi = None; y_is_reg = False
    ops.append((op,x_is_reg,xi,y_is_reg,yi))
def test(a):
    regs = [a,0,0,0]
    line = 0
    prev = 1
    count = 0
    L = len(ops)
    while line < L and count < 10:
        op,x_is_reg,xi,y_is_reg,yi = ops[line]
        if op=='out':
            v = regs[xi] if x_is_reg else xi
            if v^prev!=1: return False
            prev = v
            count += 1
            line += 1
        elif op=='cpy':
            v = regs[xi] if x_is_reg else xi
            regs[yi] = v
            line += 1
        elif op=='inc':
            regs[xi] += 1; line += 1
        elif op=='dec':
            regs[xi] -= 1; line += 1
        elif op=='jnz':
            v = regs[xi] if x_is_reg else xi
            if v!=0:
                offset = regs[yi] if y_is_reg else yi
                line += offset
            else:
                line += 1
    return count>=10

i=0
while True:
    if test(i):
        sys.stdout.write(str(i))
        break
    i+=1