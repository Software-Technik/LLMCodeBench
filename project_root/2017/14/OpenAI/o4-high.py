import sys

def knot_hash_int(key):
    lengths = [ord(c) for c in key] + [17,31,73,47,23]
    nums = list(range(256))
    pos = skip = 0
    for _ in range(64):
        for length in lengths:
            if length > 1:
                i = pos
                j = (pos + length - 1) % 256
                for _ in range(length >> 1):
                    nums[i], nums[j] = nums[j], nums[i]
                    i = (i + 1) % 256
                    j = (j - 1) % 256
            pos = (pos + length + skip) & 255
            skip += 1
    h = 0
    for b in range(16):
        x = 0
        for i in range(b*16, b*16+16):
            x ^= nums[i]
        h = (h << 8) | x
    return h

with open(sys.argv[1]) as f:
    s = f.readline().strip()
s_dash = s + '-'
grid = [knot_hash_int(s_dash + str(i)) for i in range(128)]
ones = sum(row.bit_count() for row in grid)
g = grid[:]
regions = 0
for r in range(128):
    for c in range(128):
        if (g[r] >> (127-c)) & 1:
            regions += 1
            stack = [(r,c)]
            while stack:
                x, y = stack.pop()
                if 0 <= x < 128 and 0 <= y < 128 and ((g[x] >> (127-y)) & 1):
                    g[x] ^= (1 << (127-y))
                    stack.append((x+1,y)); stack.append((x-1,y))
                    stack.append((x,y+1)); stack.append((x,y-1))
sys.stdout.write(f"{ones}\n{regions}\n")