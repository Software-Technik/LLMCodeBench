import sys

def solve(digits, jump):
    return sum(n for i, n in enumerate(digits) if n == digits[(i + jump) % len(digits)])

input_strings = sys.argv[1]
with open(input_strings) as f:
    digits = [int(digit) for digit in f.read().strip()]

print(solve(digits, 1))
print(solve(digits, len(digits) // 2))