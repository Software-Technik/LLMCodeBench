from hashlib import md5
import sys



def part1(data):
    triplets = {}
    valid_keys = set()
    index = 0

    while len(valid_keys) < 64 or index < max(valid_keys) + 1000:
        hex_ = md5((data+str(index)).encode()).hexdigest()

        found_triplet = False
        for a, b, c in zip(hex_, hex_[1:], hex_[2:]):
            if a == b == c:
                if 5*a in hex_:
                    for k, v in triplets.items():
                        if a == v and k < index <= 1000+k:
                            valid_keys.add(k)
                if not found_triplet:
                    triplets[index] = a
                    found_triplet = True
        index += 1
    return sorted(valid_keys)[63]



def part2(data):
    triplets = {}
    valid_keys = set()
    index = 0

    while len(valid_keys) < 64 or index < max(valid_keys) + 1000:
        hex_ = md5((data+str(index)).encode()).hexdigest()

        for _ in range(2016):
            hex_ = md5(hex_.encode()).hexdigest()

        found_triplet = False
        for a, b, c in zip(hex_, hex_[1:], hex_[2:]):
            if a == b == c:
                if 5*a in hex_:
                    for k, v in triplets.items():
                        if a == v and k < index <= 1000+k:
                            valid_keys.add(k)
                if not found_triplet:
                    triplets[index] = a
                    found_triplet = True
        index += 1
    return sorted(valid_keys)[63]



inout_strings = sys.argv[1]
with open(inout_strings, 'r')  as file:
    data = file.read().strip()


sys.stdout.write(f"{part1(data)} {part2(data)}")  