import sys

def part1(spreadsheet):
    return sum(max(row) - min(row) for row in spreadsheet)

def part2(spreadsheet):
    total = 0
    for row in spreadsheet:
        row_set = set(row)
        for a in row:
            for b in row_set:
                if a % b == 0 and a != b:
                    total += a // b
                    break
    return total

def parse_input(input_path):
    with open(input_path) as f:
        return [list(map(int, line.split())) for line in f if line.strip()]

input_strings = sys.argv[1]
data = parse_input(input_strings)

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")