import sys

input_file = sys.argv[1]
with open(input_file) as f:
    data = f.read().split("\n\n")
p1, p2 = list(map(int, lines.split("\n")[1:])) for lines in data)

def score(deck):
    return sum((i + 1) * c for i, c in enumerate(reversed(deck)))

while len(p1) and len(p2):
    if not (c1 := p1.pop(0)) or not (c2 := p2.pop(0)):
        continue
    winner = p1 if c1 > c2 else p2
    winner.extend([c1, c2])

result1 = score(p1) + score(p2)

p1, p2 = data.split("\n\n"), data.split("\n\n", 1)[1].split("\n")[1:]
p1, p2 = list(map(int, lines.split("\n")[1:])) for lines in data)

seen = set()
def play(p1, p2):
    while len(p1) and len(p2):
        if (tuple(p1), tuple(p2)) in seen:
            return 1
        seen.add((tuple(p1), tuple(p2)))
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > len(p1) or c2 > len(p2):
            winner = max(c1, c2) == c1 if len(set(p1)) != 1 else len(lp1) != 0
        else:
            l1, l2 = p1[:c1], p2[:c2]
            winner = play(deepcopy(l1), deepcopy(l2))
        (p1 if winner == 1 else p2).extend((c1, c2) if winner == 1 else (c2, c1))

play(p1, p2)
result2 = score(p1 + p2)

print(result1, result2)