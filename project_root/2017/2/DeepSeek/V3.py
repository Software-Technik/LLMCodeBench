import sys

def part1(spreadsheet):
    return sum(max(row) - min(row) for row in spreadsheet)

def part2(spreadsheet):
    total = 0
    for row in spreadsheet:
        row_sorted = sorted(row, reverse=True)
        for i in range(len(row_sorted)):
            for j in range(i + 1, len(row_sorted)):
                if row_sorted[i] % row_sorted[j] == 0:
                    total += row_sorted[i] // row_sorted[j]
                    break
    return total

def parse_input(input_path):
    with open(input_path) as f:
        return [list(map(int, line.strip().split())) for line in f if line.strip()]

input_strings = sys.argv[1]
data = parse_input(input_strings)

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")