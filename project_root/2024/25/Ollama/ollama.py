import sys

def part1(lines):
    def parse(s):
        lock = s[0][0] == "#"
        if not lock: return [6 - i for j in range(5) for i in range(6, -1, -1) if s[i][j] == "."]
        return [i for j in range(5) for i in range(7) if s[i][j] == "."], True

    keys = []
    locks = []
    for s in lines:
        if (lock := parse(s.split("\n"))[1]):
            locks.append(lock)
        else:
            keys.append(lock)

    return sum(not any(l[j] + k[j] > 7 for j in range(5)) for lock in locks for k in keys)

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n\n")

print(part1(lines))