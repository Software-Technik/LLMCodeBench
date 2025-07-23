import sys
from itertools import groupby

def part1(data):
    c = next_password(data[0])
    while not valid_password(c):
        c = next_password(c)
    return c

def part2(data):
    c = part1([data[0]])
    return part1([c])

def next_password(password):
    password = list(password)
    for i in range(len(password) - 1, -1, -1):
        if password[i] == 'z':
            password[i] = 'a'
        else:
            password[i] = chr(ord(password[i]) + 1)
            break
    return "".join(password)

def valid_password(password):
    rule1 = any(char * 3 in password for char in 'abcdefghjkmnpqrstuvwxyz')
    rule2 = all(char not in 'iol' for char in password)
    rule3 = len(set(list(groupby(password)))) > 1
    return rule1 and rule2 and rule3

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")