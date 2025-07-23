import sys
from functools import lru_cache

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()
    line_groups = data.split("\n\n")

p1 = []
p2 = []
for idx, p in enumerate(line_groups):
    for line in p.split("\n")[1:]:
        if line == "":
            continue
        if idx == 0:
            p1.append(int(line))
        else:
            p2.append(int(line))

p1_backup = p1.copy()
p2_backup = p2.copy()

while p1 and p2:
    c1, c2 = p1.pop(0), p2.pop(0)
    if c1 > c2:
        p1.extend([c1, c2])
    else:
        p2.extend([c2, c1])

def score(deck):
    return sum((i + 1) * card for i, card in enumerate(reversed(deck)))

result1 = max(score(p1), score(p2))

p1, p2 = p1_backup, p2_backup

@lru_cache(maxsize=None)
def recursive_combat(p1, p2):
    seen = set()
    p1, p2 = list(p1), list(p2)
    while p1 and p2:
        state = (tuple(p1), tuple(p2))
        if state in seen:
            return (1, p1)
        seen.add(state)
        c1, c2 = p1.pop(0), p2.pop(0)
        if len(p1) >= c1 and len(p2) >= c2:
            winner, _ = recursive_combat(tuple(p1[:c1]), tuple(p2[:c2]))
        else:
            winner = 1 if c1 > c2 else 2
        if winner == 1:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    return (1, p1) if p1 else (2, p2)

_, winning_deck = recursive_combat(tuple(p1), tuple(p2))
result2 = score(winning_deck)

print(result1, result2)