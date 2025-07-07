import sys
import re

inout_strings = sys.argv[1]

with open(inout_strings, 'r') as infile:
    data = infile.read().splitlines()

def is_abba(line):
    return any(line[i] == line[i+3] and line[i+1] == line[i+2] and line[i] != line[i+1] 
               for i in range(len(line) - 3))

def is_ababab(sup, hyp):
    return any(sup[i] == sup[i+2] and sup[i] != sup[i+1] and sup[i+1]+sup[i]+sup[i+1] in hyp
               for i in range(len(sup) - 2))

def part1(data):
    count = 0
    for line in data:
        parts = re.split(r'\[|\]', line.strip())
        supernet = ' '.join(parts[::2])
        hypernet = ' '.join(parts[1::2])
        if is_abba(supernet) and not is_abba(hypernet):
            count += 1
    return count

def part2(data):
    count = 0
    for line in data:
        parts = re.split(r'\[|\]', line.strip())
        supernet = ' '.join(parts[::2])
        hypernet = ' '.join(parts[1::2])
        if is_ababab(supernet, hypernet):
            count += 1
    return count

sys.stdout.write(f"{part1(data)} {part2(data)}")