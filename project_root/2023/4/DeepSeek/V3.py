import sys

def part1(text: str) -> int:
    total = 0
    for line in text.splitlines():
        parts = line.split(":", 1)[1].split("|", 1)
        winning_numbers = set(parts[0].split())
        numbers = set(parts[1].split())
        matches = len(winning_numbers & numbers)
        if matches:
            total += 1 << (matches - 1)
    return total

def part2(text: str) -> int:
    lines = text.splitlines()
    n = len(lines)
    cards = [0] * n
    for i, line in enumerate(lines):
        parts = line.split(":", 1)[1].split("|", 1)
        winning_numbers = set(parts[0].split())
        numbers = set(parts[1].split())
        cards[i] = len(winning_numbers & numbers)
    
    dp = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, min(i + 1 + cards[i], n)):
            dp[i] += dp[j]
    return sum(dp)

with open(sys.argv[1]) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")