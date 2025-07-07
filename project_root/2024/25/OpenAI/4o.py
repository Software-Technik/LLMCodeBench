import sys

def part1(lines):
    def parse(s):
        lock = s[0][0] == "#"
        vals = [next((i if lock else 6 - i) for i in range(7) if (s[i][j] == "." if lock else s[6-i][j] == ".")) for j in range(5)]
        return vals, lock

    locks, keys = [], []
    for section in lines:
        vals, lock = parse(section.split("\n"))
        (locks if lock else keys).append(vals)

    return sum(all(lock[j] + key[j] <= 7 for j in range(5)) for lock in locks for key in keys)

input_path = sys.argv[1]
with open(input_path) as fin:
    lines = fin.read().strip().split("\n\n")
    print(part1(lines))