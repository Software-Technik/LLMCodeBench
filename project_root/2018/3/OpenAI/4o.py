def extract_coordinates(iterable):
    for label in iterable:
        number, _, specs = label.partition(" @ ")
        coor, _, size = specs.partition(": ")
        x, y = coor.split(",")
        width, height = size.strip().split("x")
        yield number[1:], (int(x), int(y)), (int(width), int(height))

def day3_part1(f):
    used = {}
    for _, (x, y), (width, height) in extract_coordinates(f):
        for x1 in range(x, x+width):
            for y1 in range(y, y+height):
                used[(x1, y1)] = used.get((x1, y1), 0) + 1
    return sum(1 for square in used.values() if square >= 2)

def day3_part2(f):
    claims_on_square = {}
    labels = {}
    for number, (x, y), (width, height) in extract_coordinates(f):
        labels[number] = True
        for x1 in range(x, x+width):
            for y1 in range(y, y+height):
                if (x1, y1) in claims_on_square:
                    for claim in claims_on_square[(x1, y1)]:
                        labels[claim] = False
                    labels[number] = False
                else:
                    claims_on_square[(x1, y1)] = []
                claims_on_square[(x1, y1)].append(number)
    
    return next(claim for claim, no_overlap in labels.items() if no_overlap)

if __name__ == "__main__":
    import sys
    inout_strings = sys.argv[1]
    with open(inout_strings) as f:
        data = f.read().strip().splitlines()

    overlap_squares = day3_part1(data)
    claim_without_overlap = day3_part2(data)

    sys.stdout.write(f"{overlap_squares} {claim_without_overlap}")