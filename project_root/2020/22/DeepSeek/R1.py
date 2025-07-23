import os
import sys

input_path = sys.argv[1]

input_file = input_path
try:
    with open(input_file) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

line_groups = data.split("\n\n")

def coords(arr2d):
    coords = []
    for y in range(len(arr2d)):
        for x in range(len(arr2d[y])):
            coords.append((x, y))
    return coords

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def ans(answer):
    pass

strips = lambda l: list(map(str.strip, l))
ints = lambda l: list(map(int, l))
commas = lambda s: s.split(",")
comma_ints = lambda s: ints(strips(s.split(",")))

L, I, D, S = list, int, dict, set
P, E, R, M = print, enumerate, range, map

p1 = []
p2 = []
groups = data.split("\n\n")
PRINT_OUTPUT = "p" in sys.argv

for idx, p in enumerate(groups):
    for line in p.split("\n")[1:]:
        if line == "":
            continue
        if idx == 0:
            p1.append(int(line))
        else:
            p2.append(int(line))

p1_backup = p1.copy()
p2_backup = p2.copy()

while True:
    c1, c2 = p1[0], p2[0]
    p1 = p1[1:]
    p2 = p2[1:]
    bigger, smaller = max(c1, c2), min(c1, c2)
    if c1 > c2:
        p1.extend([bigger, smaller])
    else:
        p2.extend([bigger, smaller])
    if len(p1) * len(p2) == 0:
        break

def score(deck):
    score = 0
    for idx, c in enumerate(deck[::-1]):
        score += (idx + 1) * c
    return score

result1 = max(score(p1), score(p2))

p1, p2 = p1_backup, p2_backup

if "b" in sys.argv:
    p1 = [9, 2, 6, 3, 1]
    p2 = [5, 8, 4, 7, 10]

result2 = 0

def recursive_game(deck1, deck2, depth=0):
    seen = set()
    d1 = deck1[:]
    d2 = deck2[:]
    while d1 and d2:
        state = (tuple(d1), tuple(d2))
        if state in seen:
            winner = 1
            break
        seen.add(state)
        c1 = d1.pop(0)
        c2 = d2.pop(0)
        if len(d1) >= c1 and len(d2) >= c2:
            winner = recursive_game(d1[:c1], d2[:c2], depth+1)
        else:
            winner = 1 if c1 > c2 else 2
        if winner == 1:
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)
    else:
        winner = 1 if d1 else 2
    if depth == 0:
        global result2
        result2 = score(d1 if winner == 1 else d2)
    return winner

recursive_game(p1, p2, 0)
print(result1, result2)