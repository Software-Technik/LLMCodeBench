import sys

def part1(disk_map):
    file_lengths = []
    for a, b in zip(disk_map[0::2], disk_map[1::2] + '0'):
        l = int(a)
        if l:
            file_lengths.append(l)
    checksum = 0
    start = 0
    for fid, l in enumerate(file_lengths):
        checksum += fid * (l * start + l * (l - 1) // 2)
        start += l
    return checksum

def part2(disk_map):
    disk_segments = []
    for i in range(0, len(disk_map), 2):
        f = int(disk_map[i])
        disk_segments.append(("file", f))
        if i+1 < len(disk_map):
            g = int(disk_map[i+1])
            if g: disk_segments.append(("free", g))
    blocks = []
    file_positions = []
    pos = 0
    fid = 0
    for typ, l in disk_segments:
        if typ=="file":
            blocks += [fid]*l
            file_positions.append((pos, l, fid))
            fid+=1
        else:
            blocks += [None]*l
        pos+=l
    free_spaces = []
    i = 0
    n = len(blocks)
    while i<n:
        if blocks[i] is None:
            s=i
            while i<n and blocks[i] is None: i+=1
            free_spaces.append([s, i-s])
        i+=1
    for s_pos, size, fid in reversed(file_positions):
        for fs in free_spaces:
            if fs[0]<s_pos and size<=fs[1]:
                for j in range(size):
                    blocks[s_pos+j] = None
                    blocks[fs[0]+j] = fid
                fs[0]+=size; fs[1]-=size
                break
    checksum = 0
    for i, b in enumerate(blocks):
        if b is not None: checksum += i*b
    return checksum

p = sys.argv[1]
d = open(p).read().strip()
print(part1(d), part2(d))