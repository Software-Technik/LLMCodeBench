import collections
import sys

def extract_coordinates(iterable) -> tuple:
    for label in iterable:
        number, _, specs = label.partition(" @ ")
        coor, _, size = specs.partition(": ")
        x, y = coor.split(",")
        width, height = size.strip().split("x")
        yield number[1:], (int(x), int(y)), (int(width), int(height))

def day3_part1(claims):
    seen = set()
    overlaps = set()
    for _, (x, y), (width, height) in claims:
        for x1 in range(x, x+width):
            for y1 in range(y, y+height):
                coord = (x1, y1)
                if coord in seen:
                    overlaps.add(coord)
                else:
                    seen.add(coord)
    return len(overlaps), overlaps

def day3_part2(claims, overlaps):
    for number, (x, y), (width, height) in claims:
        if not any((x1, y1) in overlaps for x1 in range(x, x+width) for y1 in range(y, y+height)):
            return number

if __name__ == "__main__":
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = f.read()
    data_lines = data.strip().splitlines()
    claims = list(extract_coordinates(data_lines))
    overlap_squares, overlaps = day3_part1(claims)
    claim_without_overlap = day3_part2(claims, overlaps)
    sys.stdout.write(f"{overlap_squares} {claim_without_overlap}")