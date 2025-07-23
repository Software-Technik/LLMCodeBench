from collections import deque
from hashlib import md5
import sys

VAULT = 3 + 3j

def find_vault():
    input_hash = INPUT.encode()
    solutions = []
    que = deque([(0 + 0j, b'')])

    while que:
        pos, path = que.popleft()

        if pos == VAULT:
            solutions.append(path.decode())
            continue

        hash_md5 = md5(input_hash + path).hexdigest()
        u, d, l, r = hash_md5[:4]

        if u > 'a' and pos.imag > 0:
            que.append((pos - 1j, path + b'U'))
        if d > 'a' and pos.imag < 3:
            que.append((pos + 1j, path + b'D'))
        if l > 'a' and pos.real > 0:
            que.append((pos - 1, path + b'L'))
        if r > 'a' and pos.real < 3:
            que.append((pos + 1, path + b'R'))

    return solutions[0], len(solutions[-1])

with open(sys.argv[1], 'r') as file:
    INPUT = file.read().strip()

first, second = find_vault()
print(f"{first} {second}")