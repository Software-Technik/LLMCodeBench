import hashlib
import sys



def part1(data):
    i = 0
    first_password = ''
    second_password = [''] * 8
    available_positions = set('01234567')
    while available_positions:
        char_input = (data+str(i)).encode()
        md5_hex = hashlib.md5(char_input).hexdigest()

        if md5_hex.startswith(5*'0'):
            if len(first_password) < 8:
                first_password += md5_hex[5]
            if md5_hex[5] in available_positions:
                second_password[int(md5_hex[5])] = md5_hex[6]
                available_positions.remove(md5_hex[5])
        i += 1
    return first_password

def part2(data):
    i = 0
    first_password = ''
    second_password = [''] * 8
    available_positions = set('01234567')
    while available_positions:
        char_input = (data+str(i)).encode()
        md5_hex = hashlib.md5(char_input).hexdigest()

        if md5_hex.startswith(5*'0'):
            if len(first_password) < 8:
                first_password += md5_hex[5]
            if md5_hex[5] in available_positions:
                second_password[int(md5_hex[5])] = md5_hex[6]
                available_positions.remove(md5_hex[5])
        i += 1
    return ''.join(second_password)


inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.readline().strip()


sys.stdout.write(f"{part1(data)} {part2(data)}") 
