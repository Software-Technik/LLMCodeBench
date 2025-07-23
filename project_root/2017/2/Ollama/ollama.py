import sys

def part1(spreadsheet):
    return sum(max(row) - min(row) for row in spreadsheet)

def part2(spreadsheet):
    total = 0
    for row in spreadsheet:
        max_divisor = -float('inf')
        for a in row:
            for b in row:
                if a != b and a % b == 0:
                    max_divisor = max(max_divisor, a // b)
                    break
        total += max_divisor
    return total

def parse_input(input_path):
    with open(input_path) as f:
        data = []
        for line in f:
            line = line.strip()
            if not line: continue
            data.append(list(map(int, line.split())))
    return data

# Lecture du fichier et traitement
input_strings = sys.argv[1]
data = parse_input(input_strings)

# Affichage des résultats
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")