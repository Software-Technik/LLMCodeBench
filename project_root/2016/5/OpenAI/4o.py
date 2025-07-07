import hashlib
import sys

def find_passwords(data):
    i, first_password, available_positions = 0, [], set('01234567')
    second_password = [''] * 8
    while available_positions or len(first_password) < 8:
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
    return ''.join(first_password), ''.join(second_password)

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.readline().strip()

part1_result, part2_result = find_passwords(data)
sys.stdout.write(f"{part1_result} {part2_result}")