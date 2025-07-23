import sys

def part1(data):
    tests = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split("\n")
    test_data = data[:]
    for t in tests:
        key, val = t.split(": ")
        val = int(val)
        test_data = [d for d in test_data if not (key + ": " + str(val)) in d]
    return int(test_data[0].split()[1][:-1])

def part2(data):
    tests = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""".split("\n")
    test_data = data[:]
    for t in tests:
        key, val = t.split(": ")
        val = int(val)
        if key == "cats:" or key == "trees:":
            test_data = [d for d in test_data if not (key + ": " + str(val)) in d or int(d.split(key)[1].split()[0]) > val]
        elif key == "pomeranians:" or key == "goldfish:":
            test_data = [d for d in test_data if not (key + ": " + str(val)) in d or int(d.split(key)[1].split()[0]) < val]
        else:
            test_data = [d for d in test_data if not (key + ": " + str(val)) in d]
    return int(test_data[0].split()[1][:-1])

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
print(f"{part1(data)}\n{part2(data)}")