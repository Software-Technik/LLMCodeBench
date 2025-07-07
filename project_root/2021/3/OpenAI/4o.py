import sys

def part1(data):
    N = len(data[0])

    gamma = 0
    epsilon = 0

    for n in range(N):
        count = sum(line[n] == '1' for line in data)
        gamma = (gamma << 1) | (count > len(data) / 2)
        epsilon = (epsilon << 1) | (count <= len(data) / 2)

    return gamma * epsilon

def part2(data):
    N = len(data[0])

    def filter_data(data, criteria_func):
        lst = data
        for i in range(N):
            if len(lst) == 1:
                break
            count0 = sum(1 for x in lst if x[i] == '0')
            count1 = len(lst) - count0
            target = criteria_func(count0, count1)
            lst = [x for x in lst if x[i] == target]
        return lst[0]

    oxygen = int(filter_data(data, lambda c0, c1: '0' if c0 > c1 else '1'), 2)
    co2 = int(filter_data(data, lambda c0, c1: '0' if c0 <= c1 else '1'), 2)

    return co2 * oxygen

inout_strings = sys.argv[1]
with open(inout_strings) as f:
    data = [line.strip() for line in f if line.strip()]

sys.stdout.write(f"{part1(data)} {part2(data)}")