import sys

input_path = sys.argv[1]

with open(input_path) as f:
    data = f.read()
    
a, b = map(int, data.splitlines())
mod = 20201227

def find(sub, goal):
    value = 1
    i = 0
    while value != goal:
        value = (value * sub) % mod
        i += 1
    return i

door_loop = find(7, a)
card_loop = find(7, b)

def trans(sub, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * sub) % mod
    return value

secret = trans(a, card_loop)
secret2 = trans(b, door_loop)

print(secret, secret2)