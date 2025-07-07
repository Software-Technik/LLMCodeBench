import sys

def runComputer(data, inp):
    mem = data + [0] * (len(data) * 100)
    i = rel = 0
    out = 0
    while True:
        ins = mem[i]
        op = ins % 100
        if op == 99:
            break
        m1 = ins // 100 % 10
        m2 = ins // 1000 % 10
        m3 = ins // 10000 % 10
        if op == 3:
            p = mem[i+1] + (rel if m1 == 2 else 0) if m1 != 1 else i+1
            mem[p] = inp
            i += 2
            continue
        p1 = mem[i+1] + (rel if m1 == 2 else 0) if m1 != 1 else i+1
        if op != 4 and op != 9:
            p2 = mem[i+2] + (rel if m2 == 2 else 0) if m2 != 1 else i+2
        if op in (1,2,7,8):
            p3 = mem[i+3] + (rel if m3 == 2 else 0)
        if op == 1:
            mem[p3] = mem[p1] + mem[p2]
            i += 4
        elif op == 2:
            mem[p3] = mem[p1] * mem[p2]
            i += 4
        elif op == 4:
            out = mem[p1]
            i += 2
        elif op == 5:
            i = mem[p2] if mem[p1] != 0 else i + 3
        elif op == 6:
            i = mem[p2] if mem[p1] == 0 else i + 3
        elif op == 7:
            mem[p3] = 1 if mem[p1] < mem[p2] else 0
            i += 4
        elif op == 8:
            mem[p3] = 1 if mem[p1] == mem[p2] else 0
            i += 4
        elif op == 9:
            rel += mem[p1]
            i += 2
    return out

def part1(data):
    return runComputer(data, 1)

def part2(data):
    return runComputer(data, 2)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data = list(map(int, f.read().strip().split(",")))
    sys.stdout.write(f"{part1(data)} {part2(data)}")