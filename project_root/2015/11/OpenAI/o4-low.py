import sys

chars = "abcdefghjkmnpqrstuvwxyz"
c2i = {c:i for i,c in enumerate(chars)}
i2c = {i:c for i,c in enumerate(chars)}
invalid = set("iol")

def next_password(pw):
    idxs = [c2i[c] for c in pw]
    i = len(idxs) - 1
    while i >= 0:
        idxs[i] += 1
        if idxs[i] == len(chars):
            idxs[i] = 0
            i -= 1
        else:
            break
    return "".join(i2c[i] for i in idxs)

def valid_password(pw):
    cnt = 0
    pairs = 0
    last_pair = ''
    has_straight = False
    for i in range(len(pw)):
        if pw[i] in invalid:
            return False
        if i < len(pw) - 2:
            a, b, c = pw[i], pw[i+1], pw[i+2]
            if ord(b) == ord(a) + 1 and ord(c) == ord(b) + 1:
                has_straight = True
        if i < len(pw) - 1 and pw[i] == pw[i+1] and pw[i] != last_pair:
            pairs += 1
            last_pair = pw[i]
    return has_straight and pairs >= 2

def part1(pw):
    pw = next_password(pw)
    while not valid_password(pw):
        pw = next_password(pw)
    return pw

def part2(pw):
    return part1(part1(pw))

with open(sys.argv[1]) as f:
    start = f.read().strip()

res1 = part1(start)
res2 = part2(start)
sys.stdout.write(res1 + "\n" + res2 + "\n")