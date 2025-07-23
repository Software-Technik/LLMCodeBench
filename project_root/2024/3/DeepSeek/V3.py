import sys
import re

def part1(line):
    ans = 0
    for match in re.finditer(r"mul\((\d+),(\d+)\)", line):
        ans += int(match.group(1)) * int(match.group(2))
    return ans

def part2(line):
    ans = 0
    enabled = True
    for match in re.finditer(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", line):
        if match.group(3):
            enabled = match.group(3) == "do()"
        elif enabled:
            ans += int(match.group(1)) * int(match.group(2))
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    line = fin.read().strip()
    print(part1(line), part2(line))