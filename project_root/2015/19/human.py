import sys

def part1(data):
    replacements = data[:-2]
    molecule = data[-1]
    new_molecules = set()

    for replacement in replacements:
        a, b = replacement.split(" => ")
        for i in range(len(molecule)):
            if molecule[i : i + len(a)] == a:
                new_molecule = molecule[:i] + b + molecule[i + len(a) :]
                new_molecules.add(new_molecule)

    return len(new_molecules)

def part2(data):
    molecule = data[-1]
    replacements = {i[1]: i[0] for i in [i.split(" => ") for i in data[:-2]]}
    count = 0

    # matching from the left seems not work, tried from the right and it works
    while molecule != "e":
        matched = []
        for rep in replacements:
            if replacements[rep] == "e" and rep != molecule:
                continue
            if rep in molecule:
                matched += [(rep, molecule.rindex(rep))]
        matched = sorted(matched, key=lambda i: i[1])
        right_most = matched[-1][0]

        molecule = replacements[right_most].join(molecule.rsplit(right_most, 1))
        count += 1

    return count

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")