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
perfumes: 1""".split(
        "\n"
    )

    test_data = data
    new_data = []
    for t in tests:
        a, b = t.split(" ")
        for i in test_data:
            if a not in i or t in i:
                new_data += [i]
        test_data = new_data
        new_data = []
    return test_data

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
perfumes: 1""".split(
        "\n"
    )

    test_data = data
    new_data = []
    for t in tests:
        a, b = t.split(" ")
        for i in test_data:
            if a not in i:
                new_data += [i]
            else:
                if a in ["cats:", "trees:"]:
                    thing = [k for k in i.split(": ", 1)[1].split(", ") if a in k]
                    if len(thing) < 1 or int(thing[0].split(": ")[1]) > int(b):
                        new_data += [i]
                elif a in ["pomeranians:", "goldfish:"]:
                    thing = [k for k in i.split(": ", 1)[1].split(", ") if a in k]
                    if len(thing) < 1 or int(thing[0].split(": ")[1]) < int(b):
                        new_data += [i]
                elif t in i:
                    new_data += [i]
        test_data = new_data
        new_data = []
    return test_data

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")