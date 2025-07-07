import sys

def part1(data):
    code_len = 0
    mem_len = 0
    for line in data:
        code_len += len(line)
        i = 1
        end = len(line) - 1
        while i < end:
            c = line[i]
            if c == '\\':
                nxt = line[i+1]
                if nxt == 'x':
                    mem_len += 1
                    i += 4
                else:
                    mem_len += 1
                    i += 2
            else:
                mem_len += 1
                i += 1
    return code_len - mem_len

def part2(data):
    code_len = 0
    new_len = 0
    for line in data:
        code_len += len(line)
        line_len = 2
        for c in line:
            if c in ('\\','"'):
                line_len += 2
            else:
                line_len += 1
        new_len += line_len
    return new_len - code_len

with open(sys.argv[1]) as f:
    data = [l.rstrip() for l in f]
print(part1(data))
print(part2(data))