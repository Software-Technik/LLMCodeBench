import sys

def part1(disk_map):
    current_index = 0
    total_checksum = 0
    file_id = 0
    n = len(disk_map)
    i = 0
    while i < n:
        file_length = int(disk_map[i])
        if i+1 < n:
            free_length = int(disk_map[i+1])
        else:
            free_length = 0

        if file_length > 0:
            total_checksum += file_id * (current_index * file_length + file_length*(file_length-1)//2)
            current_index += file_length
            file_id += 1

        i += 2
    return total_checksum

def part2(disk_map):
    current_start = 0
    file_segments = []
    free_spaces = []
    file_id = 0
    n = len(disk_map)
    i = 0
    while i < n:
        file_length = int(disk_map[i])
        if i+1 < n:
            free_length = int(disk_map[i+1])
        else:
            free_length = 0

        if file_length > 0:
            file_segments.append((current_start, file_length, file_id))
            file_id += 1
        current_start += file_length

        if free_length > 0:
            free_spaces.append((current_start, free_length))
            current_start += free_length

        i += 2

    for idx in range(len(file_segments)-1, -1, -1):
        start, L, fid = file_segments[idx]
        found_index = -1
        for j in range(len(free_spaces)):
            s, size = free_spaces[j]
            if s < start and size >= L:
                found_index = j
                break
        if found_index != -1:
            s, size = free_spaces[found_index]
            file_segments[idx] = (s, L, fid)
            if size == L:
                del free_spaces[found_index]
            else:
                free_spaces[found_index] = (s+L, size-L)

    total = 0
    for (start, L, fid) in file_segments:
        total += fid * (start * L + L*(L-1)//2)
    return total

input_path = sys.argv[1]

with open(input_path, "r") as file:
    disk_map = file.read().strip()
    print(part1(disk_map), part2(disk_map))