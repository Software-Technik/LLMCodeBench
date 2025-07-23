import sys
import re

pattern = re.compile(r'\((\d+)x(\d+)\)')

def part1(data):
    start, end = 0, len(data)
    res = len(data)
    while True:
        m = pattern.search(data[start:end])
        if not m: break
        l, t = map(int, m.groups())
        start += m.end()
        end -= (len(data) - start + 1)
        res -= ((m.start() - start) * (t - 1))
    return res

def part2(data):
    start, end = 0, len(data)
    res = len(data)
    while True:
        m = pattern.search(data[start:end])
        if not m: break
        l, t = map(int, m.groups())
        sub_len = part2(data[m.end():m.end() + l])
        start += m.end()
        end -= (len(data) - start + 1)
        res -= ((m.start() - start ) * (t - 1)) * len((data[start:m.end()]))
        res += t* sub_len
    return res

with open(sys.argv[1], 'r') as file:
    data = file.read().strip()

sys.stdout.write(f"{part1(data)} {part2(data)}")