import sys
import hashlib

def part1(data):
    key = data[0]
    return find_num(key, 5)

def part2(data):
    key = data[0]
    return find_num(key, 6)

def find_num(key, digits):
    i = 1
    while True:
        if hashlib.md5((key + str(i)).encode()).hexdigest().startswith("0" * digits):
            return i
        i += 1

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")