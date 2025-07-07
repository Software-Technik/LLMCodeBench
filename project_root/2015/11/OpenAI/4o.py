import sys

def part1(data):
    c = data[0]
    while not valid_password(c := next_password(c)):
        continue
    return c

def part2(data):
    return part1([part1(data)])

def next_password(password):
    chars = "abcdefghjkmnpqrstuvwxyz"
    password = list(password)
    i = len(password) - 1
    while i >= 0:
        idx = chars.index(password[i]) + 1
        if idx == len(chars):
            password[i] = "a"
        else:
            password[i] = chars[idx]
            break
        i -= 1
    return "".join(password)

def valid_password(password):
    chars = "abcdefghijklmnopqrstuvwxyz"
    rule1 = any(password[i:i+3] in chars for i in range(len(password) - 2))
    rule2 = not any(c in password for c in "iol")
    rule3 = len({password[i] for i in range(len(password) - 1) if password[i] == password[i+1]}) > 1
    return rule1 and rule2 and rule3

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")