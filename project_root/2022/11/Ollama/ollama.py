import sys
from collections import deque
from math import lcm

def part1(data):
    monkeys, test_lcm= parse_data(data)
    mod = 3

    for _ in range(20):
        for m in monkeys:
            while m["items"]:
                m["times"] += 1
                worry = m["items"].popleft()
                worry //= mod
                worry = m["ope"](worry) % test_lcm
                target = m["target"][worry % m["test"] == 0]
                monkeys[target]["items"].append(worry)

    times = sorted(m["times"] for m in monkeys)
    return times[-1] * times[-2]

def part2(data):
    monkeys, test_lcm= parse_data(data)

    for _ in range(10000):
        for m in monkeys:
            while m["items"]:
                m["times"] += 1
                worry = m["items"].popleft()
                worry = m["ope"](worry) % test_lcm
                target = m["target"][worry % m["test"] == 0]
                monkeys[target]["items"].append(worry)

    times = sorted(m["times"] for m in monkeys)
    return times[-1] * times[-2]

def parse_data(data):
    data = [i.split("\n") for i in ("\n".join(data)).split("\n\n")]
    test_lcm = lcm(*[int(i[3].split("by")[1].strip()) for i in data])

    monkeys = []
    for i in data:
        items = deque(map(int, i[1].split(":")[1].strip().split(", ")))
        match i[2].split("=")[1].strip().split():
            case ["old", "+", "old"]:
                ope = lambda x: x + x
            case ["old", "+", val]:
                ope = lambda x, val=int(val): x + val
            case ["old", "*", "old"]:
                ope = lambda x: x * x
            case ["old", "*", val]:
                ope = lambda x, val=int(val): x * val
        test = int(i[3].split("by")[1].strip())
        target = [int(i[5].split("monkey")[1].strip()), int(i[4].split("monkey")[1].strip())]  # [if_false, if_true]

        monkey = {"items": items, "ope": ope, "test": test, "target": target, "times": 0}
        monkeys.append(monkey)

    return monkeys, test_lcm

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")