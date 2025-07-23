import sys
import re

pattern1 = re.compile(r"mul\((\d+),(\d+)\)")
pattern2 = re.compile(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))")

def part1(line):
    matches = pattern1.findall(line)
    return sum(int(a) * int(b) for a, b in matches)

def part2(line):
    matches = pattern2.findall(line)
    enabled = True
    ans = 0
    for a, b, c in matches:
        if c == '':
            if enabled:
                ans += int(a) * int(b)
        else:
            if c == "do()":
                enabled = True
            else:
                enabled = False
    return ans

input_path = sys.argv[1]
with open(input_path) as fin:
    line = fin.read().strip()
    print(part1(line), part2(line))