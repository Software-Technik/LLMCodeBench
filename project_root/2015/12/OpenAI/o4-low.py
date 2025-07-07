import sys
import re
import json

def part1(data):
    return sum(map(int, re.findall(r"-?\d+", data[0])))

def part2(data):
    def helper(x):
        if isinstance(x, int):
            return x
        if isinstance(x, list):
            return sum(helper(i) for i in x)
        if isinstance(x, dict):
            if "red" in x.values():
                return 0
            return sum(helper(v) for v in x.values())
        return 0
    return helper(json.loads(data[0]))

with open(sys.argv[1]) as f:
    data = [f.read().strip()]
print(part1(data))
print(part2(data))