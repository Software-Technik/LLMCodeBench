import sys

def part1(data):
    code_len = 0
    memory_size = 0
    for line in data:
        code_len += len(line)
        i = 1
        memory_size -= 2  # accounts for the enclosing quotes
        while i < len(line) - 1:
            if line[i] == '\\':
                if line[i + 1] in ('\\', '"'):
                    i += 1
                elif line[i + 1] == 'x':
                    i += 3
            memory_size += 1
            i += 1
    return code_len + memory_size

def part2(data):
    code_len = 0
    new_code_len = 0
    for line in data:
        code_len += len(line)
        new_code_len += 2  # adds for the enclosing quotes
        for c in line:
            if c in ('\\', '"'):
                new_code_len += 2
            else:
                new_code_len += 1
    return new_code_len - code_len

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")