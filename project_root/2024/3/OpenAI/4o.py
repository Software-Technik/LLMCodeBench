import sys
import re

def part1(line):
    return sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", line))

def part2(line):
    matches = re.findall(r"(mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", line)

    ans = 0
    enabled = True

    for m in matches:
        if m[0] and enabled:
            ans += int(m[1]) * int(m[2])
        elif m[3] == "do()":
            enabled = True
        elif m[3] == "don't()":
            enabled = False

    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    line = fin.read().strip()
    print(part1(line), part2(line))