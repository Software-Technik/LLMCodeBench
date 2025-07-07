import sys

def knot_hash(s, bin_out=False):
    lengths = [ord(c) for c in s] + [17,31,73,47,23]
    n = 256
    nums = list(range(n))
    pos = skip = 0
    for _ in range(64):
        for length in lengths:
            if length > n: continue
            end = pos + length
            if end <= n:
                nums[pos:end] = reversed(nums[pos:end])
            else:
                wrap = end % n
                tmp = nums[pos:] + nums[:wrap]
                tmp.reverse()
                l = n - pos
                nums[pos:] = tmp[:l]
                nums[:wrap] = tmp[l:]
            pos = (pos + length + skip) % n
            skip += 1
    dense = []
    for i in range(0, n, 16):
        x = 0
        for v in nums[i:i+16]:
            x ^= v
        dense.append(x)
    if bin_out:
        return ''.join(f'{x:08b}' for x in dense)
    return ''.join(f'{x:02x}' for x in dense)

def create_grid(key):
    g = [[0]*128 for _ in range(128)]
    for r in range(128):
        row = g[r]
        bh = knot_hash(f'{key}-{r}', True)
        for c, ch in enumerate(bh):
            if ch == '1':
                row[c] = 1
    return g

def count_regions(g):
    regions = 0
    for i in range(128):
        for j in range(128):
            if g[i][j]:
                regions += 1
                stack = [(i,j)]
                g[i][j] = 0
                while stack:
                    x, y = stack.pop()
                    if x > 0 and g[x-1][y]:
                        g[x-1][y] = 0; stack.append((x-1,y))
                    if x < 127 and g[x+1][y]:
                        g[x+1][y] = 0; stack.append((x+1,y))
                    if y > 0 and g[x][y-1]:
                        g[x][y-1] = 0; stack.append((x,y-1))
                    if y < 127 and g[x][y+1]:
                        g[x][y+1] = 0; stack.append((x,y+1))
    return regions

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        key = f.readline().strip()
    grid = create_grid(key)
    used = sum(sum(row) for row in grid)
    regions = count_regions(grid)
    sys.stdout.write(f"{used}\n{regions}\n")