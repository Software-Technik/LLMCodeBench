import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.read().strip().splitlines()
    two = three = 0
    for s in lines:
        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
        f2 = f3 = False
        for v in cnt.values():
            if v == 2:
                f2 = True
            elif v == 3:
                f3 = True
        two += f2
        three += f3
    checksum = two * three
    common = ''
    if lines:
        L = len(lines[0])
        for i in range(L):
            seen = set()
            for s in lines:
                key = s[:i] + s[i+1:]
                if key in seen:
                    common = key
                    break
                seen.add(key)
            if common:
                break
    sys.stdout.write(f"{checksum} {common}")