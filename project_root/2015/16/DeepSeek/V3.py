import sys

def part1(data):
    tests = {
        "children:": 3,
        "cats:": 7,
        "samoyeds:": 2,
        "pomeranians:": 3,
        "akitas:": 0,
        "vizslas:": 0,
        "goldfish:": 5,
        "trees:": 3,
        "cars:": 2,
        "perfumes:": 1
    }
    
    for line in data:
        parts = line.split()
        sue_num = parts[1][:-1]
        valid = True
        for i in range(2, len(parts), 2):
            key = parts[i]
            value = int(parts[i+1].rstrip(','))
            if tests[key] != value:
                valid = False
                break
        if valid:
            return int(sue_num)
    return -1

def part2(data):
    tests = {
        "children:": 3,
        "cats:": 7,
        "samoyeds:": 2,
        "pomeranians:": 3,
        "akitas:": 0,
        "vizslas:": 0,
        "goldfish:": 5,
        "trees:": 3,
        "cars:": 2,
        "perfumes:": 1
    }
    
    for line in data:
        parts = line.split()
        sue_num = parts[1][:-1]
        valid = True
        for i in range(2, len(parts), 2):
            key = parts[i]
            value = int(parts[i+1].rstrip(','))
            if key in ["cats:", "trees:"]:
                if value <= tests[key]:
                    valid = False
                    break
            elif key in ["pomeranians:", "goldfish:"]:
                if value >= tests[key]:
                    valid = False
                    break
            else:
                if tests[key] != value:
                    valid = False
                    break
        if valid:
            return int(sue_num)
    return -1

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]
sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")