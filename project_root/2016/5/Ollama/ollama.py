import hashlib
import sys

def get_next_char(digest_prefix):
    i = 0
    while True:
        md5_hex = hashlib.md5((data + str(i)).encode()).hexdigest()
        if md5_hex.startswith(digest_prefix):
            return (md5_hex[5], md5_hex[6])
        i += 1

def part1():
    password = []
    for _ in range(8):
        password.append(get_next_char('0' * 5)[0])
    return ''.join(password)

def part2():
    second_password = [None] * 8
    available_positions = set(range(8))
    while None in second_password:
        pos, char = get_next_char('0' * 6)
        if int(pos) < 8 and (int(pos) not in second_password):
            second_password[int(pos)] = char
    return ''.join(second_password)

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.readline().strip()

sys.stdout.write(f"{part1()} {part2()}")