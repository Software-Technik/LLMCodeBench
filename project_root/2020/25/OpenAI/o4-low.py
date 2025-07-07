import sys

input_file = sys.argv[1]
with open(input_file) as f:
    a, b = map(int, f.read().split())

mod = 20201227

def find_loop_size(subject, target):
    value = 1
    ls = 0
    while True:
        ls += 1
        value = (value * subject) % mod
        if value == target:
            return ls

door_loop = find_loop_size(7, a)
card_loop = find_loop_size(7, b)
secret = pow(a, card_loop, mod)
secret2 = pow(b, door_loop, mod)
print(secret, secret2)