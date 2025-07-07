import sys

def part1(s):
    total = 0
    i = 0
    n = len(s)
    while True:
        l = s.find('(', i)
        if l == -1:
            total += n - i
            return total
        total += l - i
        r = s.find(')', l)
        a, b = s[l+1:r].split('x')
        A, B = int(a), int(b)
        total += A * B
        i = r + 1 + A

def part2_rec(s, start, end):
    total = 0
    i = start
    while i < end:
        l = s.find('(', i, end)
        if l == -1:
            total += end - i
            break
        total += l - i
        r = s.find(')', l, end)
        a, b = s[l+1:r].split('x')
        A, B = int(a), int(b)
        total += B * part2_rec(s, r+1, r+1+A)
        i = r + 1 + A
    return total

def part2(s):
    return part2_rec(s, 0, len(s))

data = open(sys.argv[1], 'r').read()
sys.stdout.write(f"{part1(data)} {part2(data)}")