import sys

def part1(data):
    if not data:
        return 0
    N = len(data[0])
    counts = [0] * N
    for line in data:
        for i, bit in enumerate(line):
            if bit == '1':
                counts[i] += 1
    gamma = 0
    epsilon = 0
    n = len(data)
    for c in counts:
        gamma <<= 1
        epsilon <<= 1
        if c > n - c:
            gamma += 1
        else:
            epsilon += 1
    return gamma * epsilon

def part2(data):
    if not data:
        return 0
    N = len(data[0])
    
    lst = data
    for i in range(N):
        if len(lst) == 1:
            break
        groups = [[], []]
        for num in lst:
            groups[1 if num[i]=='1' else 0].append(num)
        if len(groups[1]) >= len(groups[0]):
            lst = groups[1]
        else:
            lst = groups[0]
    oxygen = int(lst[0], 2)

    lst = data
    for i in range(N):
        if len(lst) == 1:
            break
        groups = [[], []]
        for num in lst:
            groups[1 if num[i]=='1' else 0].append(num)
        if len(groups[0]) <= len(groups[1]):
            lst = groups[0]
        else:
            lst = groups[1]
    co2 = int(lst[0], 2)
    
    return oxygen * co2

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")