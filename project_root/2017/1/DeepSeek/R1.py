import sys

def solve(digits, jump):
    n = len(digits)
    if n == 0:
        return 0
    if jump == 1:
        total = 0
        for i in range(n-1):
            if digits[i] == digits[i+1]:
                total += digits[i]
        if digits[-1] == digits[0]:
            total += digits[-1]
        return total
    elif jump == n // 2 and n % 2 == 0:
        total = 0
        half = n // 2
        for i in range(half):
            if digits[i] == digits[i+half]:
                total += digits[i] * 2
        return total
    else:
        total = 0
        for i in range(n):
            if digits[i] == digits[(i + jump) % n]:
                total += digits[i]
        return total

input_file = sys.argv[1]
with open(input_file) as f:
    data = f.read().strip()
    digits = [int(d) for d in data]

print(solve(digits, 1))
print(solve(digits, len(digits) // 2))