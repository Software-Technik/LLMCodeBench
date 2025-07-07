import sys
def mix(values, rounds):
    n = len(values)
    nxt = list(range(1, n+1))
    prv = list(range(-1, n-1))
    nxt[-1] = 0
    prv[0] = n-1
    for _ in range(rounds):
        for i, v in enumerate(values):
            steps = v % (n-1)
            if steps == 0: continue
            a = prv[i]; b = nxt[i]
            nxt[a] = b; prv[b] = a
            dest = i
            for _ in range(steps):
                dest = nxt[dest]
            c = nxt[dest]
            nxt[dest] = i; prv[i] = dest
            nxt[i] = c; prv[c] = i
    return nxt, prv

def score(values, nxt):
    n = len(values)
    z = values.index(0)
    res = 0
    cur = z
    for steps in (1000, 2000, 3000):
        for _ in range(steps % n):
            cur = nxt[cur]
        res += values[cur]
    return res

data = sys.argv[1]
with open(data) as f:
    vals = [int(line) for line in f]

nxt1, prv1 = mix(vals, 1)
p1 = score(vals, nxt1)
vals2 = [v * 811589153 for v in vals]
nxt2, prv2 = mix(vals2, 10)
p2 = score(vals2, nxt2)

sys.stdout.write(f"{p1}\n{p2}\n")