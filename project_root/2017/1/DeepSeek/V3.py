import sys

def solve(digits, jump):
    size = len(digits)
    return sum(n for i, n in enumerate(digits) if n == digits[(i + jump) % size])

with open(sys.argv[1]) as f:
    digits = [int(digit) for digit in f.read().strip()]

print(solve(digits, 1))
print(solve(digits, len(digits) // 2))