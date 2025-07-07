import sys

def main():
    with open(sys.argv[1]) as f:
        rules = []
        rs = set()
        for line in f:
            line = line.strip()
            if not line:
                break
            a, b = line.split("|")
            a = int(a); b = int(b)
            rules.append((a, b))
            rs.add((a, b))
        s1 = 0
        s2 = 0
        for line in f:
            line = line.strip()
            if not line:
                continue
            upd = list(map(int, line.split(",")))
            n = len(upd)
            mid = n // 2
            idx = {num: i for i, num in enumerate(upd)}
            ok = True
            for a, b in rules:
                ia = idx.get(a)
                ib = idx.get(b)
                if ia is not None and ib is not None and ia >= ib:
                    ok = False
                    break
            if ok:
                s1 += upd[mid]
            else:
                seq = upd[:]
                m = n
                while True:
                    swapped = False
                    for i in range(m - 1):
                        if (seq[i+1], seq[i]) in rs:
                            seq[i], seq[i+1] = seq[i+1], seq[i]
                            swapped = True
                    if not swapped:
                        break
                s2 += seq[mid]
    print(s1, s2)

if __name__ == "__main__":
    main()