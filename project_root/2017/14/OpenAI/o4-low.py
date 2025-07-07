import sys

def knot_hash(s, bin_out=False):
    lengths = [ord(c) for c in s] + [17,31,73,47,23]
    nums = list(range(256))
    pos = skip = 0
    for _ in range(64):
        for l in lengths:
            if l:
                rev = nums[pos:pos+l] if pos+l<=256 else nums[pos:]+nums[:(pos+l)%256]
                rev.reverse()
                for i in range(l):
                    nums[(pos+i)%256] = rev[i]
            pos = (pos + l + skip) % 256
            skip += 1
    dense = []
    for i in range(0,256,16):
        x=0
        for j in nums[i:i+16]: x^=j
        dense.append(x)
    if bin_out:
        return ''.join(f"{x:08b}" for x in dense)
    return ''.join(f"{x:02x}" for x in dense)

def main():
    data = open(sys.argv[1]).read().strip().splitlines()
    key = data[0]
    rows = [knot_hash(f"{key}-{r}", True) for r in range(128)]
    part1 = sum(r.count('1') for r in rows)
    grid = [list(map(int, row)) for row in rows]
    regions = 0
    for i in range(128):
        for j in range(128):
            if grid[i][j]:
                regions += 1
                stack = [(i,j)]
                grid[i][j] = 0
                while stack:
                    x,y = stack.pop()
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny = x+dx, y+dy
                        if 0<=nx<128 and 0<=ny<128 and grid[nx][ny]:
                            grid[nx][ny] = 0
                            stack.append((nx,ny))
    sys.stdout.write(f"{part1}\n{regions}\n")

if __name__=="__main__":
    main()