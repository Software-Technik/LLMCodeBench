import sys

def part1(disk_map):
    disk_segments = []
    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
        disk_segments.extend([(file_length, i // 2), (free_length, ".")])

    blocks = []
    for length, id_or_dot in disk_segments:
        if length > 0:
            blocks.extend([id_or_dot] * length)

    blocks = [block for block in blocks if block != "."]
    return sum(i * block for i, block in enumerate(blocks))

def part2(disk_map):
    disk_segments = []
    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
        disk_segments.append((file_length, None, i // 2))
        if free_length:
            disk_segments.append((free_length, "free", None))

    pos = 0
    free_spaces = []
    file_positions = []

    for length, segment_type, file_id in disk_segments:
        if segment_type == "free":
            if not free_spaces or free_spaces[-1][0] + free_spaces[-1][1] != pos:
                free_spaces.append((pos, length))
            else:
                free_spaces[-1] = (free_spaces[-1][0], free_spaces[-1][1] + length)
        elif length > 0:
            file_positions.append((pos, length, file_id))
        pos += length

    for start_pos, file_size, file_id in reversed(file_positions):
        for space_index in range(len(free_spaces)):
            space_pos, space_size = free_spaces[space_index]
            if space_pos < start_pos and file_size <= space_size:
                free_spaces[space_index] = (space_pos + file_size, space_size - file_size)
                break

    blocks = [None] * pos
    for start_pos, file_size, file_id in file_positions:
        for j in range(file_size):
            blocks[start_pos + j] = file_id

    return sum(i * block for i, block in enumerate(filter(None, blocks)))

input_path = sys.argv[1]

with open(input_path, "r") as file:
    disk_map = file.read().strip()
    print(part1(disk_map), part2(disk_map))