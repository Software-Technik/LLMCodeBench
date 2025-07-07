import sys
from collections import deque

p1 = p2 = 0
prev = None
buf = deque(maxlen=3)
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip()
        if not line: continue
        curr = int(line)
        if prev is not None and prev < curr:
            p1 += 1
        if len(buf) == 3 and buf[0] < curr:
            p2 += 1
        buf.append(curr)
        prev = curr
sys.stdout.write(f"{p1} {p2}")