from hashlib import md5

def part1(data):
    valid_keys = set()
    index = 0
    while len(valid_keys) < 64 or index < max(valid_keys, default=0) + 1000:
        hex_ = md5((data + str(index)).encode()).hexdigest()
        triplets = {i: c for i in range(max(valid_keys, default=index), index) if (c := hex_[max(0, i - 999):][0]) == hex_.count(c)*3}
        valid_keys.update(
            k for k, v in triplets.items() if hex_.count(v * 5) > 0 and k < index + min(triplets)
        )
        index += 1
    return sorted(valid_keys)[63]

def part2(data):
    valid_keys = set()
    index = 0
    while len(valid_keys) < 64 or index < max(valid_keys, default=0) + 1000:
        hex_ = md5((data + str(index)).encode()).hexdigest()
        for _ in range(2016):
            hex_ = md5(hex_.encode()).hexdigest()
        triplets = {i: c for i in range(max(valid_keys, default=index), index) if (c := hex_[max(0, i - 999):][0]) == hex_.count(c)*3}
        valid_keys.update(
            k for k, v in triplets.items() if hex_.count(v * 5) > 0 and k < index + min(triplets)
        )
        index += 1
    return sorted(valid_keys)[63]

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as file:
    data = file.read().strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")