import sys

def part1(disk_map):
    disk_segments = []
    disk_map = disk_map.split()
    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
        disk_segments.append(("file", file_length))
        if free_length > 0:
            disk_segments.append(("free", free_length))

    blocks = []
    file_id = 0
    for segment, length in disk_segments:
        if segment == "file":
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            blocks.extend(["."] * length)

    left, right = 0, len(blocks) - 1
    while left < right:
        while left < len(blocks) and blocks[left] != ".":
            left += 1
        while right >= 0 and blocks[right] == ".":
            right -= 1
        if left < right:
            blocks[left], blocks[right] = blocks[right], blocks[left]

    checksum = sum(i * block for i, block in enumerate(blocks) if block != ".")
    return checksum

def part2(disk_map):
    disk_segments = []
    disk_map = disk_map.split()
    for i in range(0, len(disk_map), 2):
        file_length = int(disk_map[i])
        free_length = int(disk_map[i + 1]) if i + 1 < len(disk_map) else 0
        disk_segments.append(("file", file_length))
        if free_length > 0:
            disk_segments.append(("free", free_length))

    blocks = []
    file_positions = []
    file_id = 0
    pos = 0
    for segment, length in disk_segments:
        if segment == "file":
            blocks.extend([file_id] * length)
            file_positions.append((pos, length, file_id))
            pos += length
            file_id += 1
        else:
            blocks.extend([None] * length)
            pos += length

    free_spaces = []
    current_pos = 0
    while current_pos < len(blocks):
        if blocks[current_pos] is None:
            start = current_pos
            while current_pos < len(blocks) and blocks[current_pos] is None:
                current_pos += 1
            free_spaces.append((start, current_pos - start))
        current_pos += 1

    for file_index in range(len(file_positions) - 1, -1, -1):
        start_pos, file_size, file_id = file_positions[file_index]
        for space_index in range(len(free_spaces)):
            space_pos, space_size = free_spaces[space_index]
            if space_pos < start_pos and file_size <= space_size:
                blocks[start_pos:start_pos + file_size] = [None] * file_size
                blocks[space_pos:space_pos + file_size] = [file_id] * file_size
                free_spaces[space_index] = (space_pos + file_size, space_size - file_size)
                break

    checksum = sum(i * block for i, block in enumerate(blocks) if block is not None)
    return checksum

input_path = sys.argv[1]
with open(input_path, "r") as file:
    disk_map = file.read().strip()
    print(part1(disk_map), part2(disk_map))