import sys
def part1(text: str) -> int:
    mappings = []
    sections = text.split("map:\n")
    seeds = list(map(int, sections[0].split("\n", maxsplit=1)[0].split(":")[1].split()))

    for part in sections[1:]:
        numbers = [list(map(int, line.split())) for line in part.splitlines() if line]
        if numbers:
            mappings.append(numbers)

    min_location = float('inf')
    for seed in seeds:
        value = seed
        for mapping in mappings:
            for dest_range, src_range, length in mapping:
                if src_range <= value <= src_range + length - 1:
                    value += dest_range - src_range
                    break
        min_location = min(min_location, value)

    return min_location

def get_ranges(istart: int, ilength: int, mappings: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    ranges = []
    iend = istart + ilength
    for dest_start, src_start, length in mappings:
        src_end = src_start + length
        if iend <= src_start:
            ranges.append((istart, iend - istart))
            return ranges
        if istart < src_start:
            ranges.append((istart, src_start - istart))
            istart = src_start

        if istart < src_end:
            new_istart = istart + (dest_start - src_start)
            iend_here = min(iend, src_end)
            ranges.append((new_istart, iend_here - istart))
            istart = src_end

    if istart < iend:
        ranges.append((istart, iend - istart))
    return ranges

def part2(text: str) -> int:
    mappings = []
    sections = text.split("map:\n")
    seeds = list(map(int, sections[0].split("\n", maxsplit=1)[0].split(":")[1].split()))
    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    for part in sections[1:]:
        numbers = [list(map(int, line.split())) for line in part.splitlines() if line]
        if numbers:
            numbers.sort(key=lambda x: x[1])
            mappings.append(numbers)

    for mapping in mappings:
        seeds = [
            rng for seed_start, seed_length in seeds
            for rng in get_ranges(seed_start, seed_length, mapping)
        ]

    return min(start for start, _ in seeds)

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")