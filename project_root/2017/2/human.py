import sys

def part1(spreadsheet):
    return sum(max(row) - min(row) for row in spreadsheet)

def part2(spreadsheet):
    total = 0
    for row in spreadsheet:
        for a in row:
            for b in row:
                if a != b and a % b == 0:
                    total += a // b
                    break
    return total

def parse_input(input_path):
    with open(input_path) as f:
        return [list(map(int, line.strip().split())) for line in f if line.strip()]

# Lecture du fichier et traitement
input_strings = sys.argv[1]
data = parse_input(input_strings)

# Affichage des résultats
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")