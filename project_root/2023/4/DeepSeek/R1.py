import sys

def part1(text: str) -> int:
    total = 0
    for line in text.splitlines():
        parts = line.split(":", 1)[1].split("|", 1)
        winning_numbers = set(parts[0].split())
        numbers = set(parts[1].split())
        matches = winning_numbers & numbers
        if matches:
            total += 1 << (len(matches) - 1)
    return total

def part2(text: str) -> int:
    cards = []
    for line in text.splitlines():
        parts = line.split(":", 1)[1].split("|", 1)
        winning_numbers = set(parts[0].split())
        numbers = set(parts[1].split())
        matches = winning_numbers & numbers
        cards.append(len(matches))
    
    n = len(cards)
    dp = [1] * n
    for i in range(n-2, -1, -1):
        count = cards[i]
        for j in range(1, count+1):
            if i+j < n:
                dp[i] += dp[i+j]
    return sum(dp)

input_file = sys.argv[1]
with open(input_file) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")