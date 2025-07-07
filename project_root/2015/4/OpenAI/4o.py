import sys
import hashlib

def part1(data):
    key = data[0]
    return find_num(key, 5)

def part2(data):
    key = data[0]
    return find_num(key, 6)

def find_num(key, digits):
    zeros = "0" * digits
    i = 1
    while True:
        md5_hash = hashlib.md5()
        md5_hash.update(f"{key}{i}".encode())
        if md5_hash.hexdigest().startswith(zeros):
            return i
        i += 1

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")