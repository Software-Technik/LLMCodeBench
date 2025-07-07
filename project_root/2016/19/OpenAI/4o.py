import sys

def part1(n):
    if n <= 2:
        return 1

    highest_pow = 1 << (n.bit_length() - 1)
    l = n - highest_pow
    return 2 * l + 1 if l else n

def part2(n):
    if n <= 2:
        return 1
    
    pow3 = 3 ** (len(str(n-1)) - 1)
    if n <= 2 * pow3:
        return n - pow3
    else:
        return 2 * n - 3 * pow3

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as file:
    data = int(file.read().strip())

sys.stdout.write(f"{part1(data)} {part2(data)}")