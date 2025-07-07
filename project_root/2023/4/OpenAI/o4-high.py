import sys
def main():
    ks = []
    p1 = 0
    with open(sys.argv[1]) as f:
        for line in f:
            l = line.rstrip('\n')
            if not l: continue
            i = l.find(':')
            j = l.find('|', i+1)
            w = set(l[i+1:j].split())
            n = set(l[j+1:].split())
            c = len(w & n)
            ks.append(c)
            if c: p1 += 1 << (c-1)
    N = len(ks)
    suff = [0] * (N+1)
    sd = 0
    for idx in range(N-1, -1, -1):
        c = ks[idx]
        j = idx + c + 1
        if j > N: j = N
        dp = c + suff[idx+1] - suff[j]
        sd += dp
        suff[idx] = dp + suff[idx+1]
    p2 = sd + N
    sys.stdout.write(f"{p1} {p2}")
if __name__ == "__main__":
    main()