import sys
def main():
    p1 = p2 = 0
    with open(sys.argv[1]) as f:
        for line in f:
            parts = line.split()
            if not parts:
                continue
            arr = list(map(int, parts))
            n = len(arr)
            if n < 2:
                continue
            d0 = arr[1] - arr[0]
            if d0 == 0:
                continue
            inc0 = d0 > 0
            low0, high0 = (1, 3) if inc0 else (-3, -1)
            bad = []
            for i in range(n-1):
                d = arr[i+1] - arr[i]
                if d < low0 or d > high0:
                    bad.append(i)
                    if len(bad) > 2:
                        break
            if not bad:
                p1 += 1
                p2 += 1
            else:
                ks = {0, n-1}
                if len(bad) <= 2:
                    for d in bad:
                        ks.add(d)
                        ks.add(d+1)
                for k in ks:
                    if k < 0 or k >= n:
                        continue
                    idx0 = 1 if k == 0 else 0
                    idx1 = 2 if k <= 1 else 1
                    if idx1 >= n:
                        continue
                    inc = arr[idx1] > arr[idx0]
                    low, high = (1, 3) if inc else (-3, -1)
                    ok = True
                    for j in range(1, n-1):
                        prev = j-1 + (1 if j-1 >= k else 0)
                        cur = j + (1 if j >= k else 0)
                        d = arr[cur] - arr[prev]
                        if d < low or d > high:
                            ok = False
                            break
                    if ok:
                        p2 += 1
                        break
    print(p1, p2)
if __name__ == '__main__':
    main()