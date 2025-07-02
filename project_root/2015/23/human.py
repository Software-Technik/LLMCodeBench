import sys

def part1(data):
    r = exec({"a": 0, "b": 0}, data)
    return r["b"]

def part2(data):
    r = exec({"a": 1, "b": 0}, data)
    return r["b"]

def exec(r, data):
    idx = 0
    while idx in range(len(data)):
        offset = 1
        inst, inst_data = data[idx].split(" ", 1)
        if inst == "hlf":
            r[inst_data] = r[inst_data] // 2
        elif inst == "tpl":
            r[inst_data] = r[inst_data] * 3
        elif inst == "inc":
            r[inst_data] += 1
        elif inst == "jmp":
            offset = int(inst_data)
        elif inst == "jie":
            p, o = inst_data.split(", ")
            if r[p] % 2 == 0:
                offset = int(o)
        elif inst == "jio":
            p, o = inst_data.split(", ")
            if r[p] == 1:
                offset = int(o)
        idx += offset
    return r

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")