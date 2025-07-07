import sys
data = open(sys.argv[1]).read().strip()
n = len(data)
file_lengths = []
orig = []
free = []
pos = 0
for i in range(0, n, 2):
    fl = ord(data[i]) - 48
    orig.append(pos)
    file_lengths.append(fl)
    pos += fl
    if i + 1 < n:
        fr = ord(data[i + 1]) - 48
        if fr:
            free.append([pos, fr])
            pos += fr
part1 = 0
cur = 0
for fid, fl in enumerate(file_lengths):
    if fl:
        e = cur + fl - 1
        part1 += fid * (cur + e) * fl // 2
        cur = e + 1
new = orig[:]
for fid in range(len(file_lengths) - 1, -1, -1):
    fl = file_lengths[fid]
    if fl:
        o = orig[fid]
        for j in range(len(free)):
            sp, sl = free[j]
            if sp < o and sl >= fl:
                new[fid] = sp
                free[j][0] = sp + fl
                free[j][1] = sl - fl
                break
part2 = 0
for fid, fl in enumerate(file_lengths):
    if fl:
        fs = new[fid]
        e = fs + fl - 1
        part2 += fid * (fs + e) * fl // 2
print(part1, part2)