import sys
from collections import Counter
def part1(blocks):
    locks = []
    keys = []
    for b in blocks:
        lines = b.splitlines()
        lock = lines[0][0] == "#"
        vals = []
        if lock:
            for j in range(5):
                for i in range(7):
                    if lines[i][j] == ".":
                        vals.append(i)
                        break
            locks.append(tuple(vals))
        else:
            for j in range(5):
                for i in range(6, -1, -1):
                    if lines[i][j] == ".":
                        vals.append(6 - i)
                        break
            keys.append(tuple(vals))
    lc = Counter(locks)
    kc = Counter(keys)
    ans = 0
    for l, lc_count in lc.items():
        for k, kc_count in kc.items():
            for lj, kj in zip(l, k):
                if lj + kj > 7:
                    break
            else:
                ans += lc_count * kc_count
    return ans

blocks = open(sys.argv[1]).read().strip().split("\n\n")
print(part1(blocks))