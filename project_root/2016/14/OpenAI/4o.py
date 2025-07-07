from hashlib import md5
import sys

def part1(data):
    triplets = {}
    valid_keys = set()
    index = 0
    max_check = None

    while len(valid_keys) < 64 or index < max_check:
        hex_ = md5((data + str(index)).encode()).hexdigest()

        for i in range(len(hex_) - 2):
            if hex_[i] == hex_[i + 1] == hex_[i + 2]:
                if not max_check:
                    max_check = index + 1000
                if any(hex_[i] * 5 in md5((data + str(j)).encode()).hexdigest() for j in range(index + 1, index + 1001)):
                    valid_keys.add(index)
                triplets[index] = hex_[i]
                break
        index += 1

    return sorted(valid_keys)[63]

def part2(data):
    triplets = {}
    valid_keys = set()
    index = 0
    max_check = None

    def hash2017(val):
        for _ in range(2017):
            val = md5(val.encode()).hexdigest()
        return val

    while len(valid_keys) < 64 or index < max_check:
        hex_ = hash2017(data + str(index))

        for i in range(len(hex_) - 2):
            if hex_[i] == hex_[i + 1] == hex_[i + 2]:
                if not max_check:
                    max_check = index + 1000
                if any(hex_[i] * 5 in hash2017(data + str(j)) for j in range(index + 1, index + 1001)):
                    valid_keys.add(index)
                triplets[index] = hex_[i]
                break
        index += 1

    return sorted(valid_keys)[63]

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as file:
    data = file.read().strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")