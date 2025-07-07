import sys

def part1(data):
    return execute({"a": 0, "b": 0}, data)["b"]

def part2(data):
    return execute({"a": 1, "b": 0}, data)["b"]

def execute(registers, data):
    idx = 0
    len_data = len(data)
    while 0 <= idx < len_data:
        inst, *args = data[idx].replace(",", "").split()
        
        if inst == "hlf":
            registers[args[0]] //= 2
        elif inst == "tpl":
            registers[args[0]] *= 3
        elif inst == "inc":
            registers[args[0]] += 1
        elif inst == "jmp":
            idx += int(args[0]) - 1
        elif inst == "jie":
            if registers[args[0]] % 2 == 0:
                idx += int(args[1]) - 1
        elif inst == "jio":
            if registers[args[0]] == 1:
                idx += int(args[1]) - 1
        
        idx += 1

    return registers

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")