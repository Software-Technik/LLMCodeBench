import sys

def mix(values, times):
    n = len(values)
    nxt = list(range(1, n)) + [0]
    prv = [n-1] + list(range(0, n-1))
    for _ in range(times):
        for i, v in enumerate(values):
            k = v % (n-1)
            if k:
                a = prv[i]; b = nxt[i]
                nxt[a] = b; prv[b] = a
                t = i
                for _ in range(k):
                    t = nxt[t]
                c = nxt[t]
                nxt[t] = i; prv[i] = t
                nxt[i] = c; prv[c] = i
    return nxt

def grove(nxt, values):
    n = len(values)
    i = values.index(0)
    res = 0
    for steps in (1000, 2000, 3000):
        for _ in range(steps % n):
            i = nxt[i]
        res += values[i]
    return res

data = sys.argv[1]
with open(data) as f:
    values = [int(line) for line in f]
nxt1 = mix(values, 1)
ans1 = grove(nxt1, values)
key = 811589153
values2 = [v * key for v in values]
nxt2 = mix(values2, 10)
ans2 = grove(nxt2, values2)
sys.stdout.write(f"{ans1}\n{ans2}\n")