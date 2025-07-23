import sys

def part1(data):
    N = len(data[0])
    gamma = 0
    epsilon = 0

    for n in range(N):
        count0 = 0
        for line in data:
            if line[n] == '0':
                count0 += 1
        count1 = len(data) - count0
        gamma <<= 1
        epsilon <<= 1
        if count0 < count1:
            gamma += 1
        else:
            epsilon += 1

    return gamma * epsilon

def part2(data):
    N = len(data[0])

    def filter_data(d, position, criteria):
        if len(d) <= 1:
            return d
        count0 = 0
        for x in d:
            if x[position] == '0':
                count0 += 1
        count1 = len(d) - count0
        v = criteria(count0, count1)
        return [x for x in d if x[position] == v]

    lst = data.copy()
    for i in range(N):
        lst = filter_data(lst, i, lambda c0, c1: '0' if c0 > c1 else '1')
        if len(lst) == 1:
            break
    oxygen = int(lst[0], 2)

    lst = data.copy()
    for i in range(N):
        lst = filter_data(lst, i, lambda c0, c1: '0' if c0 <= c1 else '1')
        if len(lst) == 1:
            break
    co2 = int(lst[0], 2)

    return co2 * oxygen

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")