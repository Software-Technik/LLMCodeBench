import sys
from collections import deque

def run_game(p, m):
    s = [0] * p
    c = deque([0])
    n, i = -1, 0
    while (n := n+1) != m:
        if not (n % 23): c.appendleft(*c.popleft()); s[i] += n + c.pop(); i = (i+1) % p; continue
        c.rotate(2); c[0] = n; i = (i+1) % p

    return max(s)

with open(sys.argv[1], 'r') as f: (p, m) = map(int, filter(str.isdigit, f.read()))
print(f'{run_game(p, m)} {run_game(p, m * 100)}')