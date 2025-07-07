import sys

def part1(data):
    coords = [(idx, int(item)) for idx, item in enumerate(data)]
    _len = len(coords)

    for i in range(_len):
        pos, coord = next((p, coord) for p, coord in enumerate(coords) if coord[0] == i)
        new_pos = (pos + coord[1] + (_len - 1)) % (_len - 1)

        coords.pop(pos)
        coords.insert(new_pos, coord)

    zero_pos = next(p for p, item in enumerate(coords) if item[1] == 0)

    return sum(coords[(zero_pos + offset) % _len][1] for offset in [1000, 2000, 3000])

def part2(data):
    key = 811589153
    coords = [(idx, int(item) * key) for idx, item in enumerate(data)]
    _len = len(coords)

    for _ in range(10):
        for i in range(_len):
            pos, coord = next((p, coord) for p, coord in enumerate(coords) if coord[0] == i)
            new_pos = (pos + coord[1] + (_len - 1)) % (_len - 1)

            coords.pop(pos)
            coords.insert(new_pos, coord)

    zero_pos = next(p for p, item in enumerate(coords) if item[1] == 0)

    return sum(coords[(zero_pos + offset) % _len][1] for offset in [1000, 2000, 3000])

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")