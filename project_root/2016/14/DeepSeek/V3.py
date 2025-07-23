from hashlib import md5
import sys

def part1(data):
    triplets = {}
    valid_keys = set()
    index = 0

    while len(valid_keys) < 64 or index < max(valid_keys) + 1000:
        hex_ = md5((data + str(index)).encode()).hexdigest()
        found_triplet = False
        for i in range(len(hex_) - 2):
            a, b, c = hex_[i], hex_[i+1], hex_[i+2]
            if a == b == c:
                if not found_triplet:
                    triplets[index] = a
                    found_triplet = True
                if 5 * a in hex_:
                    for k in list(triplets):
                        if triplets[k] == a and k < index <= k + 1000:
                            valid_keys.add(k)
        index += 1
    return sorted(valid_keys)[63]

def part2(data):
    triplets = {}
    valid_keys = set()
    index = 0
    md5_cache = {}

    while len(valid_keys) < 64 or index < max(valid_keys) + 1000:
        hex_ = md5_cache.get(index)
        if hex_ is None:
            hex_ = md5((data + str(index)).encode()).hexdigest()
            for _ in range(2016):
                hex_ = md5(hex_.encode()).hexdigest()
            md5_cache[index] = hex_
        
        found_triplet = False
        for i in range(len(hex_) - 2):
            a, b, c = hex_[i], hex_[i+1], hex_[i+2]
            if a == b == c:
                if not found_triplet:
                    triplets[index] = a
                    found_triplet = True
                if 5 * a in hex_:
                    for k in list(triplets):
                        if triplets[k] == a and k < index <= k + 1000:
                            valid_keys.add(k)
        index += 1
    return sorted(valid_keys)[63]

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as file:
    data = file.read().strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")