from collections import deque
import sys
from hashlib import md5

VAULT_X, VAULT_Y = 3, 3

def find_vault(INPUT):
    first = None
    max_len = 0
    q = deque([(0, 0, "")])
    while q:
        x, y, path = q.popleft()
        if x == VAULT_X and y == VAULT_Y:
            if first is None:
                first = path
            if len(path) > max_len:
                max_len = len(path)
            continue
        h = md5((INPUT + path).encode()).hexdigest()
        if h[0] > "a" and y > 0:
            q.append((x, y - 1, path + "U"))
        if h[1] > "a" and y < VAULT_Y:
            q.append((x, y + 1, path + "D"))
        if h[2] > "a" and x > 0:
            q.append((x - 1, y, path + "L"))
        if h[3] > "a" and x < VAULT_X:
            q.append((x + 1, y, path + "R"))
    return first, max_len

with open(sys.argv[1]) as f:
    inp = f.read().strip()
a, b = find_vault(inp)
sys.stdout.write(f"{a} {b}")