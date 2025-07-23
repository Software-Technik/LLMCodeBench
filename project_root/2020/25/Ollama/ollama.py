import sys

a, b = map(int, open(sys.argv[1]).read().splitlines())
mod = 20201227

def transform(value, loop_size):
    value = (value * pow(7, loop_size, mod)) % mod
    return value

def find_loop(subject_number, goal):
    value, loop_size = subject_number, 0
    while value != 1:
        if value == goal: return loop_size + 1
        value = (value * subject_number) % mod
        loop_size += 1

door_loop = find_loop(7, a)
card_loop = find_loop(7, b)

secret_card = transform(a, card_loop)
secret_door = transform(b, door_loop)
print(secret_card, secret_door)