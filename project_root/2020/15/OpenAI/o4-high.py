import sys
from array import array
initial = list(map(int, open(sys.argv[1]).read().split(',')))
t1, t2 = 2020, 30000000
last_seen = array('I', [0]) * (t2+1)
for i, n in enumerate(initial[:-1], 1):
    last_seen[n] = i
last = initial[-1]
res1 = 0
for turn in range(len(initial)+1, t2+1):
    prev = last_seen[last]
    speak = turn-1-prev if prev else 0
    last_seen[last] = turn-1
    last = speak
    if turn == t1:
        res1 = last
print(res1, last)