import sys

def part1(data):
    replacements = data[:-2]
    molecule = data[-1]
    new_molecules = set()
    molecule_len = len(molecule)

    for replacement in replacements:
        a, b = replacement.split(" => ")
        a_len = len(a)
        for i in range(molecule_len - a_len + 1):
            if molecule[i : i + a_len] == a:
                new_molecules.add(molecule[:i] + b + molecule[i + a_len :])

    return len(new_molecules)

def part2(data):
    molecule = data[-1]
    replacements = {i[1]: i[0] for i in (line.split(" => ") for line in data[:-2])}
    count = 0

    while molecule != "e":
        matched = [(rep, molecule.rindex(rep)) for rep in replacements if rep in molecule]
        right_most = max(matched, key=lambda i: i[1])[0]
        molecule = molecule.rsplit(right_most, 1)
        molecule = replacements[right_most].join(molecule)
        count += 1

    return count

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")