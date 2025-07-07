import sys

def part1(data):
    tests = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    for sue in data:
        sue_data = sue.split(": ", 1)[1].replace(" ", "").split(",")
        sue_dict = {item.split(":")[0]: int(item.split(":")[1]) for item in sue_data}
        if all(sue_dict.get(item, tests[item]) == tests[item] for item in tests if item in sue_dict):
            return int(sue.split()[1][:-1])
    return None

def part2(data):
    tests = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }

    for sue in data:
        sue_data = sue.split(": ", 1)[1].replace(" ", "").split(",")
        sue_dict = {item.split(":")[0]: int(item.split(":")[1]) for item in sue_data}
        if all(
            (item in ["cats", "trees"] and sue_dict.get(item, tests[item] + 1) > tests[item]) or
            (item in ["pomeranians", "goldfish"] and sue_dict.get(item, tests[item] - 1) < tests[item]) or
            (sue_dict.get(item, tests[item]) == tests[item])
            for item in tests if item in sue_dict
        ):
            return int(sue.split()[1][:-1])
    return None

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")