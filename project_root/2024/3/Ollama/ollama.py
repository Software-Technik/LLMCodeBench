import re
import sys

def multiply(match):
    a, b = map(int, match.groups())
    return a * b

def optimize_line(line):
    instructions = iter(re.findall(r'(\(enable\)|\(disable\))', line))
    actions = [part for part in re.split(r'\s*\(enable\)\s*|\s*\(disable\)\s*', line) if part]

    result1 = sum((multiply(m) for m in re.finditer(r'mul\((\d+),(\d+)\)', line)))
    result2 = 0
    enabled = True

    for action in actions:
        result2 += sum((enabled and multiply(m) for m in re.finditer(r'mul\((\d+),(\d+)\)', action)))
        if next(instructions, None) == '(disable)':
            enabled = False
        else:
            enabled = True

    return result1, result2

input_path = sys.argv[1]
with open(input_path) as fin:
    line = fin.read().strip()
    print(*optimize_line(line))