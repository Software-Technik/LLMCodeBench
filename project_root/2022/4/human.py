import sys

def part1(data):
    r = 0
    for line in data:
        s1, s2 = map(lambda section: tuple(map(int, section.split("-"))), line.split(","))
        # if s1[1] - s1[0] > s2[1] - s2[0]:
        #     s1, s2 = s2, s1
        # if s2[0] <= s1[0] and s1[1] <= s2[1]:
        #     r += 1
        if (s1[0] - s2[0]) * (s1[1] - s2[1]) <= 0:
            r += 1
    return r

def part2(data):
    r = 0
    for line in data:
        s1, s2 = map(lambda section: tuple(map(int, section.split("-"))), line.split(","))
        # if s1[0] > s2[0]:
        #     s1, s2 = s2, s1
        # if s1[1] >= s2[0]:
        #     r += 1
        if s2[0] <= s1[0] <= s2[1] or s1[0] <= s2[0] <= s1[1]:
            r += 1
    return r

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")