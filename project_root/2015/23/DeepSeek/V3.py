import sys

def part1(data):
    return execute({"a": 0, "b": 0}, data)["b"]

def part2(data):
    return execute({"a": 1, "b": 0}, data)["b"]

def execute(registers, instructions):
    idx = 0
    n = len(instructions)
    while 0 <= idx < n:
        inst_parts = instructions[idx].split()
        inst = inst_parts[0]
        offset = 1
        if inst == "hlf":
            registers[inst_parts[1]] //= 2
        elif inst == "tpl":
            registers[inst_parts[1]] *= 3
        elif inst == "inc":
            registers[inst_parts[1]] += 1
        elif inst == "jmp":
            offset = int(inst_parts[1])
        elif inst == "jie":
            reg = inst_parts[1].rstrip(',')
            if registers[reg] % 2 == 0:
                offset = int(inst_parts[2])
        elif inst == "jio":
            reg = inst_parts[1].rstrip(',')
            if registers[reg] == 1:
                offset = int(inst_parts[2])
        idx += offset
    return registers

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]
print(f"{part1(data)}\n{part2(data)}")