import sys

def solve(s, jump):
    n = len(s)
    total = 0
    for i, c in enumerate(s):
        if c == s[(i + jump) % n]:
            total += ord(c) - 48
    return total

with open(sys.argv[1]) as f:
    s = f.read().strip()
print(solve(s, 1))
print(solve(s, len(s) // 2))