import sys

def part1(spreadsheet):
    return sum(max(row) - min(row) for row in spreadsheet)

def part2(spreadsheet):
    total = 0
    for row in spreadsheet:
        row_sorted = sorted(row, reverse=True)
        n = len(row_sorted)
        for i in range(n):
            a = row_sorted[i]
            for j in range(i+1, n):
                b = row_sorted[j]
                if a % b == 0:
                    total += a // b
                    break
            else:
                continue
            break
    return total

def parse_input(input_path):
    with open(input_path) as f:
        return [list(map(int, line.strip().split())) for line in f if line.strip()]

input_strings = sys.argv[1]
data = parse_input(input_strings)
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")