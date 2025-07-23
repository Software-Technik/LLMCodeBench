import sys

def parse(line):
    s, groups = line.strip().split(" ")
    lookup = {"#": 2, "?": 1, ".": 0}
    return tuple(lookup[char] for char in s), tuple(int(g) for g in groups.split(","))

def count_dp(data, blocks):
    n = len(data)
    m = len(blocks)
    prefix = [0] * (n+1)
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + (1 if data[i-1]==0 else 0)
    
    suffix_has_two = [False] * (n+1)
    for i in range(n-1, -1, -1):
        suffix_has_two[i] = (data[i] == 2) or suffix_has_two[i+1]
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(n+1):
        if i == n:
            dp[i][m] = 1
        else:
            dp[i][m] = 1 if not suffix_has_two[i] else 0

    for j in range(m-1, -1, -1):
        for i in range(n-1, -1, -1):
            total = 0
            if data[i] == 0 or data[i] == 1:
                total += dp[i+1][j]
            if data[i] == 1 or data[i] == 2:
                L = blocks[j]
                end = i + L
                if end <= n:
                    if prefix[end] - prefix[i] == 0:
                        if end < n:
                            if data[end] != 2:
                                total += dp[end+1][j+1]
                        else:
                            total += dp[end][j+1]
            dp[i][j] = total
            
    return dp[0][0]

def part1(text):
    data = [parse(line) for line in text.strip().splitlines()]
    return sum(count_dp(chars, blocks) for chars, blocks in data)

def part2(text):
    data = [parse(line) for line in text.strip().splitlines()]
    total = 0
    for chars, blocks in data:
        new_chars = ((chars + (1,)) * 5)[:-1]
        new_blocks = blocks * 5
        total += count_dp(new_chars, new_blocks)
    return total

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    text = f.read()
sys.stdout.write(f"{part1(text)} {part2(text)}")