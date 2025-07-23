import sys

def part1(data):
    replacements = data[:-2]
    molecule = data[-1]
    new_molecules = set()

    for replacement in replacements:
        a, b = replacement.split(" => ")
        a_len = len(a)
        for i in range(len(molecule) - a_len + 1):
            if molecule.startswith(a, i):
                new_molecule = molecule[:i] + b + molecule[i + a_len:]
                new_molecules.add(new_molecule)

    return len(new_molecules)

def part2(data):
    molecule = data[-1]
    replacements = {i[1]: i[0] for i in [i.split(" => ") for i in data[:-2]]}
    count = 0

    while molecule != "e":
        matched = []
        for rep in replacements:
            if replacements[rep] == "e" and rep != molecule:
                continue
            pos = molecule.rfind(rep)
            if pos != -1:
                matched.append((rep, pos))
        if not matched:
            break
        matched.sort(key=lambda x: x[1])
        right_most = matched[-1][0]
        molecule = molecule.rsplit(right_most, 1)[0] + replacements[right_most] + molecule.rsplit(right_most, 1)[1]
        count += 1

    return count

input_file = sys.argv[1]
with open(input_file) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")