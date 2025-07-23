from collections import deque
from hashlib import md5
import sys

VAULT = 3+3j

def find_vault():
    que = deque([(0+0j, '')])
    shortest = None
    while que:
        pos, path = que.popleft()
        if pos == VAULT:
            shortest = path
            break
        hash_val = md5((INPUT + path).encode()).hexdigest()[:4]
        u, d, l, r = hash_val
        if u > 'a' and pos.imag > 0:
            que.append((pos - 1j, path + 'U'))
        if d > 'a' and pos.imag < 3:
            que.append((pos + 1j, path + 'D'))
        if l > 'a' and pos.real > 0:
            que.append((pos - 1, path + 'L'))
        if r > 'a' and pos.real < 3:
            que.append((pos + 1, path + 'R'))
    
    stack = [(0+0j, '')]
    longest = 0
    while stack:
        pos, path = stack.pop()
        if pos == VAULT:
            if len(path) > longest:
                longest = len(path)
            continue
        hash_val = md5((INPUT + path).encode()).hexdigest()[:4]
        u, d, l, r = hash_val
        if u > 'a' and pos.imag > 0:
            stack.append((pos - 1j, path + 'U'))
        if d > 'a' and pos.imag < 3:
            stack.append((pos + 1j, path + 'D'))
        if l > 'a' and pos.real > 0:
            stack.append((pos - 1, path + 'L'))
        if r > 'a' and pos.real < 3:
            stack.append((pos + 1, path + 'R'))
    return shortest, longest

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as file:
    INPUT = file.read().strip()

first, second = find_vault()
sys.stdout.write(f"{first} {second}")