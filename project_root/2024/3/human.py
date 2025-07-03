import sys
import re


def part1(line):
    matches = re.findall(r"mul\((\d+),(\d+)\)", line)

    ans = 0
    for match in matches:
        ans += int(match[0]) * int(match[1])

    return ans


def part2(line):
    matches = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", line)

    enabled = True

    ans = 0
    for match in matches:
        if match[2] == "" and enabled:
            ans += int(match[0]) * int(match[1])
        else:
            if match[2] == "do()":
                enabled = True
            else:
                enabled = False

    return ans


input_path = sys.argv[1]
with open(input_path) as fin:
    line = fin.read().strip()
    print(part1(line), part2(line))
