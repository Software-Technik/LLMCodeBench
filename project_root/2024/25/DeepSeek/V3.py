import sys

def part1(lines):
    def parse(s):
        lock = s[0][0] == '#'
        vals = []
        if lock:
            for j in range(5):
                for i in range(7):
                    if s[i][j] == '.':
                        vals.append(i)
                        break
        else:
            for j in range(5):
                for i in range(6, -1, -1):
                    if s[i][j] == '.':
                        vals.append(6 - i)
                        break
        return vals, lock

    locks = []
    keys = []
    for s in lines:
        vals, lock = parse(s.split('\n'))
        if lock:
            locks.append(vals)
        else:
            keys.append(vals)

    ans = 0
    for lock in locks:
        for key in keys:
            good = True
            for l, k in zip(lock, key):
                if l + k > 7:
                    good = False
                    break
            ans += good
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split('\n\n')
    print(part1(lines))