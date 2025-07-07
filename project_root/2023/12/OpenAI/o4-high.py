import sys
def parse(line):
    s, groups = line.strip().split()
    lookup = {'.':0,'?':1,'#':2}
    return [lookup[c] for c in s], [int(x) for x in groups.split(',')]
def solve_line(data, blocks):
    n = len(data)
    m = len(blocks)
    zeros = [0]*(n+1)
    for i in range(n):
        zeros[i+1] = zeros[i] + (data[i]==0)
    fixed = [0]*(n+1)
    for i in range(n-1,-1,-1):
        fixed[i] = fixed[i+1] + (data[i]==2)
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[n][m] = 1
    for i in range(n-1,-1,-1):
        dp[i][m] = 1 if fixed[i]==0 else 0
        for j in range(m-1,-1,-1):
            v = dp[i+1][j] if data[i]<2 else 0
            L = blocks[j]
            end = i+L
            if end<=n and zeros[end]-zeros[i]==0:
                if end==n:
                    if j+1==m: v+=1
                elif data[end]<2:
                    v+=dp[end+1][j+1]
            dp[i][j] = v
    return dp[0][0]
def main():
    text = open(sys.argv[1]).read()
    lines = text.strip().splitlines()
    db = [parse(l) for l in lines]
    part1 = 0
    for data, blocks in db:
        part1 += solve_line(data, blocks)
    part2 = 0
    for data, blocks in db:
        d = (data + [1]) * 5
        d = d[:-1]
        part2 += solve_line(d, blocks * 5)
    sys.stdout.write(f"{part1} {part2}")
if __name__ == "__main__":
    main()