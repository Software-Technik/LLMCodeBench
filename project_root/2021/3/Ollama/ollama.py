import sys

def part1(data):
    N = len(data[0])
    gamma, epsilon = 0, 0

    for n in range(N):
        count0 = sum(line[n] == '0' for line in data)
        count1 = len(data) - count0
        gamma = (gamma << 1) | (count0 < count1)
        epsilon = (epsilon << 1) | (count0 > count1)

    return gamma * epsilon

def part2(data):
    N = len(data[0])
    most_common = lambda lst, position: '0' if sum(line[position] == '0' for line in lst) > len(lst) / 2 else '1'
    least_common = lambda lst, position: '0' if sum(line[position] == '0' for line in lst) <= len(lst) / 2 else '1'

    def filter_by_criteria(data, criteria):
        filtered_data = data.copy()
        for i in range(N):
            if len(filtered_data) <= 1:
                break
            filtered_data = [line for line in filtered_data if line[i] == criteria(filtered_data, i)]
        return int(filtered_data[0], 2)

    oxygen = filter_by_criteria(data, most_common)
    co2 = filter_by_criteria(data, least_common)

    return oxygen * co2

data = [line.strip() for line in sys.stdin if line.strip()]
sys.stdout.write(f"{part1(data)} {part2(data)}")