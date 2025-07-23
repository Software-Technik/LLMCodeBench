import sys

input_path = sys.argv[1]

try:
    with open(input_path) as f:
        data = f.read()
        lines = data.splitlines()
except:
    data, lines = "", []

def line_transform(line):
    return line.split(",")

lines = [line_transform(line) for line in lines]

def solve(limit):
    before = {}
    before2 = {}
    nums = list(map(int, data.split(",")))
    turn = 0
    last = None
    for num in nums:
        before[num] = turn
        last = num
        turn += 1
    while turn < limit:
        if last in before2:
            to_speak = before[last] - before2[last]
        else:
            to_speak = 0
        if to_speak in before:
            before2[to_speak] = before[to_speak]
        before[to_speak] = turn
        last = to_speak
        turn += 1
    return last

result1 = solve(2020)
result2 = solve(30000000)
print(result1, result2)