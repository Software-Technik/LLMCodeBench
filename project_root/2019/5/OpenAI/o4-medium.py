import sys
def solve(data, inp):
    p = data.copy()
    i = 0
    out = 0
    while True:
        v = p[i]
        op = v % 100
        if op == 99:
            break
        m = v // 100
        a = p[i+1] if m%10 else p[p[i+1]]
        m //= 10
        if op == 1:
            b = p[i+2] if m%10 else p[p[i+2]]
            p[p[i+3]] = a + b
            i += 4
        elif op == 2:
            b = p[i+2] if m%10 else p[p[i+2]]
            p[p[i+3]] = a * b
            i += 4
        elif op == 3:
            p[p[i+1]] = inp
            i += 2
        elif op == 4:
            out = a
            i += 2
        elif op == 5:
            b = p[i+2] if m%10 else p[p[i+2]]
            i = b if a != 0 else i+3
        elif op == 6:
            b = p[i+2] if m%10 else p[p[i+2]]
            i = b if a == 0 else i+3
        elif op == 7:
            b = p[i+2] if m%10 else p[p[i+2]]
            p[p[i+3]] = 1 if a < b else 0
            i += 4
        elif op == 8:
            b = p[i+2] if m%10 else p[p[i+2]]
            p[p[i+3]] = 1 if a == b else 0
            i += 4
        else:
            raise ValueError
    return out

def part1(data):
    return solve(data, 1)

def part2(data):
    return solve(data, 5)

data = list(map(int, open(sys.argv[1]).read().strip().split(',')))
print(part1(data), part2(data))