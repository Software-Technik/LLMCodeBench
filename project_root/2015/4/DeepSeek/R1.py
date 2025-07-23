import sys
import hashlib

def part1(data):
    key = data[0]
    return find_num(key, 5)

def part2(data):
    key = data[0]
    return find_num(key, 6)

def find_num(key, digits):
    key_bytes = key.encode()
    k = digits // 2
    r = digits % 2
    i = 1
    while True:
        data = key_bytes + str(i).encode()
        digest = hashlib.md5(data).digest()
        if any(digest[j] != 0 for j in range(k)):
            i += 1
            continue
        if r == 0:
            return i
        if (digest[k] & 0xF0) == 0:
            return i
        i += 1

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")