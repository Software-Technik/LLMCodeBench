import sys

tests = {
    "children": (lambda x, y: x == y, 3),
    "cats": (lambda x, y: x > y, 7),
    "samoyeds": (lambda x, y: x == y, 2),
    "pomeranians": (lambda x, y: x < y, 3),
    "akitas": (lambda x, y: x == y, 0),
    "vizslas": (lambda x, y: x == y, 0),
    "goldfish": (lambda x, y: x < y, 5),
    "trees": (lambda x, y: x > y, 3),
    "cars": (lambda x, y: x == y, 2),
    "perfumes": (lambda x, y: x == y, 1),
}

def parse(data):
    sues = []
    for line in data:
        id_part, rest = line.split(":", 1)
        num = int(id_part.split()[1])
        items = {}
        for pair in rest.strip().split(","):
            if pair:
                k, v = pair.strip().split(":")
                items[k] = int(v)
        sues.append((num, items))
    return sues

def part1(sues):
    for num, items in sues:
        if all(tests[k][0](items.get(k, tests[k][1]), v) for k, (tests_k, v) in tests.items() if k in items):
            return num

def part2(sues):
    for num, items in sues:
        ok = True
        for k, val in items.items():
            cmpfunc, tv = tests[k]
            if not cmpfunc(val, tv):
                ok = False
                break
        if ok:
            return num

data = open(sys.argv[1]).read().strip().splitlines()
sues = parse(data)
print(part1(sues))
print(part2(sues))