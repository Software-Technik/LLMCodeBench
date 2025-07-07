import sys

def has_abba(s):
    for i in range(len(s) - 3):
        a, b, c, d = s[i], s[i+1], s[i+2], s[i+3]
        if a != b and a == d and b == c:
            return True
    return False

def abas(s):
    res = set()
    for i in range(len(s) - 2):
        a, b, c = s[i], s[i+1], s[i+2]
        if a == c and a != b:
            res.add((a, b))
    return res

def parse(line):
    supernets = []
    hypernets = []
    buf = []
    in_bracket = False
    for ch in line:
        if ch == '[':
            if buf:
                supernets.append(''.join(buf)) if not in_bracket else hypernets.append(''.join(buf))
            buf = []
            in_bracket = True
        elif ch == ']':
            if buf:
                hypernets.append(''.join(buf)) if in_bracket else supernets.append(''.join(buf))
            buf = []
            in_bracket = False
        else:
            buf.append(ch)
    if buf:
        supernets.append(''.join(buf)) if not in_bracket else hypernets.append(''.join(buf))
    return supernets, hypernets

data = [line.strip() for line in open(sys.argv[1])]

count1 = 0
count2 = 0

for line in data:
    supernets, hypernets = parse(line)
    if any(has_abba(seg) for seg in supernets) and not any(has_abba(seg) for seg in hypernets):
        count1 += 1
    sup_abas = set()
    for seg in supernets:
        sup_abas |= abas(seg)
    found = False
    for a, b in sup_abas:
        bab = b + a + b
        if any(bab in seg for seg in hypernets):
            found = True
            break
    if found:
        count2 += 1

sys.stdout.write(f"{count1} {count2}")