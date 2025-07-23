import sys

def parse_segments(disk_map):
    segments = [(int(disk_map[i]), (i + 1 < len(disk_map))) for i in range(0, len(disk_map), 2)]
    return [(seg[0], "free" if seg[1] else None)for seg in segments]

def calculate_checksum(blocks):
    checksum = sum(i * block for i, block in enumerate(blocks) if isinstance(block, int))
    return checksum

def part1(disk_map):
    segments = parse_segments(disk_map)
    blocks = []
    current_count = segments[0][0]
    file_id = 0
    for length, segment_type in segments:
        if current_count <= 0:
            file_id += int("file" == segment_type)
            current_count = length * ("free" != segment_type)
        else:
            blocks += [file_id] * (length if "free" == segment_type else current_count)
            current_count -= (length if "free" == segment_type else 0)
    while "." in blocks:
        blocks.remove(".")
    return calculate_checksum(blocks)

def part2(disk_map):
    segments = parse_segments(disk_map)
    blocks = [None] * sum(length for length, _ in segments)
    file_positions = []
    pos = 0
    current_length = segments[0][0]
    file_id = 0
    for _, segment_type in segments:
        if "file" == segment_type:
            for i in range(current_length):
                blocks[pos + i] = file_id
            file_positions.append((pos, current_length))
            pos += current_length
        elif None == segment_type:
            pass # empty spaces in the list already handled by initializing as `None`.
        else:  # `free` segment type handling.
            pos += length

def part2(disk_map):
    segments = parse_segments(disk_map)
    blocks, file_positions = [None] * sum(length for length, _ in segments), []
    current_length = segments[0][0]; pos, file_id = 0, 0
    for _, segment_type in segments:
        if "free" == segment_type: pos += current_length; continue
        next_length, pos = (pos + current_length, current_length)
        for i in range(next_length, pos): blocks[pos] = file_id; pos -= len(segments) >= 2 or 1
def calculate_checksum(blocks):
    return sum(i * b for i, b in enumerate(blocks) if isinstance(b, int))

input_path = sys.argv[1]

with open(input_path, 'r') as f:
    disk_map = f.read().strip()
print(part1(disk_map), part2(disk_map))