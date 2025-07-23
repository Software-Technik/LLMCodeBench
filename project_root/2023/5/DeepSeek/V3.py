import sys

def part1(text: str) -> int:
    sections = text.split("\n\n")
    seeds = list(map(int, sections[0].split()[1:]))
    mappings = []
    for section in sections[1:]:
        mapping = []
        for line in section.splitlines()[1:]:
            if line.strip():
                mapping.append(list(map(int, line.split())))
        mappings.append(mapping)
    
    min_location = None
    for seed in seeds:
        value = seed
        for mapping in mappings:
            for dest, src, length in mapping:
                if src <= value < src + length:
                    value += dest - src
                    break
        if min_location is None or value < min_location:
            min_location = value
    return min_location

def part2(text: str) -> int:
    sections = text.split("\n\n")
    seed_ranges = list(map(int, sections[0].split()[1:]))
    seeds = [(seed_ranges[i], seed_ranges[i+1]) for i in range(0, len(seed_ranges), 2)]
    
    mappings = []
    for section in sections[1:]:
        mapping = []
        for line in section.splitlines()[1:]:
            if line.strip():
                dest, src, length = map(int, line.split())
                mapping.append((dest, src, length))
        mapping.sort(key=lambda x: x[1])
        mappings.append(mapping)
    
    for mapping in mappings:
        new_seeds = []
        for start, length in seeds:
            current_start = start
            remaining = length
            for dest, src, m_len in mapping:
                if current_start >= src + m_len:
                    continue
                if current_start < src:
                    overlap = min(src - current_start, remaining)
                    new_seeds.append((current_start, overlap))
                    current_start += overlap
                    remaining -= overlap
                    if remaining == 0:
                        break
                if remaining == 0:
                    break
                overlap_start = max(current_start, src)
                overlap_end = min(current_start + remaining, src + m_len)
                if overlap_start < overlap_end:
                    overlap_length = overlap_end - overlap_start
                    new_seeds.append((dest + (overlap_start - src), overlap_length))
                    current_start += overlap_length
                    remaining -= overlap_length
                    if remaining == 0:
                        break
            if remaining > 0:
                new_seeds.append((current_start, remaining))
        seeds = new_seeds
    
    return min(start for start, _ in seeds)

with open(sys.argv[1]) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")