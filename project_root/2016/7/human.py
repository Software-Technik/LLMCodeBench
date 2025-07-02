import sys
import re

inout_strings = sys.argv[1]

with open(inout_strings, 'r') as infile:
    addresses = infile.readlines()

addresses_separated = [re.split(r'\[|\]', line.strip()) for line in addresses]

supernet = [' '.join(line[::2]) for line in addresses_separated]
hypernet = [' '.join(line[1::2]) for line in addresses_separated]


def is_abba(line):
    return any(a+b == d+c and a != b
               for a, b, c, d in zip(line, line[1:], line[2:], line[3:]))

def is_ababab(sup, hyp):
    return any(a == c and a != b and b+a+b in hyp
               for a, b, c in zip(sup, sup[1:], sup[2:]))



def part1(data):
    addresses_separated = [re.split(r'\[|\]', line.strip()) for line in data]

    supernet = [' '.join(line[::2]) for line in addresses_separated]
    hypernet = [' '.join(line[1::2]) for line in addresses_separated]

    return sum(is_abba(sup) and not is_abba(hyp)
                     for sup, hyp in zip(supernet, hypernet))

def part2(data):
    addresses_separated = [re.split(r'\[|\]', line.strip()) for line in data]

    supernet = [' '.join(line[::2]) for line in addresses_separated]
    hypernet = [' '.join(line[1::2]) for line in addresses_separated]

    return sum(is_ababab(sup, hyp)
                for sup, hyp in zip(supernet, hypernet))

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.readlines()

sys.stdout.write(f"{part1(data)} {part2(data)}") 
