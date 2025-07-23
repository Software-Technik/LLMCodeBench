import sys

input_path = sys.argv[1]

input_file = input_path
if "s" in sys.argv:
    input_file = "input_small.txt"
try:
    with open(input_file) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

a, b = map(int, data.splitlines())
door_pub = a
card_pub = b
mod = 20201227

def find_loop_size(sub, goal):
    value = 1
    loop_size = 0
    while value != goal:
        value = (value * sub) % mod
        loop_size += 1
    return loop_size

door_loop = find_loop_size(7, door_pub)
card_loop = find_loop_size(7, card_pub)

def transform(sub, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * sub) % mod
    return value

secret = transform(door_pub, card_loop)
print(secret)