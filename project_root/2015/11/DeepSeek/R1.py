import sys
from itertools import groupby

def part1(data):
    c = data[0]
    c = next_password(c)
    while not valid_password(c):
        c = next_password(c)
    return c

def part2(data):
    c = part1(data)
    return part1([c])

def next_password(password):
    chars = "abcdefghjkmnpqrstuvwxyz"
    n_chars = len(chars)
    password_list = list(password)
    i = len(password_list) - 1
    carry = 1
    while i >= 0 and carry:
        c = password_list[i]
        pos = chars.index(c)
        new_val = pos + carry
        carry = new_val // n_chars
        new_val %= n_chars
        password_list[i] = chars[new_val]
        i -= 1
        if not carry:
            break
    return ''.join(password_list)

def valid_password(password):
    if any(c in "iol" for c in password):
        return False
    found = False
    for i in range(len(password)-2):
        a, b, c = password[i], password[i+1], password[i+2]
        if ord(b) == ord(a)+1 and ord(c) == ord(a)+2:
            found = True
            break
    if not found:
        return False
    total_pairs = 0
    for _, g in groupby(password):
        n = 0
        for _ in g:
            n += 1
        total_pairs += n // 2
        if total_pairs > 1:
            break
    return total_pairs > 1

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")