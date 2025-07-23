import sys

def part1(data):
    total = 0
    i = 0
    n = len(data)
    while i < n:
        if data[i] == '(':
            j = data.find(')', i)
            if j == -1:
                break
            marker = data[i+1:j]
            parts = marker.split('x')
            if len(parts) != 2:
                i += 1
                continue
            try:
                length = int(parts[0])
                times = int(parts[1])
            except:
                i += 1
                continue
            total += times * length
            i = j + 1 + length
        else:
            total += 1
            i += 1
    return total

def part2(data):
    total = 0
    i = 0
    n = len(data)
    stack = []
    current_multiplier = 1
    while i < n:
        if data[i] == '(':
            j = data.find(')', i)
            if j == -1:
                break
            marker = data[i+1:j]
            parts = marker.split('x')
            if len(parts) != 2:
                i += 1
                continue
            try:
                length = int(parts[0])
                times = int(parts[1])
            except:
                i += 1
                continue
            end_segment = j + 1 + length
            stack.append((end_segment, current_multiplier))
            current_multiplier *= times
            i = j + 1
        else:
            while stack and stack[-1][0] == i:
                _, saved_mult = stack.pop()
                current_multiplier = saved_mult
            total += current_multiplier
            i += 1
    return total

inout_strings = sys.argv[1]
with open(inout_strings, 'r') as infile:
    data = infile.read()

sys.stdout.write(f"{part1(data)} {part2(data)}")