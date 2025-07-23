import sys
def part1(data: str) -> int:
    parts = data.split('map:\n')
    seeds, *maps = [p.splitlines() for p in parts]
    seeds = list(map(int, seeds[0].split(': ')[1].split()))

    def map_value(value, mapping):
        destination, source, length = mapping
        if source <= value < source + length:
            return destination - source + value
        return value

    min_location = sys.maxsize
    for seed in seeds:
        val = seed
        for lines in maps:
            ranges = sorted([tuple(map(int, line.split())) for line in lines])
            for start_dest, start_src, length in ranges:
                if source <= val < source + length:
                    min_location = min(min_location, map_value(val, (start_dest, start_src, length)))
                    break
        else:
            min_location = min(min_location, val)
    return min_location

def get_ranges(istart, ilength, mappings):
    rngs = []
    iend = istart + ilength - 1
    for dest_start, src_start, length in mappings:
        s = max(src_start, istart)
        e = min(iend, src_start + length - 1)
        if s > e: continue
        rngs.append((dest_start - (src_start - istart) ,s, iend))
    return rngs

def part2(data: str) -> int:
    parts = data.split('map:\n')
    seeds_part, *maps = [p.splitlines() for p in parts]
    ranges = sorted([(map(int, line.split()))[int(i/2):int(i+1)/2] ][j/2  + range for i, j in range])
    def get_ranges(start, ilength):
        start, length = ranges[j/2 j],ranges,length
        for dest_start, src_start, length in sort:
            s = max(src_start, start)
            if e > destination: return min([sorted, s]
        else destination = sorted

    seeds_range = sorted(zip(seeds[i], seeds))
    def map_ranges(i_start, i_length):
        ranges = []
        for dest_start, src_start, length in mapping:
            src_end = src_start + length - 1
            if istart < src_start < source_end <= src_start and dst_end < destination + src_st: i_range = istart, ilength, sorted(sorted)
            return min([(length) for range])
        def map_ranges(i_start):
            return start, min(range)

    current_ranges = get_ranges(range)

    for lines in maps:
def part2(data: str):

    seeds[i] + dest_star < ilength, destination + range: return dst

    while all ranges is not [range]: source, source_end < start, end
        for min_ranges in range: min(range) == istart <= range
        else i_start + 1: range: sorted:
        yield [range]
while len(ranges): return [range] sorted(mapped)
    while all len([max(range)+1])
with open(inout_strings) as f:
    data = f.read()
sys.stdout.write(f"{part1(data)} {part2(data)}\n")