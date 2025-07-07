import sys
from collections import deque
from itertools import islice

def combat(d1, d2):
    seen = set()
    while d1 and d2:
        key = (tuple(d1), tuple(d2))
        if key in seen:
            return 1, d1
        seen.add(key)
        c1 = d1.popleft()
        c2 = d2.popleft()
        if len(d1) >= c1 and len(d2) >= c2:
            nd1 = deque(islice(d1, 0, c1))
            nd2 = deque(islice(d2, 0, c2))
            w, _ = combat(nd1, nd2)
        else:
            w = 1 if c1 > c2 else 2
        if w == 1:
            d1.append(c1); d1.append(c2)
        else:
            d2.append(c2); d2.append(c1)
    return (1, d1) if d1 else (2, d2)

def score(d):
    return sum((i+1)*c for i, c in enumerate(reversed(d)))

with open(sys.argv[1]) as f:
    blocks = f.read().strip().split('\n\n')
d1_init = deque(int(x) for x in blocks[0].splitlines()[1:])
d2_init = deque(int(x) for x in blocks[1].splitlines()[1:])

d1, d2 = deque(d1_init), deque(d2_init)
while d1 and d2:
    c1 = d1.popleft(); c2 = d2.popleft()
    if c1 > c2:
        d1.append(c1); d1.append(c2)
    else:
        d2.append(c2); d2.append(c1)
score1 = score(d1 if d1 else d2)

_, deck2 = combat(deque(d1_init), deque(d2_init))
score2 = score(deck2)

print(score1, score2)