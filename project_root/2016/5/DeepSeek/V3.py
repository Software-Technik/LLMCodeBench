import hashlib
import sys

def solve(data):
    i = 0
    first_password = []
    second_password = [''] * 8
    available_positions = set('01234567')
    while len(first_password) < 8 or available_positions:
        char_input = (data + str(i)).encode()
        md5_hex = hashlib.md5(char_input).hexdigest()
        if md5_hex.startswith('00000'):
            if len(first_password) < 8:
                first_password.append(md5_hex[5])
            pos = md5_hex[5]
            if pos in available_positions:
                second_password[int(pos)] = md5_hex[6]
                available_positions.remove(pos)
        i += 1
    return ''.join(first_password[:8]), ''.join(second_password)

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.readline().strip()

part1, part2 = solve(data)
sys.stdout.write(f"{part1} {part2}")