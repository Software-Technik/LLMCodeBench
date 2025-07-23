import sys

def part1(data):
    return sum(ord(("".join(set(line[:_sep]) & set(line[_sep:])))) - (38 if b.islower() else 96) for line in data for _sep, b in [(len(line)//2, *set(line).intersection(*map(set, [line[:len(line)//2], line[len(line)//2:]])))])

def part2(data):
    return sum(ord("".join(set(data[i]) & set(data[i+1]) & set(data[i+2]))) - (38 if b.islower() else 96) for i in range(0, len(data), 3) for b in ["".join(set(data[i]) & set(data[i+1]) & set(data[i+2]))])

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")