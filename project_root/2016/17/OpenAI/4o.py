from collections import deque
from hashlib import md5
import sys

VAULT = 3 + 3j

def find_vault():
    shortest = None
    longest_length = 0
    que = deque([(0 + 0j, '')])

    while que:
        pos, path = que.popleft()

        if pos == VAULT:
            if shortest is None:
                shortest = path
            longest_length = max(longest_length, len(path))
            continue

        u, d, l, r = md5((INPUT + path).encode()).hexdigest()[:4]

        if u > 'a' and pos.imag > 0:
            que.append((pos - 1j, path + 'U'))
        if d > 'a' and pos.imag < 3:
            que.append((pos + 1j, path + 'D'))
        if l > 'a' and pos.real > 0:
            que.append((pos - 1, path + 'L'))
        if r > 'a' and pos.real < 3:
            que.append((pos + 1, path + 'R'))

    return shortest, longest_length

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as file:
    INPUT = file.read().strip()

first, second = find_vault()

sys.stdout.write(f"{first} {second}")