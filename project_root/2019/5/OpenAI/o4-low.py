import sys
def solve(data, inp):
    p = data.copy()
    i = 0
    out = None
    while True:
        ins = p[i]
        op = ins % 100
        if op == 99:
            break
        m1 = ins // 100 % 10
        m2 = ins // 1000 % 10
        if op == 1:
            a = p[i+1] if m1 else p[p[i+1]]
            b = p[i+2] if m2 else p[p[i+2]]
            p[p[i+3]] = a + b
            i += 4
        elif op == 2:
            a = p[i+1] if m1 else p[p[i+1]]
            b = p[i+2] if m2 else p[p[i+2]]
            p[p[i+3]] = a * b
            i += 4
        elif op == 3:
            p[p[i+1]] = inp
            i += 2
        elif op == 4:
            out = p[i+1] if m1 else p[p[i+1]]
            i += 2
        elif op == 5:
            a = p[i+1] if m1 else p[p[i+1]]
            b = p[i+2] if m2 else p[p[i+2]]
            i = b if a else i+3
        elif op == 6:
            a = p[i+1] if m1 else p[p[i+1]]
            b = p[i+2] if m2 else p[p[i+2]]
            i = b if not a else i+3
        elif op == 7:
            a = p[i+1] if m1 else p[p[i+1]]
            b = p[i+2] if m2 else p[p[i+2]]
            p[p[i+3]] = 1 if a < b else 0
            i += 4
        elif op == 8:
            a = p[i+1] if m1 else p[p[i+1]]
            b = p[i+2] if m2 else p[p[i+2]]
            p[p[i+3]] = 1 if a == b else 0
            i += 4
        else:
            raise
    return out

with open(sys.argv[1]) as f:
    data = list(map(int, f.read().split(",",)))
r1 = solve(data,1)
r2 = solve(data,5)
sys.stdout.write(f"{r1} {r2}")