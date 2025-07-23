import sys

def part1(text: str) -> int:
    mappings = []
    lines = text.split("map:\n")
    seeds = list(
        map(int, lines[0].split("\n", maxsplit=1)[0].split(":", maxsplit=1)[1].split())
    )

    for split in lines[1:]:
        numbers = []
        for line in split.splitlines():
            if not line:
                break
            numbers.append(list(map(int, line.split())))
        if numbers:
            mappings.append(numbers)

    min_location = None
    for seed in seeds:
        value = seed
        for mapping in mappings:
            for dest_range, src_range, length in mapping:
                if src_range <= value <= src_range + length - 1:
                    value += dest_range - src_range
                    break
        if min_location is None or value < min_location:
            min_location = value

    return min_location

def get_ranges(
    istart: int, ilength: int, mappings: list[tuple[int, int, int]]
) -> list[tuple[int, int]]:
    ranges = []
    iend = istart + ilength - 1
    for dest_start, src_start, length in mappings:
        src_end = src_start + length - 1
        if istart < src_start:
            if iend < src_start:
                ranges.append((istart, iend - istart + 1))
                return ranges
            ranges.append((istart, src_start - istart))
            istart = src_start
        if src_start <= istart <= src_end:
            if iend <= src_end:
                new_istart = istart + (dest_start - src_start)
                ranges.append((new_istart, iend - istart + 1))
                return ranges
            new_istart = istart + (dest_start - src_start)
            ranges.append((new_istart, src_end - istart + 1))
            istart = src_end + 1
    ranges.append((istart, iend - istart + 1))
    return ranges

def part2(text: str) -> int:
    mappings = []
    lines = text.split("map:\n")
    all_seeds = list(
        map(int, lines[0].split("\n", maxsplit=1)[0].split(":", maxsplit=1)[1].split())
    )
    seeds = [(all_seeds[i], all_seeds[i + 1]) for i in range(0, len(all_seeds), 2)]
    if seeds:
        seeds.sort(key=lambda x: x[0])
        merged_seeds = []
        current_start, current_length = seeds[0]
        for i in range(1, len(seeds)):
            s, l = seeds[i]
            if current_start + current_length == s:
                current_length += l
            else:
                merged_seeds.append((current_start, current_length))
                current_start, current_length = s, l
        merged_seeds.append((current_start, current_length))
        seeds = merged_seeds

    for split in lines[1:]:
        numbers = []
        for line in split.splitlines():
            if not line:
                break
            numbers.append(list(map(int, line.split())))
        if numbers:
            numbers.sort(key=lambda x: x[1])
            mappings.append(numbers)

    for mapping in mappings:
        new_seeds = []
        for seed in seeds:
            ranges = get_ranges(seed[0], seed[1], mapping)
            new_seeds.extend(ranges)
        if not new_seeds:
            seeds = []
            continue
        new_seeds.sort(key=lambda x: x[0])
        merged_seeds = []
        current_start, current_length = new_seeds[0]
        for i in range(1, len(new_seeds)):
            s, l = new_seeds[i]
            if current_start + current_length == s:
                current_length += l
            else:
                merged_seeds.append((current_start, current_length))
                current_start, current_length = s, l
        merged_seeds.append((current_start, current_length))
        seeds = merged_seeds

    return min(start for start, _ in seeds) if seeds else 0

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")