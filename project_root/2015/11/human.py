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
    password = list(password)[::-1]
    add = 1
    for i in range(len(password)):
        c = password[i]
        idx = chars.index(c) + add
        add = 0
        if idx >= len(chars):
            password[i] = "a"
            add = 1
        else:
            password[i] = chars[idx]
            break
    return "".join(password[::-1])

def valid_password(password):
    chars = "abcdefghijklmnopqrstuvwxyz"
    rule1 = sum(1 for i in range(len(password) - 2) if password[i : i + 3] in chars) > 0
    rule2 = sum(1 for i in password if i in "iol") < 1
    rule3 = sum(len(list(j)) // 2 for i, j in groupby(password)) > 1
    return rule1 and rule2 and rule3

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")