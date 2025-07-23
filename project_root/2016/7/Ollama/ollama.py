import sys
import re

def is_abba(s):
    for i in range(len(s) - 3):
        if s[i] + s[i+1] == s[i+3] + s[i+2] and s[i] != s[i+1]:
            return True
    return False

def is_ababab(sup, hyp):
    for i in range(len(sup) - 2):
        if sup[i] == sup[i+2] and sup[i] != sup[i+1] and sup[i:i+3].replace('','').find(sup[i]+sup[i+1]) > 0:
            return True
    return False

def part1(data):
    net_data = [re.split(r'\[|\]', line.strip()) for line in data]
    supernet = [' '.join([part[::2] for part in line if part != '']) for line in net_data]
    hypernet = [' '.join([part[1::2] for part in line if part != '']) for line in net_data]
    return sum(is_abba(sup) and not is_abba(hyp) for sup, hyp in zip(supernet, hypernet))

def part2(data):
    net_data = [re.split(r'\[|\]', line.strip()) for line in data]
    supernet = [' '.join([part[::2] for part in line if part != '']) for line in net_data]
    hypernet = [' '.join([part[1::2] for part in line if part != '']) for line in net_data]
    return sum(is_ababab(sup, hyp) for sup, hyp in zip(supernet, hypernet))

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as infile:
        data = infile.readlines()
    sys.stdout.write(f"{part1(data)} {part2(data)}\n")