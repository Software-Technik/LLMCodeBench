import sys

def grove(values, rounds):
    n = len(values)
    prev = [i-1 for i in range(n)]
    nxt = [i+1 for i in range(n)]
    prev[0] = n-1
    nxt[n-1] = 0
    for _ in range(rounds):
        for i, v in enumerate(values):
            steps = v % (n-1)
            if steps:
                t = i
                for _ in range(steps):
                    t = nxt[t]
                p, q = prev[i], nxt[i]
                nxt[p] = q
                prev[q] = p
                u = nxt[t]
                nxt[t] = i
                prev[i] = t
                nxt[i] = u
                prev[u] = i
    idx = values.index(0)
    res = 0
    for off in (1000, 2000, 3000):
        for _ in range(off % n):
            idx = nxt[idx]
        res += values[idx]
    return res

def main():
    path = sys.argv[1]
    with open(path) as f:
        vals = [int(line) for line in f]
    p1 = grove(vals, 1)
    p2 = grove([v * 811589153 for v in vals], 10)
    sys.stdout.write(f"{p1}\n{p2}\n")

if __name__ == "__main__":
    main()