import sys
from collections import defaultdict

def runComputer(data, inp):
    pr = defaultdict(int)
    pr.update(enumerate(data))
    pop = inp.pop
    i = 0; rb = 0
    while True:
        inst = pr[i]; op = inst % 100
        if op == 99: break
        m1 = inst//100 % 10; m2 = inst//1000 % 10; m3 = inst//10000 % 10
        if m1 == 1:
            a1 = i+1
        elif m1 == 2:
            a1 = pr[i+1] + rb
        else:
            a1 = pr[i+1]
        if op == 3:
            pr[a1] = pop(); i += 2; continue
        v1 = pr[a1]
        if op == 4:
            yield v1; i += 2; continue
        if m2 == 1:
            a2 = i+2
        elif m2 == 2:
            a2 = pr[i+2] + rb
        else:
            a2 = pr[i+2]
        v2 = pr[a2]
        if op == 9:
            rb += v1; i += 2; continue
        if op == 5:
            i = v2 if v1 else i+3; continue
        if op == 6:
            i = v2 if not v1 else i+3; continue
        if m3 == 2:
            a3 = pr[i+3] + rb
        else:
            a3 = pr[i+3]
        if op == 1:
            pr[a3] = v1 + v2
        elif op == 2:
            pr[a3] = v1 * v2
        elif op == 7:
            pr[a3] = int(v1 < v2)
        elif op == 8:
            pr[a3] = int(v1 == v2)
        else:
            raise
        i += 4

def part1(data):
    cnt = 0
    gen = runComputer(data, [])
    for _, _, t in zip(gen, gen, gen):
        if t == 2: cnt += 1
    return cnt

def part2(data):
    data = data[:]
    data[0] = 2
    inp = [0]
    gen = runComputer(data, inp)
    score = -1
    px = py = bx = by = 0
    for x, y, t in zip(gen, gen, gen):
        if x < 0:
            score = t
        else:
            if t == 3:
                px, py = x, y
            elif t == 4:
                bx, by = x, y
            inp.clear()
            if px < bx:
                inp.append(1 if by < py+1 else -1)
            elif px > bx:
                inp.append(-1 if by < py+1 else 1)
            else:
                inp.append(0)
    return score

if __name__ == '__main__':
    data = list(map(int, open(sys.argv[1]).read().strip().split(',')))
    r1 = part1(data)
    r2 = part2(data)
    sys.stdout.write(f"{r1} {r2}")