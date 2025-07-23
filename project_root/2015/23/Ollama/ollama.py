import sys

def part1(data):
    r = {"a": 0, "b": 0}
    idx = 0
    while idx < len(data):
        inst, inst_data = data[idx].split(" ", 1)
        if inst == "hlf":
            r[inst_data] //= 2
        elif inst == "tpl":
            r[inst_data] *= 3
        elif inst == "inc":
            r[inst_data] += 1
        elif inst == "jmp":
            idx += int(inst_data) - 1
        elif inst == "jie":
            p, o = inst_data.split(", ")
            if not r[p] % 2:
                idx += int(o) - 1
        elif inst == "jio":
            p, o = inst_data.split(", ")
            if r[p] == 1:
                idx += int(o) - 1
        idx += 1
    return r["b"]

def part2(data):
    r = {"a": 1, "b": 0}
    idx = 0
    while idx < len(data):
        inst, inst_data = data[idx].split(" ", 1)
        if inst == "hlf":
            r[inst_data] //= 2
        elif inst == "tpl":
            r[inst_data] *= 3
        elif inst == "inc":
            r[inst_data] += 1
        elif inst == "jmp":
            idx += int(inst_data) - 1
        elif inst == "jie":
            p, o = inst_data.split(", ")
            if not r[p] % 2:
                idx += int(o) - 1
        elif inst == "jio":
            p, o = inst_data.split(", ")
            if r[p] == 1:
                idx += int(o) - 1
        idx += 1
    return r["b"]

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")