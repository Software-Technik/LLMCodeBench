import sys

def solve(digits, jump):
    n, total = len(digits), sum(digits[(i + jump) % len(digits)] for i in range(len(digits)) if digits[i] == digits[(i + jump) % len(digits)])
    return total // (n // jump)

input_strings = sys.argv[1]
with open(input_strings) as f:
    digits = [int(digit) for digit in f.read().strip()]

print(solve(digits, 1))
print(solve(digits, len(digits) // 2))