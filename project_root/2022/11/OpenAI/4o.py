from collections import deque
from math import lcm
import sys

def part1(data):
    monkeys = parse_data(data)

    for _ in range(20):
        for m in monkeys:
            items = m["items"]
            ope = m["ope"]
            target = m["target"]
            test = m["test"]
            times = m["times"]
            while items:
                times += 1
                worry = items.popleft()
                worry = ope(worry) // 3
                monkeys[target[worry % test == 0]]["items"].append(worry)
            m["times"] = times

    times = sorted(m["times"] for m in monkeys)
    return times[-1] * times[-2]

def part2(data):
    monkeys = parse_data(data)
    test_lcm = lcm(*[m["test"] for m in monkeys])

    for _ in range(10000):
        for m in monkeys:
            items = m["items"]
            ope = m["ope"]
            target = m["target"]
            test = m["test"]
            times = m["times"]
            while items:
                times += 1
                worry = items.popleft()
                worry = ope(worry) % test_lcm
                monkeys[target[worry % test == 0]]["items"].append(worry)
            m["times"] = times

    times = sorted(m["times"] for m in monkeys)
    return times[-1] * times[-2]

def parse_data(data):
    data = [block.split("\n") for block in "\n".join(data).split("\n\n")]

    monkeys = []
    for block in data:
        items = deque(map(int, block[1].split(":")[1].strip().split(", ")))
        operations = block[2].split("=")[1].strip().split()
        if operations == ["old", "+", "old"]:
            ope = lambda x: x + x
        elif operations[1] == "+":
            val = int(operations[2])
            ope = lambda x: x + val
        elif operations == ["old", "*", "old"]:
            ope = lambda x: x * x
        else:
            val = int(operations[2])
            ope = lambda x: x * val
        test = int(block[3].split("by")[1].strip())
        target = [int(block[5].split("monkey")[1].strip()), int(block[4].split("monkey")[1].strip())]

        monkeys.append({"items": items, "ope": ope, "test": test, "target": target, "times": 0})

    return monkeys

if __name__ == "__main__":
    input_file = sys.argv[1]
    with open(input_file) as f:
        data = [line.strip() for line in f]

    print(part1(data))
    print(part2(data))