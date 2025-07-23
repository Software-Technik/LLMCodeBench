import sys
import re

def part1(data):
    code_len, memory_size = 0, 0
    for line in data:
        decoded = re.sub(r'\\x[0-9a-f]{2}', lambda m: bytes.fromhex(m.group(0)[2:]).decode(), line[1:-1].replace('\\\\', '/').replace("\\\"", '"'))
        code_len += len(line)
        memory_size += len(decoded)
    return code_len - memory_size

def part2(data):
    code_len, new_code_len = 0, 0
    for line in data:
        new_line = re.sub(r'(["\\])', lambda c: (c.group(1) == '"') * '\\"' + ('\\' if c.group(1) == '\\' else ''), line)
        code_len += len(line)
        new_code_len += len(new_line) + 2
    return new_code_len - code_len

with open(sys.argv[1]) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}")