import sys
from itertools import islice

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
except:
    data = ""

p1, p2 = data.strip().split("\n\n")
p1 = list(map(int, p1.splitlines()[1:]))
p2 = list(map(int, p2.splitlines()[1:]))

p1_backup = p1[:]
p2_backup = p2[:]

while p1 and p2:
    c1, c2 = p1.pop(0), p2.pop(0)
    if c1 > c2:
        p1.extend([c1, c2])
    else:
        p2.extend([c2, c1])

def score(deck):
    return sum((i + 1) * card for i, card in enumerate(reversed(deck)))

result1 = score(p1 or p2)

p1, p2 = p1_backup, p2_backup

def game(p1, p2):
    seen = set()
    while p1 and p2:
        if (tuple(p1), tuple(p2)) in seen:
            return 1, p1
        seen.add((tuple(p1), tuple(p2)))

        c1, c2 = p1.pop(0), p2.pop(0)
        if len(p1) >= c1 and len(p2) >= c2:
            winner, _ = game(p1[:c1], p2[:c2])
        else:
            winner = 1 if c1 > c2 else 2

        if winner == 1:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])

    return (1, p1) if p1 else (2, p2)

_, winning_deck = game(p1, p2)
result2 = score(winning_deck)

print(result1, result2)