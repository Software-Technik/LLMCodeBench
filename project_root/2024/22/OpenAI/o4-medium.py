import sys

def main():
    path = sys.argv[1]
    with open(path) as f:
        lines = [int(l) for l in f.read().split()]
    mask = (1<<24)-1
    res1 = 0
    for seed in lines:
        x = seed & mask
        for _ in range(2000):
            x = (x ^ (x * 64 & mask)) & mask
            x = (x ^ (x // 32)) & mask
            x = (x ^ (x * 2048 & mask)) & mask
        res1 += x
    global_sum = {}
    for seed in lines:
        seen = set()
        x = seed & mask
        last = [seed % 10]
        for t in range(2000):
            x = (x ^ (x * 64 & mask)) & mask
            x = (x ^ (x // 32)) & mask
            x = (x ^ (x * 2048 & mask)) & mask
            curr = x % 10
            last.append(curr)
            if t >= 5:
                w = last[-5:]
                d = (w[1]-w[0], w[2]-w[1], w[3]-w[2], w[4]-w[3])
                if d not in seen:
                    seen.add(d)
                    global_sum[d] = global_sum.get(d, 0) + curr
    best = max(global_sum.values()) if global_sum else 0
    print(res1, best)

if __name__ == "__main__":
    main()