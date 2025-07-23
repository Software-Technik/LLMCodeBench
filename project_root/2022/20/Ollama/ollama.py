import sys

def solve(data, key):
    zero_pos = 0
    _len = len(data)

    coords = [(idx, int(item) * key) for idx, item in enumerate(data)]

    for coord in coords:
        pos = coordinates.index(coord)
        new_pos = (pos + coord[1] + (_len - 1)) % (_len - 1)

        del coordinates[pos]
        zero_pos -= pos < zero_pos
        coordinates.insert(new_pos, coord)
        zero_pos += new_pos < zero_pos

    return sum(coords[(zero_pos + offset) % _len][1] for offset in [1000, 2000, 3000])

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

coordinates = [(idx, int(item)) for idx, item in enumerate(data)]
print(solve(coordinates, 1))
coordinates = [(idx, int(item) * 811589153) for idx, item in enumerate(data)]
print(solve(coordinates, 811589153))