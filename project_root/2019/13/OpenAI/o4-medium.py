import sys

def runComputer(data, inputs):
    mem = data[:] + [0]*10000
    i = 0
    rb = 0
    while True:
        inst = mem[i]
        op = inst % 100
        if op == 99:
            return
        m1 = inst//100 % 10
        m2 = inst//1000 % 10
        m3 = inst//10000 % 10
        if op in (1,2,7,8):
            a = mem[i+1] if m1==1 else (mem[mem[i+1]+rb] if m1==2 else mem[mem[i+1]])
            b = mem[i+2] if m2==1 else (mem[mem[i+2]+rb] if m2==2 else mem[mem[i+2]])
            dest = mem[i+3] + (rb if m3==2 else 0)
            if op==1:
                mem[dest] = a+b
            elif op==2:
                mem[dest] = a*b
            elif op==7:
                mem[dest] = 1 if a<b else 0
            else:
                mem[dest] = 1 if a==b else 0
            i += 4
        elif op == 3:
            dest = mem[i+1] + (rb if m1==2 else 0)
            mem[dest] = inputs.pop()
            i += 2
        elif op == 4:
            val = mem[i+1] if m1==1 else (mem[mem[i+1]+rb] if m1==2 else mem[mem[i+1]])
            yield val
            i += 2
        elif op in (5,6):
            cond = mem[i+1] if m1==1 else (mem[mem[i+1]+rb] if m1==2 else mem[mem[i+1]])
            target = mem[i+2] if m2==1 else (mem[mem[i+2]+rb] if m2==2 else mem[mem[i+2]])
            if (op==5 and cond) or (op==6 and not cond):
                i = target
            else:
                i += 3
        elif op == 9:
            val = mem[i+1] if m1==1 else (mem[mem[i+1]+rb] if m1==2 else mem[mem[i+1]])
            rb += val
            i += 2

def part1(data):
    runner = runComputer(data, [])
    blocks = 0
    it = runner
    for x in it:
        y = next(it)
        t = next(it)
        if t == 2:
            blocks += 1
    return blocks

def part2(data):
    data = data[:]
    data[0] = 2
    inputs = [0]
    runner = runComputer(data, inputs)
    score = 0
    px = py = bx = by = 0
    it = runner
    for x in it:
        y = next(it)
        t = next(it)
        if x == -1:
            score = t
        else:
            if t == 3:
                px,py = x,y
            elif t == 4:
                bx,by = x,y
            inputs.clear()
            if px < bx:
                inputs.append(1 if by < py + 1 else -1)
            elif px > bx:
                inputs.append(-1 if by < py + 1 else 1)
            else:
                inputs.append(0)
    return score

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = list(map(int, f.read().split(',')))
    sys.stdout.write(f"{part1(data)} {part2(data)}")