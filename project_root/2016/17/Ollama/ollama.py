from collections import deque
from hashlib import md5
import sys

VAULT = (3 + 3j)

def find_vault():
    sol_len = -1
    que = deque([(0 + 0j, '')])
    while que:
        pos, path = que.popleft()
        if pos.real == VAULT.real and pos.imag == VAULT.imag:
            return path, len(path)
        hash_value = md5((INPUT + path).encode()).hexdigest()[:4]
        movements = [(pos - 1j, 'U'), (pos + 1j, 'D'), (pos - 1, 'L'), (pos + 1, 'R')]

        for new_pos, move in movements:
            if (0 <= new_pos.real < 4) and (0 <= new_pos.imag < 4) and hash_value[movements.index((new_pos, move))] > 'a':
                que.append((new_pos, path + move))

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as file:
    INPUT = file.read().strip()

first, second = find_vault()
sys.stdout.write(f"{first} {second}")