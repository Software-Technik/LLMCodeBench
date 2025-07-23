import collections
import sys

def extract_coordinates(iterable):
    for label in iterable:
        number, _, specs = label.partition(" @ ")
        coor, _, size = specs.partition(": ")
        x, y = coor.split(",")
        width, height = size.strip().split("x")
        yield number[1:], (int(x), int(y)), (int(width), int(height))

def day3_part1(f):
    used = collections.defaultdict(int)
    for _, (x, y), (width, height) in extract_coordinates(f):
        for x1 in range(x, x + width):
            for y1 in range(y, y + height):
                used[(x1, y1)] += 1
    return sum(1 for count in used.values() if count >= 2)

def day3_part2(f):
    claims_on_square = collections.defaultdict(list)
    labels = {}
    for number, (x, y), (width, height) in extract_coordinates(f):
        labels[number] = True
        for x1 in range(x, x + width):
            for y1 in range(y, y + height):
                claims_on_square[(x1, y1)].append(number)
                if len(claims_on_square[(x1, y1)]) > 1:
                    for claim in claims_on_square[(x1, y1)]:
                        labels[claim] = False
    return next(claim for claim, no_overlap in labels.items() if no_overlap)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        data_lines = f.read().strip().splitlines()
    overlap_squares = day3_part1(data_lines)
    claim_without_overlap = day3_part2(data_lines)
    sys.stdout.write(f"{overlap_squares} {claim_without_overlap}")