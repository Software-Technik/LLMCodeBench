import sys
from itertools import groupby

def part1(data):
    c = data[0]
    while True:
        c = next_password(c)
        if valid_password(c):
            return c

def part2(data):
    c = part1(data)
    return part1([c])

def next_password(password):
    chars = "abcdefghjkmnpqrstuvwxyz"
    password = list(password)
    n = len(password)
    i = n - 1
    while i >= 0:
        c = password[i]
        idx = chars.index(c) + 1
        if idx < len(chars):
            password[i] = chars[idx]
            break
        password[i] = 'a'
        i -= 1
    return ''.join(password)

def valid_password(password):
    if any(c in password for c in "iol"):
        return False
    
    has_straight = False
    for i in range(len(password) - 2):
        a, b, c = ord(password[i]), ord(password[i+1]), ord(password[i+2])
        if a + 1 == b and b + 1 == c:
            has_straight = True
            break
    
    if not has_straight:
        return False
    
    pairs = 0
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i+1]:
            pairs += 1
            i += 2
            if pairs >= 2:
                return True
        else:
            i += 1
    return pairs >= 2

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")