import sys
from math import sqrt, ceil
f = open(sys.argv[1])
times = list(map(int, f.readline().partition(':')[2].split()))
distances = list(map(int, f.readline().partition(':')[2].split()))
_sqrt, _ceil = sqrt, ceil
total = 1
for t, d in zip(times, distances):
    i = _ceil((t - _sqrt(t*t - 4*d)) * 0.5)
    if i*(t - i) <= d: i += 1
    mp = t // 2
    if i < mp:
        total *= (mp - i + 1)*2 if t & 1 else (mp - i)*2 + 1
t0, d0 = times[0], distances[0]
i = _ceil((t0 - _sqrt(t0*t0 - 4*d0)) * 0.5)
if i*(t0 - i) <= d0: i += 1
mp = t0 // 2
if i < mp:
    p2 = (mp - i + 1)*2 if t0 & 1 else (mp - i)*2 + 1
else:
    p2 = 0
sys.stdout.write(f"{total} {p2}")