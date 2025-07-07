import sys
from collections import Counter

CARDS = {"A":14,"K":13,"Q":12,"J":11,"T":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}

def get_hand_type(h):
    c = Counter(h)
    l = len(c)
    if l == 1: return 7
    if l == 2:
        m = max(c.values())
        if m == 4: return 6
        return 5
    if l == 3:
        m = max(c.values())
        if m == 3: return 4
        return 3
    if l == 4: return 2
    return 1

d = []
with open(sys.argv[1]) as f:
    for line in f:
        h, s = line.split()
        d.append((get_hand_type(h), tuple(CARDS[c] for c in h), int(s)))
d.sort(key=lambda x: (x[0], x[1]))
tot = 0
for i, (_, _, s) in enumerate(d):
    tot += (i + 1) * s
sys.stdout.write(f"{tot} {tot}")