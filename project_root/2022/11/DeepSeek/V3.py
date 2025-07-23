import sys
from collections import deque
from math import lcm

def part1(data):
    monkeys = parse_data(data)

    for _ in range(20):
        for m in monkeys:
            items = m["items"]
            m["times"] += len(items)
            while items:
                worry = items.popleft()
                worry = m["ope"](worry) // 3
                target = m["target"][worry % m["test"] == 0]
                monkeys[target]["items"].append(worry)

    times = sorted(m["times"] for m in monkeys)
    return times[-1] * times[-2]

def part2(data):
    monkeys = parse_data(data)
    test_lcm = lcm(*[m["test"] for m in monkeys])

    for _ in range(10000):
        for m in monkeys:
            items = m["items"]
            m["times"] += len(items)
            while items:
                worry = m["ope"](items.popleft()) % test_lcm
                target = m["target"][worry % m["test"] == 0]
                monkeys[target]["items"].append(worry)

    times = sorted(m["times"] for m in monkeys)
    return times[-1] * times[-2]

def parse_data(data):
    data = [i.split("\n") for i in ("\n".join(data)).split("\n\n")]
    monkeys = []
    for i in data:
        items = deque(map(int, i[1].split(":")[1].strip().split(", ")))
        op_parts = i[2].split("=")[1].strip().split()
        if op_parts[1] == '+':
            if op_parts[2] == 'old':
                ope = lambda x: x + x
            else:
                val = int(op_parts[2])
                ope = lambda x, val=val: x + val
        else:
            if op_parts[2] == 'old':
                ope = lambda x: x * x
            else:
                val = int(op_parts[2])
                ope = lambda x, val=val: x * val
        test = int(i[3].split("by")[1].strip())
        target = [int(i[5].split("monkey")[1].strip()), int(i[4].split("monkey")[1].strip())]
        monkeys.append({"items": items, "ope": ope, "test": test, "target": target, "times": 0})
    return monkeys

input_strings = sys.argv[1]
with open(input_strings) as f:
    data = [line.strip() for line in f]

sys.stdout.write(f"{part1(data)}\n{part2(data)}\n")