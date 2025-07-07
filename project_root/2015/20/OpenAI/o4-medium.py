import sys
def main():
    T = int(open(sys.argv[1]).read().strip())
    limit1 = T // 10
    h1 = [0] * (limit1 + 1)
    for e in range(1, limit1 + 1):
        v = e * 10
        for m in range(e, limit1 + 1, e):
            h1[m] += v
    for i in range(1, limit1 + 1):
        if h1[i] >= T:
            p1 = i
            break
    limit2 = T // 11
    h2 = [0] * (limit2 + 1)
    for e in range(1, limit2 + 1):
        v = e * 11
        m = e
        for _ in range(50):
            if m > limit2: break
            h2[m] += v
            m += e
    for i in range(1, limit2 + 1):
        if h2[i] >= T:
            p2 = i
            break
    print(p1)
    print(p2)
if __name__ == '__main__':
    main()