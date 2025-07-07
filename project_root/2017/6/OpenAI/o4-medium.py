import sys
def redistribute(banks):
    seen = {}
    n = len(banks)
    step = 0
    t = tuple(banks)
    while t not in seen:
        seen[t] = step
        i = max(range(n), key=banks.__getitem__)
        v = banks[i]
        banks[i] = 0
        for j in range(1, v+1):
            banks[(i+j) % n] += 1
        step += 1
        t = tuple(banks)
    return step, step - seen[t]

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        banks = list(map(int, f.read().split()))
    p1, p2 = redistribute(banks)
    print(p1)
    print(p2)