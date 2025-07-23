import sys
import re

def is_abba(s):
    for i in range(len(s) - 3):
        a, b, c, d = s[i], s[i+1], s[i+2], s[i+3]
        if a == d and b == c and a != b:
            return True
    return False

def is_ababab(sup, hyp):
    for i in range(len(sup) - 2):
        a, b, c = sup[i], sup[i+1], sup[i+2]
        if a == c and a != b:
            bab = b + a + b
            if bab in hyp:
                return True
    return False

def part1(data):
    count = 0
    for line in data:
        parts = re.split(r'\[|\]', line.strip())
        sup = ' '.join(parts[::2])
        hyp = ' '.join(parts[1::2])
        if is_abba(sup) and not is_abba(hyp):
            count += 1
    return count

def part2(data):
    count = 0
    for line in data:
        parts = re.split(r'\[|\]', line.strip())
        sup = ' '.join(parts[::2])
        hyp = ' '.join(parts[1::2])
        if is_ababab(sup, hyp):
            count += 1
    return count

with open(sys.argv[1], 'r') as infile:
    data = infile.readlines()

sys.stdout.write(f"{part1(data)} {part2(data)}")